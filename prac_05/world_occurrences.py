text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
