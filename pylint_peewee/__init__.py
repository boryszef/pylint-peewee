from astroid import MANAGER, ClassDef
from astroid import scoped_nodes

from .mocks import (DummySelect, DummyInsert, DummyDelete, DummyUpdate,
                    DummyPrimaryKeyField)


def register(linter):
    pass


def _returns(ret_val):
    return lambda: ret_val

def get_base_classes(cls):
    module_names = (getattr(mod, 'value', None) for mod in cls.getattr('__module__'))
    class_names = (klass.name for klass in cls.mro())
    return tuple(zip(module_names, class_names))


def transform(cls):
    bases = get_base_classes(cls)
    if ('peewee', 'Model') in bases:
        overrides = {
            'select': _returns(DummySelect()),
            'get': _returns(DummySelect()),
            'insert': _returns(DummyInsert()),
            'update': _returns(DummyUpdate()),
            'delete': _returns(DummyDelete()),
            # @TODO: There has to be a better way to see if the id field is
            # missing or just not needed
            'id': DummyPrimaryKeyField(),
            'create': _returns(cls.instantiate_class()),
            'DoesNotExist': ClassDef('DoesNotExist', None),
        }
        for key in overrides:
            cls.locals[key] = [overrides[key]]


MANAGER.register_transform(scoped_nodes.ClassDef, transform)
