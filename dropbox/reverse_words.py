
def reverse_words(s: str):
    l = s.split(" ")

    for i in range(len(l)):
        l.insert(0, l.pop(i))

    return " ".join(l)


if __name__ == "__main__":
    print(reverse_words("I am currently at my home"))
