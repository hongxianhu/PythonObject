class ClassWithRegularAttributs:
    def __init__(self, someParameter):
        self.someAttribut=someParameter

obj = ClassWithRegularAttributs('some initial value')
print(obj.someAttribut)
obj.someAttribut='changed value'
print(obj.someAttribut)
del obj.someAttribut