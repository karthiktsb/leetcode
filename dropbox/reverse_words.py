
def reverse_words(s: str):
    l = s.split(" ")
    result = []

    for i in range(len(l) - 1, -1, -1):
        word = l.pop(0)
        result.insert(0, word)

    return " ".join(result)


if __name__ == "__main__":
    print(reverse_words("I am currently at my home"))
