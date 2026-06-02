from markov import MarkovChain

def get_text():
    print("\n==============================")
    print(" MARKOV TEXT GENERATOR ")
    print("==============================\n")

    choice = input("(1) Sample text\n(2) Your own text\nChoose: ")

    if choice == "1":
        with open("sample.txt", "r", encoding="utf-8") as f:
            return f.read()

    elif choice == "2":
        print("\nPaste your text:")
        return input()

    else:
        print("Invalid choice → using sample text")
        with open("sample.txt", "r", encoding="utf-8") as f:
            return f.read()


def main():
    text = get_text()

    mc = MarkovChain()

    # train both models
    mc.train_words(text)
    mc.train_chars(text)

    print("\nChoose Model:")
    print("1. Word-based")
    print("2. Character-based")
    print("3. Hybrid (Recommended)")

    choice = input("\nEnter choice: ")

    print("\nGenerating...\n")

    if choice == "1":
        length = int(input("How many words? "))
        start = input("Starting word (optional): ")
        output = mc.generate_words(length, start)

    elif choice == "2":
        length = int(input("How many characters? "))
        output = mc.generate_chars(length)

    else:
        w_len = int(input("Word output length: "))
        c_len = int(input("Character output length: "))
        output = mc.generate_hybrid(w_len, c_len)

    print("\n------ OUTPUT ------\n")
    print(output)
    print("\n--------------------\n")


if __name__ == "__main__":
    main()