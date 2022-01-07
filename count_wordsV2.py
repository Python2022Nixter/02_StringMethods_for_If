# en 0-122
# ru 1040-1279
# he 1424-1535

string = "My test string. Строка для теста для примера. מחרוזת מבחן בעברית"
# string - input("Enter statement")

en = list(range(65, 122))
ru = list(range(1040, 1103))
he = list(range(1424, 1535))

he_word_counter = 1 if ord(string[0]) in he else 0
en_word_counter = 1 if ord(string[0]) in en else 0
ru_word_counter = 1 if ord(string[0]) in ru else 0
# count words
for i in range(len(string)-1):
    if string[i] == " ":
        if ord(string[i+1]) in he:
            he_word_counter += 1
        elif ord(string[i+1]) in en:
            en_word_counter += 1
        elif ord(string[i+1]) in ru:
            ru_word_counter += 1


print(f"Word detected he: {he_word_counter }")
print(f"Word detected en: {en_word_counter }")
print(f"Word detected ru: {ru_word_counter }")
