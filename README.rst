===========
selectors34
===========

*selectors34* is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-François Natali. This port is based on
Victor Stinner's ``trollius/selectors.py`` port.

Installation and Usage
----------------------

To install *selectors34* via pip::

    $ pip install selectors34

For best compatibility for Python 3.4, import *selectors34* like::

    try:
        import selectors
    except ImportError:
        import selectors34 as selectors

Project Details
---------------

:Documentation: https://docs.python.org/3/library/selectors.html
:PyPI: https://pypi.python.org/pypi/selectors34
:Issue tracker: https://bugs.python.org/ (upstream)
:Issue tracker: https://github.com/berkerpeksag/selectors34/issues
:Supported versions: Python 2.6, 2.7 and 3.3
:License: Python Software Foundation License
:Build status:
    .. image:: https://travis-ci.org/berkerpeksag/selectors34.svg?branch=master
        :target: https://travis-ci.org/berkerpeksag/selectors34

Release management
------------------

#. Bump version number in ``setup.py``
#. Update ``CHANGELOG.rst``
#. Run tests via ``tox``
#. Install requirements to make a release: ``pip install -r requirements-dev.txt``
#. Make a new release on the PyPI test server: ``make test-release``
#. Create a tag: ``git tag X.Y.X``
#. Make the actual release: ``make release``
