import pandas as pd
import numpy as np
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
import mlflow
import mlflow.sklearn
import logging


mlflow.set_tracking_uri( 'https://dagshub.com/yotitan/MLOps-Dagshub-Demo.mlflow' )
tracking_uri = mlflow.get_tracking_uri( )
print( 'Current tracking uri: {}'.format(tracking_uri) )


logging.basicConfig( level=logging.WARN )
logger = logging.getLogger( __name__ )

def eval_metrics( actual, pred ):
    rmse = np.sqrt( mean_squared_error(actual, pred) )
    mae = mean_absolute_error( actual, pred )
    r2 = r2_score( actual, pred )
    return rmse, mae, r2

def main( ):
    
    dat = pd.read_csv( '../../data/raw/winequality-red.csv' )

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split( dat )
     
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop( columns=['quality'] )
    test_x = test.drop( columns=['quality'] )
    train_y = train[['quality']]
    test_y = test[['quality']]

    std = StandardScaler( )
    train_x = std.fit_transform( train_x )
    test_x = std.transform( test_x )


    alpha = float( sys.argv[1] ) if len(sys.argv) > 1 else 0.5
    l1_ratio = float( sys.argv[2] ) if len(sys.argv) > 2 else 0.5

    with mlflow.start_run( ):
        lr = ElasticNet( alpha=alpha, l1_ratio=l1_ratio, random_state=42 )
        lr.fit( train_x, train_y )

        predicted_qualities = lr.predict( test_x )

        ( rmse, mae, r2 ) = eval_metrics( test_y, predicted_qualities )

        print( 'Elasticnet model (alpha=%f, l1_ratio=%f):' % (alpha, l1_ratio) )
        print( '\tRMSE : %s' % rmse )
        print( '\tMAE  : %s' % mae )
        print( '\tR2   : %s' % r2 )

        mlflow.log_param( 'alpha', alpha )
        mlflow.log_param( 'l1_ratio', l1_ratio )
        mlflow.log_metric( 'rmse', rmse )
        mlflow.log_metric( 'r2', r2 )
        mlflow.log_metric( 'mae', mae )

        # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry 
        mlflow.sklearn.log_model( lr, 'model' )

if __name__ == '__main__':
    main( )