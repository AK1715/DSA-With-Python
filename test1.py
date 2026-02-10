class Test:
    x =5
    def __init__(self):
        self.a = 5
        self.b = 6

    def f1(self):
        pass

    @staticmethod
    def f2():
        print("Hello")
    
    @classmethod
    def f3(cls):
        print(cls.x)

t1 = Test()
t2 = Test()
print(t1.a,t1.b)
print(t2.a,t2.b)
Test.f2()
Test.f3()
