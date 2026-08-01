"""Pure engine package. Front ends should enter through :mod:`session`."""

from .session import act, describe, new_game

__all__ = ["act", "describe", "new_game"]

