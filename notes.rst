Release management
------------------

#. Bump version number in ``setup.py``
#. Update ``CHANGELOG.rst``
#. Run tests via ``tox``
#. Install requirements to make a release: ``pip install -r requirements-dev.txt``
#. Make a new release on the PyPI test server: ``make test-release``
#. Create a tag: ``git tag X.Y.X``
#. Make the actual release: ``make release``
