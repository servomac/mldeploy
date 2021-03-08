import abc
import joblib


class BaseLoader(abc.ABC):
    @classmethod
    def load(cls, file):
        raise NotImplementedError


class SklearnLoader(BaseLoader):
    @classmethod
    def load(cls, file):
        """
        Loads a scikit-learn model from an absolute path in disk.
        """
        # TODO SECURITY: This is a security vulnerability, you cannot just load 
        # untrusted objects, or arbitrary python code could be executed.
        return joblib.load(file)


class TensorflowLoader(BaseLoader):
    @classmethod
    def load(cls, file):
        pass
