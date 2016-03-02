pylint-peewee Changelog
=======================

Here you can see the full list of changes between each pylint-peewee release.

Version 0.2
-----------

- Moved plugin to it's own installation directory of: ``pylint_peewee``, this 
  means this IS a backwards incompatible upgrade and you need to update your
  .pylintrc to load the plugin: ``pylint_peewee`` and not ``pylint-peewee``.
- Mocked out the ``id`` member variable that is added automatically.
- Mocked out ``create`` method.
- Made mocks more realistic. They are now methods that return the expected
  objects, instead of just mocking to the objects.
- Added this Changelog.

Version 0.1
-----------

- Initial plugin release. Mocks all common query operations and data 
  manipulation operations.
