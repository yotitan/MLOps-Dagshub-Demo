# MLOps DagsHub Demo
Step 1:
    Create Git repo
    create DagsHub repo: https://dagshub.com

Step 2:
    install DVC
    dvc init
    configure dvc:
        dvc remote add origin https://dagshub.com/yotitan/MLOps-Dagshub-Demo.dvc
        dvc remote modify origin --local auth basic
        dvc remote modify origin --local user yotitan
        dvc remote modify origin --local password $DAGSHUB_TOKEN

        dvc pull -r origin
        dvc add data/raw
        dvc push -r origin    

Step 3:
    install mlflow

    # add the following in the python code!
    mlflow.set_tracking_uri("https://dagshub.com/sashicds/MLOPS-Dagshub.mlflow")
    tracking_uri = mlflow.get_tracking_uri()
    print("Current tracking uri: {}".format(tracking_uri))

    export MLFLOW_TRACKING_USERNAME=sashicds
    export MLFLOW_TRACKING_PASSWORD=$DAGSHUB_TOKEN

# Install Docker/Jenkins
# Docker
     https://docs.docker.com/desktop/linux/install/ubuntu/

# Jenkins     
     $ docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
     
     $ docker ps
     $ docker logs d899d573f167 (CONTAINER ID obtained from docker ps)
      ubuntu : /var/snap/docker/common/var-lib-docker
      
     Open http://localhost:8080 & enter the password
     Install default packages
     Create First Admin User
     Jenkins URL: http://localhost:8080/



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
