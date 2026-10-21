"""The intern's model client. It now lives in ``dclabai.models.client`` (shared with the model gateway); this name
is kept so the intern and anything that imported ``dclabai.intern.llm`` keep working unchanged."""

from ..models.client import DEFAULT_MODEL, PAUSE_SECONDS, ChatClient, failure, resume, settings  # noqa: F401
