import typing


class Model:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        training_library: str,
        serialized_model: typing.IO,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.training_library = training_library
        self.serialized_model = serialized_model

    @classmethod
    def from_dict(cls, data: typing.Dict):
        return Model(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            training_library=data.get('training_library'),
            serialized_model=data.get('serialized_model'),
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
