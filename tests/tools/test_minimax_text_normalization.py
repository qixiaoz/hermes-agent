import sys
from types import SimpleNamespace

from tools.tts_tool import _minimax_text_to_simplified


def test_minimax_text_to_simplified_uses_opencc(monkeypatch):
    class FakeOpenCC:
        def __init__(self, mode):
            assert mode == "t2s"

        def convert(self, text):
            assert text == "繁體中文"
            return "繁体中文"

    monkeypatch.setitem(sys.modules, "opencc", SimpleNamespace(OpenCC=FakeOpenCC))
    assert _minimax_text_to_simplified("繁體中文", {}) == "繁体中文"


def test_minimax_text_to_simplified_can_be_disabled(monkeypatch):
    monkeypatch.setitem(sys.modules, "opencc", None)
    assert (
        _minimax_text_to_simplified(
            "繁體中文", {"convert_to_simplified": False}
        )
        == "繁體中文"
    )
