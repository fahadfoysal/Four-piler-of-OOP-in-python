class A:
    def method(self):
        print("This method belongs to Class A")

class B(A):
    def method(self):
        print("This method belongs to Class B")

class C(A):
    def method(self):
        print("This method belongs to Class C")

class D(B, C):
    pass

d = D()
d.method()