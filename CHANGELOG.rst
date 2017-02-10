Changelog
=========

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
