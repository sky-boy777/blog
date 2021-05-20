from django.test import TestCase

# Create your tests here.

class A():
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    pass
    # def __init__(self):
    #     print("C")

class E:
    def __init__(self):
        print('E')

class D(B,C,E):
    pass

print(D.__mro__)
D()
