import os
import typing

from werkzeug.utils import secure_filename

from .loaders import SklearnLoader
from .repositories import AbstractRepo
from .domain import Model


# TODO /persisted_models dir as config envvar
def create_model(repo: AbstractRepo, data: typing.Dict) -> Model:
    serialized_model_file = data.get('serialized_model')
    file_absolute_path = os.path.join(
        '/persisted_models', secure_filename(serialized_model_file.filename)
    )
    serialized_model_file.save(file_absolute_path)

    data.pop('serialized_model')
    data['serialized_model_path'] = file_absolute_path
    return repo.add(Model.from_dict(data))


def list_models(repo) -> typing.List[Model]:
    return repo.list()


def get_model_detail(repo, model_id):
    return repo.get(model_id)


def predict(repo, model_id, instances_data):
    model = repo.get(model_id)

    if model.training_library == Model.LIBRARY_SKLEARN:
        clf = SklearnLoader.load(model.serialized_model_path)
        return clf.predict(instances_data)

    return {}
