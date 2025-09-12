import sys

def list_discovery() -> list:

    list = [sys.argv[5], sys.argv[4], sys.argv[3], sys.argv[2], sys.argv[6]]
    print("Numbers has {x} elements and the sum of them all is {somme}.\n",list)

list_discovery()