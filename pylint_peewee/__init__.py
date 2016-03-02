from astroid import MANAGER
from astroid import scoped_nodes

from .mocks import DummySelect, DummyInsert, DummyDelete, DummyUpdate


def register(linter):
    pass


def transform(cls):
    if 'db.Model' in cls.basenames:
        overrides = {
            'select': DummySelect,
            'get': DummySelect,
            'insert': DummyInsert,
            'update': DummyUpdate,
            'delete': DummyDelete,
        }
        for key in overrides:
            cls.locals[key] = [overrides[key]()]


MANAGER.register_transform(scoped_nodes.Class, transform)
