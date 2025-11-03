class ClassWithBadProperty:
    def __init__(self):
        self.someAttribut='some initial value'
    
    @property
    def someAttribut(self):
        return self.someAttribut

    @someAttribut.setter
    def someAttribut(self,value):
        self._someAttribut=value

obj=ClassWithBadProperty()
print(obj.someAttribut)