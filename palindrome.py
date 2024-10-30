def is_palindrome(word):
    word=word.lower()
    return word==word[::-1]
the_word=is_palindrome("Dad")
print(the_word)

