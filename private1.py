class MyClass:
    __privateVar = 27;
    def __privMeth(self):
     print("im inside class MyClass")
    def hello (self):
        print("Variable value:",MyClass.__priv)
foo = MyClass()
foo.hello()
foo.__privateMeth