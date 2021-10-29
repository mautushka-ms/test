
import sys


def main():
    if len(sys.argv) > 2:
        print("Invalid number of arguments passed!")
        exit(2)
    a = sys.argv[1]
    b = sys.argv[2]
    print('B is ..', b)


if __name__ == '__main__':
    main()


