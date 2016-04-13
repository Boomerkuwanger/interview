from json import loads
from sys import exit


class ProductionClass(object):
    SUB_STRINGS = frozenset(['add', 'sub'])

    def __init__(self, foo):
        self.foo = foo
        self.is_valid = None

    def validate_foo(self):
        valid_types = [str, unicode]
        type_foo = type(self.foo)
        if type_foo not in valid_types:
            raise AttributeError('self.foo type must be one of type {0} - got {1}'.format(
                valid_types, type_foo))

        self.is_valid = any([sub_string in self.foo for sub_string in ProductionClass.SUB_STRINGS])
        return self.is_valid

    def do_work(self):
        if self.is_valid is None:
            raise AssertionError('You must run validate_foo before calling do_work')
        elif self.is_valid:
            return loads(self.foo)
        else:
            return {}

    def halt(self, exit_code=0):
        exit(exit_code)
