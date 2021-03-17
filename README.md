# MLDeploy: Easily deploy your machine models to production

**MLDeploy** is a web application to convert your machine learning models into restful web APIs.
Upload your scikit-learn, Keras or Tensorflow trained model and specify the features of your dataset.
A prediction endpoint is provided to the user, exposing its machine learning model, ready to accept instances to predict.

> :warning: **Security warning**: This project [unpickles untrusted objects](https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations), so arbitrary python code could be executed. Do not allow untrusted users to upload models to your deployment.

## Usage

## Configuration

TODO

## How to Deploy

```
docker-compose up -d
```

## Features

 * Expose a prediction JSON API from a trained persisted model
 * Support for multiple ML libraries: scikit-learn, keras, tensorflow
 * Statistics about prediction requests and responses
