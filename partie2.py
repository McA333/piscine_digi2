def concat_with_space(a, b) :

    first_word = str(a)
    second_word = str(b)
    result = first_word + ' ' + second_word + '\n'

    print(result)


def format_with_fstring(username, age) :

    username = str(username)
    age = str(age)

    result = f"Hello {username}, your are {age} years old!"
    print (result)


#concat_with_space(input("Entrer le premier mot :"), input("Entrer le deuxieme mot : "))
#format_with_fstring(input(), (input()))