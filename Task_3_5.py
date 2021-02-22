from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(m, repeat=False):
    jokes = []
    for idx in range(0, m):
        if repeat and len(nouns) == 0:
            break
        word1 = choice(nouns)
        word2 = choice(adverbs)
        word3 = choice(adjectives)
        jokes.append(f"{word1} {word2} {word3}")
        if repeat:
            nouns.remove(word1)
            adverbs.remove(word2)
            adjectives.remove(word3)
    return jokes
print(get_jokes(5, True))
