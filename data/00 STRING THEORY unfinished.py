print('PALINDROM')
def is_palindrome(text):

    #is_palindrome('Mr. Owl ate my metal worm')
    #is_palindrome('Eva, can I see bees in a cave?')

    text_copy = text.lower().replace(' ','')
    text_copy_2 = text_copy

    for sign in text_copy_2:
        if not sign.isalnum():
            text_copy = text.copy.replace(sign, '')

    reversed_text = text_copy[::-1]
    return text_copy == reversed_text

print(is_palindrome('blablablablablablabla'))
    

print('ISOGRAM')
def is_isogram(text):  # powtarzajace sie litery
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    text_list = list(text)
    text_set = set(text)

    return len(text_list) == len(text_set)

print(is_isogram('blablabla'))

print('PANGRAM do poprawy')
def is_pangram(text):  # uzyte wszystkie litery alfabetu
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    alphabet = string.ascii_lowercase
    text_lower = text.lower()

    for letter in alphabet:
        if letter not in text_lower:
            return False
    return True

print(is_pangram('blablablablabla'))


print('ANAGRAM')  # podmiana kolejnosci liter
def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    text1_copy = text1.lower().replace(' ','')
    text2_copy = text2.lower().replace(' ','')
    
    text_copy_2 = text1_copy

    for sign in text_copy_2:
        if not sign.isalnum():
            text1_copy = text1_copy.replace(sign, '')

    text_copy_2 = text2_copy

    for sign in text_copy_2:
        if not sign.isalnum():
            text2_copy = text1_copy.replace(sign, '')

    sorted_text1 = sorted(text1_copy)
    sorted_text2 = sorted(text2_copy)

    return sorted_text1 == sorted_text2


print('BLANAGRAM')
def is_blanagram(text1, text2):  # anagram z 1 znakiem odmiennym od pierwotnego wyrazenia
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
