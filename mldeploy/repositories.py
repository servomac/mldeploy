import abc
import itertools


class AbstractRepo(abc.ABC):
    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id):
        raise NotImplementedError


class InMemoryRepo(AbstractRepo):
    identifier = 'id'

    def __init__(self, elements=None):
        self.elements = elements or []
        self.counter = itertools.count(1).__next__

    def add(self, data):
        data.id = self.counter()
        self.elements.append(data)
        return data

    def get(self, id):
        for element in self.elements:
            if element.id == id:
                return element
        return None

    def list(self):
        return self.elements

    def delete(self, id):
        element = self.get(id)
        if element:
            self.elements.remove(element)
            return element

        return None
