import sys

import six

PY33 = (sys.version_info >= (3, 3))


def _wrap_error(exc, mapping, key):
    if key not in mapping:
        return
    new_err_cls = mapping[key]
    new_err = new_err_cls(*exc.args)

    # raise a new exception with the original traceback
    if hasattr(exc, '__traceback__'):
        traceback = exc.__traceback__
    else:
        traceback = sys.exc_info()[2]
    six.reraise(new_err_cls, new_err, traceback)


if PY33:
    import builtins

    BlockingIOError = builtins.BlockingIOError
    BrokenPipeError = builtins.BrokenPipeError
    ChildProcessError = builtins.ChildProcessError
    ConnectionRefusedError = builtins.ConnectionRefusedError
    ConnectionResetError = builtins.ConnectionResetError
    InterruptedError = builtins.InterruptedError
    ConnectionAbortedError = builtins.ConnectionAbortedError
    PermissionError = builtins.PermissionError
    FileNotFoundError = builtins.FileNotFoundError
    ProcessLookupError = builtins.ProcessLookupError

    def wrap_error(func, *args, **kw):
        return func(*args, **kw)
else:
    import errno
    import select
    import socket

    class BlockingIOError(OSError):
        pass

    class BrokenPipeError(OSError):
        pass

    class ChildProcessError(OSError):
        pass

    class ConnectionRefusedError(OSError):
        pass

    class InterruptedError(OSError):
        pass

    class ConnectionResetError(OSError):
        pass

    class ConnectionAbortedError(OSError):
        pass

    class PermissionError(OSError):
        pass

    class FileNotFoundError(OSError):
        pass

    class ProcessLookupError(OSError):
        pass

    _MAP_ERRNO = {
        errno.EACCES: PermissionError,
        errno.EAGAIN: BlockingIOError,
        errno.EALREADY: BlockingIOError,
        errno.ECHILD: ChildProcessError,
        errno.ECONNABORTED: ConnectionAbortedError,
        errno.ECONNREFUSED: ConnectionRefusedError,
        errno.ECONNRESET: ConnectionResetError,
        errno.EINPROGRESS: BlockingIOError,
        errno.EINTR: InterruptedError,
        errno.ENOENT: FileNotFoundError,
        errno.EPERM: PermissionError,
        errno.EPIPE: BrokenPipeError,
        errno.ESHUTDOWN: BrokenPipeError,
        errno.EWOULDBLOCK: BlockingIOError,
        errno.ESRCH: ProcessLookupError,
    }

    def wrap_error(func, *args, **kw):
        """
        Wrap socket.error, IOError, OSError, select.error to raise new specialized
        exceptions of Python 3.3 like InterruptedError (PEP 3151).
        """
        try:
            return func(*args, **kw)
        except (socket.error, IOError, OSError) as exc:
            if hasattr(exc, 'winerror'):
                _wrap_error(exc, _MAP_ERRNO, exc.winerror)
                # _MAP_ERRNO does not contain all Windows errors.
                # For some errors like "file not found", exc.errno should
                # be used (ex: ENOENT).
            _wrap_error(exc, _MAP_ERRNO, exc.errno)
            raise
        except select.error as exc:
            if exc.args:
                _wrap_error(exc, _MAP_ERRNO, exc.args[0])
            raise
