
import os
import datetime as dt

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

fred_api_key = '01252873c8aee98f0a2400cc57dee1b1'
now = dt.datetime.now()
month = now.strftime('%m')
year = now.year
data_primary = (str(os.getcwd()) +
                '\\data\\raw\\primary_dataset_v{}_{}_01.json'.format(year, month))
data_primary_most_recent = (str(os.getcwd()) +
                            '\\data\\raw\\primary_dataset_most_recent.json')
data_secondary = (str(os.getcwd()) +
                  '\\data\\interim\\secondary_dataset_v{}_{}_01.json'.format(year, month))
data_secondary_most_recent = (str(os.getcwd()) +
                              '\\data\\interim\\secondary_dataset_most_recent.json')
data_final = (str(os.getcwd()) + '\\data\\processed\\final_dataset.json')
exploratory_plots = (str(os.getcwd()) + '\\reports\\figures\\exploratory.pdf')
test_results_plots = (str(os.getcwd()) + '\\reports\\figures\\test_results.pdf')
deployment_results_plots = (str(os.getcwd()) + '\\reports\\figures\\deployment_results.pdf')
cv_results = (str(os.getcwd()) + '\\models\\model_metadata\\cv_results.json')
cv_metadata = (str(os.getcwd()) + '\\models\\model_metadata\\cv_metadata.json')
pred_model_metadata = (str(os.getcwd()) +
                       '\\models\\model_metadata\\pred_metadata.json')
prediction_errors = (str(os.getcwd()) +
                     '\\models\\model_metadata\\prediction_errors.json')
full_predictions = (str(os.getcwd()) +
                    '\\models\\model_metadata\\full_predictions.json')
knn_test_results = (str(os.getcwd()) +
                    '\\models\\testing_data\\knn_test_results.json')
elastic_net_test_results = (str(os.getcwd()) +
                            '\\models\\testing_data\\elastic_net_test_results.json')
naive_bayes_test_results = (str(os.getcwd()) +
                            '\\models\\testing_data\\naive_bayes_test_results.json')
svm_test_results = (str(os.getcwd()) +
                    '\\models\\testing_data\\svm_test_results.json')
gauss_test_results = (str(os.getcwd()) +
                      '\\models\\testing_data\\gauss_test_results.json')
xgboost_test_results = (str(os.getcwd()) +
                        '\\models\\testing_data\\xgboost_test_results.json')
weighted_average_test_results = (str(os.getcwd()) +
                                 '\\models\\testing_data\\weighted_average_test_results.json')
deployment_cv_results = (str(os.getcwd()) + '\\models\\model_metadata\\deployment_cv_results.json')
deployment_cv_metadata = (str(os.getcwd()) + '\\models\\model_metadata\\deployment_cv_metadata.json')
deployment_pred_model_metadata = (str(os.getcwd()) +
                                  '\\models\\model_metadata\\deployment_pred_metadata.json')
deployment_full_predictions = (str(os.getcwd()) +
                               '\\models\\model_metadata\\deployment_full_predictions.json')
deployment_svm_test_results = (str(os.getcwd()) +
                               '\\models\\testing_data\\deployment_svm_test_results.json')
deployment_chart_data = (str(os.getcwd()) + '\\reports\\deployment_chart.csv')

