class Meta(type):
    def __new__(self, name, bases, attrs):
        attrs['class_number'] = self.children_number 
        self.children_number +=1
        return type.__new__(self, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
