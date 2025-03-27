from spellchecker import SpellChecker

spell = SpellChecker()
print(spell.correction("speling"))  # Should print: "spelling"

import random
from collections import defaultdict
from spellchecker import SpellChecker

class AutocorrectKeyboard:
    def __init__(self, corpus):
        self.spell = SpellChecker()
        self.n_grams = defaultdict(list)
        self.build_ngram_model(corpus)
    
    def build_ngram_model(self, corpus, n=2):
        """
        Builds an n-gram model (default: bigram) using a given corpus.
        """
        for sentence in corpus:
            words = sentence.lower().split()
            for i in range(len(words) - 1):
                self.n_grams[words[i]].append(words[i + 1])

    def correct_spelling(self, text):
        """
        Identifies and corrects misspelled words in the given text.
        """
        words = text.split()
        corrected_words = []
        for word in words:
            if word in self.spell:  # If the word is correctly spelled
                corrected_words.append(word)
            else:
                corrected_word = self.spell.correction(word)
                corrected_words.append(corrected_word if corrected_word else word)
        return " ".join(corrected_words)

    def predict_next_word(self, previous_word):
        """
        Predicts the next word based on an n-gram model.
        """
        previous_word = previous_word.lower()
        if previous_word in self.n_grams:
            return random.choice(self.n_grams[previous_word])  # Randomly select a suggestion
        else:
            return None  # No suggestion available

    def process_text(self, text):
        """
        Runs both spell correction and word prediction on the input text.
        """
        corrected_text = self.correct_spelling(text)
        last_word = corrected_text.split()[-1] if corrected_text else ""
        next_word_prediction = self.predict_next_word(last_word) if last_word else None
        
        return corrected_text, next_word_prediction

# Example corpus for training the n-gram model (should be larger in real use cases)
corpus = [
    "hello how are you",
    "how are you doing",
    "you are great",
    "hello there",
    "good morning",
    "good afternoon",
    "good evening",
    "have a nice day",
    "have a great time",
    "what are you doing",
    "i am going home",
    "i am feeling happy",
    "i am feeling sad",
    "i am really excited",
    "i am very tired",
    "do you like coffee",
    "do you like tea",
    "do you want to play",
    "do you want to eat",
    "where are you going",
    "where do you live",
    "what do you mean",
    "what do you think",
    "can you help me",
    "can you tell me",
    "thank you so much",
    "thank you for coming",
    "see you later",
    "see you soon",
    "nice to meet you",
    "how was your day",
    "i love programming",
    "i love python",
    "i love to travel",
    "learning is fun",
    "practice makes perfect",
    "never give up",
    "believe in yourself",
]

# Initialize the autocorrect keyboard system
keyboard = AutocorrectKeyboard(corpus)

# Interactive user input loop
while True:
    user_input = input("\nType a sentence (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break

    corrected_text, predicted_next_word = keyboard.process_text(user_input)

    print(f"\nCorrected Text: {corrected_text}")
    if predicted_next_word:
        print(f"Suggested Next Word: {predicted_next_word}")
    else:
        print("No word prediction available.")