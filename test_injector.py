from injector import inject, Injector


# # 普通调用
# class A():
#    name: str = "A Class"
#
#
# class B():
#     def __init__(self, a: A):
#         self.a = a
#
#     def print_name(self):
#         print(self.a.name)
#
# a = A()
# b = B(a)
# b.print_name()

# 使用injector
class A:
    name: str = "A Class"

@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print_name(self):
        print(self.a.name)

injector = Injector()
b = injector.get(B)
b.print_name()