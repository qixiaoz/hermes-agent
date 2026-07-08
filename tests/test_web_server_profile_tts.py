"""Tests for profile-aware desktop TTS endpoint.

These tests exercise the helper functions in ``hermes_cli.web_server`` that
scope a single ``/api/audio/speak`` request to a requested Hermes profile's
``HERMES_HOME``. They never reach the real MiniMax / ElevenLabs providers --
they only verify home resolution and the request-local override semantics in
``hermes_constants``.
"""

from pathlib import Path

from hermes_constants import (
    get_hermes_home,
    reset_hermes_home_override,
    set_hermes_home_override,
)
from hermes_cli import web_server


def test_clean_audio_profile_rejects_default_empty_and_pathy_values():
    assert web_server._clean_audio_profile(None) is None
    assert web_server._clean_audio_profile("") is None
    assert web_server._clean_audio_profile(" default ") is None
    assert web_server._clean_audio_profile("../nahida") is None
    assert web_server._clean_audio_profile("nahida/slash") is None
    assert web_server._clean_audio_profile("nahida\\slash") is None


def test_clean_audio_profile_accepts_normal_profile_names():
    assert web_server._clean_audio_profile("nahida") == "nahida"
    assert web_server._clean_audio_profile("silver-wolf_01") == "silver-wolf_01"


def test_profile_tts_home_resolves_existing_profile_under_default_root(tmp_path):
    root = tmp_path / ".hermes"
    profile = root / "profiles" / "nahida"
    profile.mkdir(parents=True)
    token = set_hermes_home_override(root)
    try:
        assert web_server._profile_tts_home("nahida") == profile
    finally:
        reset_hermes_home_override(token)


def test_profile_tts_home_returns_none_for_missing_or_default(tmp_path):
    root = tmp_path / ".hermes"
    (root / "profiles").mkdir(parents=True)
    token = set_hermes_home_override(root)
    try:
        assert web_server._profile_tts_home(None) is None
        assert web_server._profile_tts_home("default") is None
        assert web_server._profile_tts_home("ghost") is None
    finally:
        reset_hermes_home_override(token)


def test_hermes_home_override_is_context_local_and_resettable(tmp_path):
    root = tmp_path / ".hermes"
    profile = root / "profiles" / "nahida"
    profile.mkdir(parents=True)
    outer = set_hermes_home_override(root)
    try:
        assert get_hermes_home() == root
        inner = set_hermes_home_override(profile)
        try:
            assert get_hermes_home() == profile
        finally:
            reset_hermes_home_override(inner)
        assert get_hermes_home() == root
    finally:
        reset_hermes_home_override(outer)
