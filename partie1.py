def multiply(a, b) :
    
    a = int(a)
    b = int(b)
    result = a * b
    print (result)

def compare(a, b) :
    
    a = int(a)
    b = int(b)

    if (a == b) :
        print("Les deux nombres sont egaux\0")
    if (a > b) :
        print("Le premier nombre est plus grand que le second\0")
    if (a < b) :
        print("Le premier nombre est plus petit que le second\0")

def counting(x) :
    
    x = int(x)

    for n in range(1, x, 2) :
        print(n, end= ', ')

def ask_user() :

    word = str(input())

    while not word  == "exit":
        print ("Vous avez entre : ", word)
        word = str(input())

def safe_divide(a, b) :

    try :
        a = float(a)
        b = float(b)
        res = a / b
        print (res)
    except (ZeroDivisionError, ValueError) :
        print("Impossible de diviser par zero")
        print("None")
        return None

def display_square(size, char) :

    for _ in range(size) :
        print (char * size)




#multiply(input("Entrer le premier nombre: "), input("Entrer le deuxieme nombre: "))
#compare(input("Entrer le premier nombre: "), input("Entrer le deuxeme nombre: "))
#counting(input("Stop : "))
#ask_user()
#safe_divide(input(), input())
#display_square(int(input("Entrer la taille du carré : ")), input("Entrer le caractere : "))