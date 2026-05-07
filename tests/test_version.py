"""Smoke tests for TicketRouter."""

import ticket_router
from ticket_router import version
from ticket_router.version import __version__


def test_version_returns_hello_ticket() -> None:
    assert version() == "hello ticket"


def test_version_string_is_semver() -> None:
    parts = __version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_top_level_import() -> None:
    assert hasattr(ticket_router, "version")
