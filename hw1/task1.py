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
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.json'

    def serialize(self, data):
        with open(self.file_name, "w") as fh:
            json.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            return json.load(fh)
        

class DictJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.json'

    def serialize(self, data):
        with open(self.file_name, "w") as fh:
            json.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            return json.load(fh)


class TupleJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.json'

    def serialize(self, data):
        with open(self.file_name, "w") as fh:
            json.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            return tuple(json.load(fh))


class SetJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.json'

    def serialize(self, data):
        data = list(data)
        with open(self.file_name, "w") as fh:
            json.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "r") as fh:
            return set(json.load(fh))


class ListBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.bin'

    def serialize(self, data):
        with open(self.file_name, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            return pickle.load(fh)


class DictBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.bin'

    def serialize(self, data):
        with open(self.file_name, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            return pickle.load(fh)


class TupleBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.bin'

    def serialize(self, data):
        with open(self.file_name, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            return pickle.load(fh)


class SetBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data
        self.file_name = 'data.bin'

    def serialize(self, data):
        with open(self.file_name, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self):
        with open(self.file_name, "rb") as fh:
            return pickle.load(fh)


if __name__ == '__main__':
    data_list = [1, 2, 3]
    data_dict = {'one': 1, 'two': 2, 'three': 3}
    data_tuple = (1, 2, 3)
    data_set = {1, 2, 3}
    #file_json = 'data.json'
    #file_bin = 'data.bin'

    ListJsonSerialization().serialize(data_list)
    unpacked = ListJsonSerialization().deserialize()
    assert unpacked == data_list, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    DictJsonSerialization().serialize(data_dict)
    unpacked = DictJsonSerialization().deserialize()
    assert unpacked == data_dict, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    TupleJsonSerialization().serialize(data_tuple)
    unpacked = TupleJsonSerialization().deserialize()
    assert unpacked == data_tuple, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    SetJsonSerialization().serialize(data_set)
    unpacked = SetJsonSerialization().deserialize()
    assert unpacked == data_set, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    ListBinSerialization().serialize(data_list)
    unpacked = ListBinSerialization().deserialize()
    assert unpacked == data_list, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    DictBinSerialization().serialize(data_dict)
    unpacked = DictBinSerialization().deserialize()
    assert unpacked == data_dict, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    TupleBinSerialization().serialize(data_tuple)
    unpacked = TupleBinSerialization().deserialize()
    assert unpacked == data_tuple, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    SetBinSerialization().serialize(data_set)
    unpacked = SetBinSerialization().deserialize()
    assert unpacked == data_set, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')
