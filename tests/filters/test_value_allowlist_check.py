import pytest

from credsweeper.filters import ValueAllowlistCheck
from tests.test_utils.dummy_line_data import get_line_data


class TestValueAllowlistCheck:
    def test_value_allowlist_check_p(self, file_path: pytest.fixture, success_line: pytest.fixture) -> None:
        line_data = get_line_data(file_path, line=success_line, pattern=r"(?P<value>.*$)")
        assert ValueAllowlistCheck().run(line_data) is False

    @pytest.mark.parametrize("line", [
        "ENC(Crackle123)",
    ])
    def test_value_allowlist_check_n(self, file_path: pytest.fixture, line: str) -> None:
        line_data = get_line_data(file_path, line=line, pattern=r"(?P<value>.*$)")
        assert ValueAllowlistCheck().run(line_data) is True

    def test_value_allowlist_check_none_value_n(self, file_path: pytest.fixture, success_line: pytest.fixture) -> None:
        line_data = get_line_data(file_path, line=success_line)
        assert ValueAllowlistCheck().run(line_data) is True
