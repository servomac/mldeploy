import typing


class Model:
    LIBRARY_SKLEARN = 'scikit-learn'

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        training_library: str,
        serialized_model_path: str,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.training_library = training_library
        self.serialized_model_path = serialized_model_path

    @classmethod
    def from_dict(cls, data: typing.Dict):
        return Model(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            training_library=data.get('training_library'),
            serialized_model_path=data.get('serialized_model_path'),
        )

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'training_library': self.training_library,
        }

    def predict(self, instances_data):
        raise NotImplementedError
