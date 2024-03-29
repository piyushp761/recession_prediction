

import os
import argparse
import datetime as dt

os.chdir(os.path.dirname(os.path.abspath(__file__))) 
import src.data.make_dataset as mk
import src.features.build_features_and_labels as ft
import src.visualization.exploratory_analysis as exp
import src.models.testing as test
import src.visualization.test_results as test_results
import src.models.deployment as deploy
import src.visualization.deployment_results as deploy_results


now = dt.datetime.now()
month = now.strftime('%m')
year = now.year

if now.day < 7:
    raise Exception("""
                    Invalid date. Please run this program on or after
                    the 7th calendar day of the current month.
                    """)
    
parser = argparse.ArgumentParser()
parser.add_argument('process', type=str,
                    help=
                    """
                    Which process would you like to run? Choices are "backtest"
                    or "deploy".
                    """,
                    choices=['backtest', 'deploy'])
args = parser.parse_args()
process = args.process

if process == 'backtest':
   get_data = mk.MakeDataset().get_all_data()
   build_features = ft.FinalizeDataset().create_final_dataset()
   explore_data = exp.ExploratoryAnalysis().explore_dataset()
   backtest = test.Backtester().run_test_procedures()
   plot_backtest = test_results.TestResultPlots().plot_test_results()
    
elif process == 'deploy':
   get_data = mk.MakeDataset().get_all_data()
   build_features = ft.FinalizeDataset().create_final_dataset()
   deploy = deploy.Deployer().run_test_procedures()
   plot_deploy = deploy_results.TestResultPlots().plot_test_results()
   
