from prediction_model import PredictionModel

class RandomForestModel(PredictionModel):
    # Attributes-------------------------------------
    n_estimators = 0 # minimum amount of trees
    min_sample_tree = 3 # minimum amount of sample in trees
    
    # Constructor------------------------------------
    def __init__(self,var_n_estimators
                     ,var_min_sample_tree):
        self.n_estimators = var_n_estimators
        self.min_sample_tree = var_min_sample_tree
    # Methods----------------------------------------

    #@Abstract method
    def fit_data(self, data_train, data_class):
        pass
    #@Abstract method
    def predict_data(self, data_test):
        pass
    #@Abstract method
    def report_result(self):
        pass

    def get_binary_probability(self,var_data_column,var_value):
        var_probability =  var_data_column.groupby(var_value).size()