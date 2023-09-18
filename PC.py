def is_palindrome(input_str):
    clean_str = ''.join(input_str.split()).lower()
    length = len(clean_str)
    i = 0
    while i < length // 2:
        if clean_str[i] != clean_str[length - i - 1]:
            return False
        i += 1
    return True

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
