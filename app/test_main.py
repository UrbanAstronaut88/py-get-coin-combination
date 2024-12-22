from app.main import get_coin_combination


def test_basic_case() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0], "It was expected [1, 0, 0, 0] for 1 cent"
