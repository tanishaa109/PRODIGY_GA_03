import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.word_model = defaultdict(list)
        self.char_model = defaultdict(list)

    # ---------------- WORD MODEL ----------------
    def train_words(self, text):
        words = text.replace("\n", " ").split()

        for i in range(len(words) - 1):
            self.word_model[words[i]].append(words[i + 1])

    def generate_words(self, length=20, start_word=None):
        if not self.word_model:
            return "Word model not trained!"

        if start_word in self.word_model:
            word = start_word
        else:
            word = random.choice(list(self.word_model.keys()))

        result = [word]

        for _ in range(length - 1):
            if word not in self.word_model:
                break
            word = random.choice(self.word_model[word])
            result.append(word)

        return " ".join(result)

    # ---------------- CHAR MODEL (IMPROVED) ----------------
    def train_chars(self, text):
        text = text.replace("\n", " ")
        chars = list(text)

        for i in range(len(chars) - 1):
            self.char_model[chars[i]].append(chars[i + 1])

    def generate_chars(self, length=200, start_char=None):
        if not self.char_model:
            return "Char model not trained!"

        if start_char and start_char in self.char_model:
            char = start_char
        else:
            char = random.choice([c for c in self.char_model.keys() if c.isalpha()])

        result = [char]

        for _ in range(length - 1):
            if char not in self.char_model:
                break
            char = random.choice(self.char_model[char])
            result.append(char)

        text = "".join(result)

        # cleanup
        text = " ".join(text.split())

        if text:
            text = text[0].upper() + text[1:]

        return text

    # ---------------- HYBRID ----------------
    def generate_hybrid(self, word_length=20, char_length=200):
        word_output = self.generate_words(word_length)
        char_output = self.generate_chars(char_length)

        return f"""--- WORD OUTPUT ---
{word_output}

--- CHAR OUTPUT ---
{char_output}
"""