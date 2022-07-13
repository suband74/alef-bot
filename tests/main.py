import pytest
from pathlib import Path

from src.alef_bot.app import start_operation


@pytest.fixture
def data_dir() -> Path:
    """[Making the string with the full path to the file]"""
    test_data_dir = Path(__file__).resolve().parent
    return test_data_dir

@pytest.fixture
def sample_requests(requests_mock, data_dir:Path) -> None:
    """[Make "requests_mock"]"""
    data_dir = Path(__file__).resolve().parent
    with open(data_dir / "mock_file.html") as content:
        requests_mock.get(
            "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8"
,
            content=content.read().encode(),
        )
    return requests_mock

def test_start_operation(sample_requests):
    x = start_operation()
    print(x)
    assert x == (
        ['Апрелевка', 'Балашиха'], ["https://ru.wikipedia.org/wiki/%D0%90%D0%BF%D1%80%D0%B5%D0%BB%D0%B5%D0%B2%D0%BA%D0%B0", "https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0"], ['34309', '518260'])
            