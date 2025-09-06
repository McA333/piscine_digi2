from operations import basic_ops, advanced_ops

def do_op (a, char, b) :
    
    match char:
        case '+':
            print(basic_ops.add(a, b))
        case '-':
            print(basic_ops.subtract(a, b))
        case '*':
            print(advanced_ops.multiply(a, b))
        case '/':
            print(advanced_ops.safe_divide(a, b))

do_op(input("Entrer le premier chiffre : "), input("Entrer le caractère : "), input("Entrer le deuxième chiffre : "))