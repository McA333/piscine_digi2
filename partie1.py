def multiply() :
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a * b
    print (result)

def compare() :
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if (a == b) :
        print("Les deux nombres sont egaux\0")
    if (a > b) :
        print("Le premier nombre est plus grand que le second\0")
    if (a < b) :
        print("Le premier nombre est plus petit que le second\0")

def counting() :
    
    x = range(1, int(input("Stop : ")), 2)

    for n in x :
        print(n, end= ', ')

def ask_user() :

    word = str(input())

    while not word  == "exit":
        print ("Vous avez entre : ", word)
        word = str(input())

def safe_divide() :


    try :
        a = float(input())
        b = float(input())
        res = a / b
        print (res)
    except (ZeroDivisionError, ValueError) :
        print("Impossible de diviser par zero")
        print("None")
        return None

def display_square(size, char) :

    for n in range(size) :
        print (char * size)




#multiply()
#compare()
#counting()
#ask_user()
#safe_divide()
#display_square(int(input("Enter size : ")), input("Enter char : "))