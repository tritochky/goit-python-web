import json
import pickle
from abc import abstractmethod, ABC


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class ListJsonSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "w") as fh:
            json.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            unpacked = json.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked
        

class DictJsonSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "w") as fh:
            json.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            unpacked = json.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class TupleJsonSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "w") as fh:
            json.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            unpacked = tuple(json.load(fh))
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class SetJsonSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        self.data = list(self.data)
        with open(self.file_name, "w") as fh:
            json.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            unpacked = set(json.load(fh))
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class ListPicklSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class DictPicklSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class TuplePicklSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked


class SetPicklSerialization(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = ''

    def serialize(self):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)
            return 'Done!'

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            assert self.data == unpacked, 'Wrong deserialization!'
            return unpacked
