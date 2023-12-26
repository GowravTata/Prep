class LimitedInstances:
    instance_count = 0
    limit = 3

    def __repr__(cls):
        return f"Instance {cls.instance_count} is created"

    def __new__(cls, *args, **kwargs):
        if cls.instance_count >= cls.limit:
            raise ValueError(f"Only {cls.limit} instances are allowed")
        cls.instance_count += 1
        return super(LimitedInstances, cls).__new__(cls)

    def __del__(self):
        type(self).instance_count -= 1


try:
    obj1 = LimitedInstances()
    obj2 = LimitedInstances()
    obj3 = LimitedInstances()
    obj4 = LimitedInstances()
except ValueError as e:
    print(e)
