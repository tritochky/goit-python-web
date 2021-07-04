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

    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed):
        return json.loads(packed)
        

class DictJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed):
        return json.loads(packed)


class TupleJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed):
        return tuple(json.loads(packed))


class SetJsonSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        #self.data = list(data)
        return json.dumps(list(data))

    def deserialize(self, packed):
        return set(json.loads(packed))


class ListBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed):
        return pickle.loads(packed)


class DictBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed):
        return pickle.loads(packed)


class TupleBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed):
        return pickle.loads(packed)


class SetBinSerialization(SerializationInterface):
    def __init__(self, data=None):
        self.data = data

    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed):
        return pickle.loads(packed)


if __name__ == '__main__':
    data_list = [1, 2, 3]
    data_dict = {'one': 1, 'two': 2, 'three': 3}
    data_tuple = (1, 2, 3)
    data_set = {1, 2, 3}
    #file_json = 'data.json'
    #file_bin = 'data.bin'

    packed = ListJsonSerialization().serialize(data_list)
    unpacked = ListJsonSerialization().deserialize(packed)
    assert unpacked == data_list, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    packed = DictJsonSerialization().serialize(data_dict)
    unpacked = DictJsonSerialization().deserialize(packed)
    assert unpacked == data_dict, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    packed = TupleJsonSerialization().serialize(data_tuple)
    unpacked = TupleJsonSerialization().deserialize(packed)
    assert unpacked == data_tuple, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    packed = SetJsonSerialization().serialize(data_set)
    unpacked = SetJsonSerialization().deserialize(packed)
    assert unpacked == data_set, 'Wrong deserialization!'
    print(f'Format JSON: {unpacked}')

    packed = ListBinSerialization().serialize(data_list)
    unpacked = ListBinSerialization().deserialize(packed)
    assert unpacked == data_list, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    packed = DictBinSerialization().serialize(data_dict)
    unpacked = DictBinSerialization().deserialize(packed)
    assert unpacked == data_dict, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    packed = TupleBinSerialization().serialize(data_tuple)
    unpacked = TupleBinSerialization().deserialize(packed)
    assert unpacked == data_tuple, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

    packed = SetBinSerialization().serialize(data_set)
    unpacked = SetBinSerialization().deserialize(packed)
    assert unpacked == data_set, 'Wrong deserialization!'
    print(f'Format BIN: {unpacked}')

