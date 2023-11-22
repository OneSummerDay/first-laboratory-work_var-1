def sort_characters_in_words(s):
    words = s.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    result_string = ' '.join(sorted_words)
    return result_string


input_string = input("Введіть рядок: ")

result = sort_characters_in_words(input_string.lower())
print("Результат:", result)
