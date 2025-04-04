def search_text(text: str, file: str):
    text = text.encode()

    with open(file, "rb") as f:
        buffer = bytearray(f.read(len(text)))

        while True:
            if buffer == text:
                return True

            next_byte = f.read(1)
            if not next_byte:
                return False

            buffer.pop(0)
            buffer.append(next_byte[0])

    return False


def main():
    print(search_text("ANZSIC06", "annual-enterprise-survey-2023-financial-year-provisional.csv"))
    print(search_text("ANZSIC06989", "annual-enterprise-survey-2023-financial-year-provisional.csv"))
    text = "abcdc"

    print(text.encode())


main()