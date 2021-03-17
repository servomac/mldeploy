import enum
import typing

from sqlalchemy import Column, Enum, Integer, String, Text

from mldeploy.db import Base


class TrainingLibrariesEnum(enum.Enum):
    SKLEARN = 'SKLEARN'
    TENSORFLOW = 'TENSORFLOW'

    def __str__(self):
        return self.name


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    training_library = Column(Enum(TrainingLibrariesEnum), nullable=False)
    serialized_model_path = Column(String(512), nullable=False)

    def __init__(self, name, description, training_library, serialized_model_path):
        self.name = name
        self.description = description
        self.training_library = training_library
        self.serialized_model_path = serialized_model_path

    @classmethod
    def from_dict(cls, data: typing.Dict):
        return Model(
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
