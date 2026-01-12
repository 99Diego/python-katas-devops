from fastapi import FastAPI
from app.domain.dictionary import Dictionary
from app.domain.shopping import get_total
from app.domain.words import nth_char

app = FastAPI(
    title="Python Katas DevOps API",
    version="1.0.0"
)

dictionary = Dictionary()
dictionary.newentry("Apple", "A fruit that grows on trees")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dictionary/{word}")
def dictionary_lookup(word: str):
    return {
        "word": word,
        "definition": dictionary.look(word)
    }


@app.post("/shopping")
def shopping(items: list[str]):
    costs = {
        "socks": 5,
        "shoes": 60,
        "sweater": 30
    }
    total = get_total(costs, items, 0.09)
    return {"items": items, "total": total}


@app.post("/words")
def words(words: list[str]):
    return {"result": nth_char(words)}
