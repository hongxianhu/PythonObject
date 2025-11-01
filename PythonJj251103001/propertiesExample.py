class ClassWithProperties:
    def __init__(self, someParameter):
        self._someAttribut=someParameter
    
    @property
    def someAttribut(self):
        return self._someAttribut
    
    @someAttribut.setter
    def someAttribut(self,value):
        self._someAttribut=value

    @someAttribut.deleter
    def someAttribut(self):
        del self._someAttribut

obj = ClassWithProperties('some initial value')
print(obj.someAttribut)
obj.someAttribut = 'changed value'
print(obj.someAttribut)
del obj.someAttribut