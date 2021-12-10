#Создайте программу, которая проверяет, является ли палиндромом введённая фраза.

word = "abccba"
word = word.lower()


def palindrom(word):
    if len(word) == 1 or len(word) == 0:
        return 0
    if word[0] == word[-1]:
        print(word[0], word[-1])
        return palindrom(word[1:-1])
    else:
       return 1

test = palindrom(word)
if test == 0:
    print("Yes")
elif test == 1:
    print("No")