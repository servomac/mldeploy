import joblib


def sklearn_load(file):
    """
    Loads a scikit-learn model from an absolute path in disk.
    """
    # TODO SECURITY: This is a security vulnerability, you cannot just load 
    # untrusted objects, or arbitrary python code could be executed.
    return joblib.load(file)


def tensorflow_load(file):
    pass
