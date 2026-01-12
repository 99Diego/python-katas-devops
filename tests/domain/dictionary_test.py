from app.domain.dictionary import Dictionary


def test_dictionary_lookup_existing_word():
    d = Dictionary()
    d.newentry("Apple", "A fruit")
    assert d.look("Apple") == "A fruit"


def test_dictionary_lookup_missing_word():
    d = Dictionary()
    assert d.look("Banana") == "Can't find entry for Banana"
