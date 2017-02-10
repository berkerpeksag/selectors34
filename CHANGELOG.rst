Changelog
=========

1.2 (not released yet)
----------------------

* Pull request #3: ``wrap_error()`` compatibility layer for PEP 3151 has been
  removed.
  (Patch written by Victor Stinner.)
* Pull request #4: Fix ``TypeError`` when ``select.select()`` is monkeypatched
  by Gevent. Note that this is no longer an issue with the stdlib
  ``selectors`` module on Gevent 1.1 and later.
  (Patch written by Przemysław Węgrzyn.)


1.1 (released on 2015-07-15)
----------------------------

* Issues #23209, #23225: ``selectors.BaseSelector.get_key()`` now raises a
  ``RuntimeError`` if the selector is closed. And
  ``selectors.BaseSelector.close()`` now clears its internal reference to the
  selector mapping to break a reference cycle.
  (Initial patch written by Martin Richard and backported by Victor Stinner.)
* Issues #23209, #23225: ``selectors.BaseSelector.close()`` now clears its
  internal reference to the selector mapping to break a reference cycle.
  (Initial patch written by Martin Richard and backported by Victor Stinner.)
* Issue #23009: Make sure ``selectors.EpollSelector.select()`` works when no
  FD is registered.
  (Backported by Victor Stinner.)


1.0 (released on 2015-02-05)
----------------------------

* Initial release.
