def multiply(a, b) :
    
    a = int(a)
    b = int(b)
    result = a * b
    print (result)

def safe_divide(a, b) :

    try :
        a = float(a)
        b = float(b)
        res = a / b
        print (res)
    except (ZeroDivisionError, ValueError) :
        print("Impossible de diviser par zero")

        return None
    