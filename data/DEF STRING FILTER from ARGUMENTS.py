def alphabet_filter(word):
    s = word    
    word_consonants = s.translate({ord(i): None for i in 'aeiou'})
    word_vowels = s.translate({ord(i): None for i in 'qwrtypsdfghjklzxcvbnm'})
    print(word_consonants)
    print(word_vowels)
    return word_consonants, word_vowels
alphabet_filter('codecool')

