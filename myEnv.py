from flask import *
from icecream import ic 


def main():
    for i in range(0,100,3):
        ic( f"{i} is devisable by 3")



if __name__ == "__main__":
    main()