import warnings
import flwr as fl
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from params import SetParams
import os.path
import time
from request import getResult

import utils

if __name__ == "__main__":
    path = './model.pkl'
    check_file = os.path.isfile(path)
    (X_train, y_train), (X_test, y_test) = utils.load_transaction_data()

    # Split train set into 10 partitions and randomly use one for training.
    # Create LogisticRegression Model
    model = LogisticRegression(
        penalty="l2",
        max_iter=1,  # local epoch
        warm_start=True,  # prevent refreshing weights when fitting
    )

    # Setting initial parameters, akin to model.compile for keras models
    utils.set_initial_params(model)
    class TrainModel(fl.client.NumPyClient):
        def __init__(self,model, X, Y):
            self.model = model
            self.X = X
            self.Y = Y
        def get_parameters(self, config):  # type: ignore
            return utils.get_model_parameters(self.model)

        def fit(self, parameters, config):  # type: ignore
            utils.set_model_params(self.model, parameters)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.model.fit(self.X, self.Y)
            print(f"Training finished for round {config['server_round']}")
            return utils.get_model_parameters(self.model), len(self.X) ,{}

        # def evaluate(self, parameters, config):  # type: ignore
        #     # utils.set_model_params(self.model, parameters)
        #     # loss = log_loss(y_test, self.model.predict_proba(X_test))
        #     # accuracy = self.model.score(X_test, y_test)
        #     # return loss, len(X_test), {"accuracy": accuracy}
        #     pass
            
    # Start Flower client
    
    while(True):
        if not check_file:
            (X, Y), _= utils.load_transaction_data()
            client = TrainModel(model, X, Y)
            fl.client.start_numpy_client(server_address="localhost:8080", client=client)
            pickle.dump(model, open('model.pkl', 'wb'))  
        else:
            X  = getResult()
            model1 = LogisticRegression(
                penalty="l2",
                max_iter=1,  # local epoch
                warm_start=True,  # prevent refreshing weights when fitting
            )
            X = np.array(X)
            # getting the client state
            pickleModel = pickle.load(open(path, 'rb'))
            result = pickleModel.predict(X)
            result[-1] = 1
            result = result.reshape((len(result) , 1))

            #setting the models parameters
            model = utils.set_model_params(model1,(pickleModel.coef_,pickleModel.intercept_))
            client = TrainModel(model, X, result)
            fl.client.start_numpy_client(server_address="localhost:8080", client=client)
            pickle.dump(model, open('model.pkl', 'wb'))