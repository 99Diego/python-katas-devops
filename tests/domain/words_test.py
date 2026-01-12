from app.domain.words import nth_char


def test_nth_char():
    words = ["yoda", "best", "has"]
    assert nth_char(words) == "yes"


def test_nth_char_empty_list():
    assert nth_char([]) == ""
