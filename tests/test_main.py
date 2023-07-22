from sample import main


def test_main() -> None:
    actual = main.calc(1, 1)

    assert actual == 2
