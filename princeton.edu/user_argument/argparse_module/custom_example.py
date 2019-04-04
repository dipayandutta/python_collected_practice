import argparse

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("message",help="display the string",type=str)
    parser.add_argument("number",help="display the number integer",type=int)

    argument = parser.parse_args()

    print(argument.message)
    print(argument.number)


if __name__ == '__main__':
    main()
