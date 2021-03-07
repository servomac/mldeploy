import typing

from .repositories import AbstractRepo
from .domain import Model


def create_model(repo: AbstractRepo, data: typing.Dict) -> Model:
    return repo.add(Model.from_dict(data))


def list_models(repo) -> typing.List[Model]:
    return repo.list()


def get_model_detail(repo, model_id):
    return repo.get(model_id)


def predict(repo, model_id, instances_data):
    model = repo.get(model_id)
    return model.predict(instances_data)
