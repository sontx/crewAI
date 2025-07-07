import threading
import contextvars
import uuid


class ExecutionContext:
  _instance = None
  _lock = threading.Lock()

  def __new__(cls):
    if not cls._instance:
      with cls._lock:
        if not cls._instance:
          cls._instance = super().__new__(cls)
          cls._instance._init()
    return cls._instance

  def _init(self):
    self._thread_local = threading.local()
    self._async_context_id = contextvars.ContextVar('execution_context_id')

  def get(self) -> str:
    """
    Get the current context ID.
    Falls back to thread-local if async context is not available.
    """
    try:
      return self._async_context_id.get()
    except LookupError:
      return getattr(self._thread_local, 'context_id', None)

  def init(self, ctx_id: str = None) -> str:
    """
    Initialize a new context ID if none is provided.
    Useful to start a new context or carry one from a parent.
    """
    ctx_id = ctx_id or str(uuid.uuid4())
    self._async_context_id.set(ctx_id)
    self._thread_local.context_id = ctx_id
    return ctx_id

execution_context = ExecutionContext()
