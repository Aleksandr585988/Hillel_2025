# ЛИНЕЙНОЕ НАСЛЕДУВАНИЕ
#
# class Base:
#     def say(self):
#         print("I am from foo Base")
#
# class Child(Base):
#     def say(self):
#         super().say()                   #  наследуем от родительского класса. в складному наследовании звертается до
#                                         #  наступного а не до батькивского смотри ниже
#         # print("I am from Child")
#
# instance = Child()
# instance.say()
#
# instance1 = Base()
# instance1.say()

# СКЛАДНЕ НАСЛИДУВАННЯ

class A:
    def foo(self):
        print("I am from A")

class B(A):
    def foo(self):
        super().foo()

class C(A):
    def foo(self):
        print("I am from C")

class D(B, C):
    def foo(self):
        super().foo()

print(D.mro())
D().foo()

print(B.mro())
B().foo()

print(C.mro())
C().foo()