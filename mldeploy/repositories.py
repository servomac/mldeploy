import abc
import itertools

from mldeploy.domain import Model


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


class SqlAlchemyRepo(AbstractRepo):
    def __init__(self, session, domain_class):
        self.domain_class = domain_class
        self.session = session

    def add(self, data):
        self.session.add(data)
        self.session.commit()
        return data

    def get(self, identifier: int):
        return self.session.query(self.domain_class).get(identifier)

    def list(self):
        return self.session.query(self.domain_class).all()

    def delete(self, id):
        pass


class SqlAlchemyModelRepo(SqlAlchemyRepo):
    def __init__(self, session):
        super().__init__(session, Model)
