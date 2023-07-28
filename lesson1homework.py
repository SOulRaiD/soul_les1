def check():
    if word_1 == word_2:
        return True
    else:
        return False


word_1 = input('введи слово для проверки низким регистром')
print(f'слово для проверки - {word_1}')
if word_1.islower():
    letters_list = tuple(word_1)
    print(letters_list)
    word_2 = ''.join(reversed(letters_list))
    print(word_2)
    check()
    print(check())
else:
    raise Exception('По русски написано "введи слово для проверки низким регистром"')
