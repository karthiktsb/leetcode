class MyClass:
    class_count = 0

    def __init__(self):
        MyClass.class_count += 1
        self.instance_count = MyClass.class_count

    def get_instance_count(self):
        return self.instance_count

    def print(self):
        print(MyClass.class_count)
        return

    @classmethod
    def get_class_count(cls):
        return cls.class_count


if __name__ == '__main__':
    cls1 = MyClass()
    cls2 = MyClass()
    cls3 = MyClass()

    print(cls1.get_instance_count())
    print(cls2.get_instance_count())
    print(cls3.get_instance_count())
    cls1.print()
    print(MyClass.get_class_count())