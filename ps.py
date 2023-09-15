def vowel_count(word):
    vowels = "AEIOUaeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Enter a word: ")
count = vowel_count(word)
print(f"The number of vowels in '{word}' is {count}.")
