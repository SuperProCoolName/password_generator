import random
import string

def main():
    length = int(input('Enter the length of password: '))
    amount = int(input('Enter the amount of variants of password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    for i in range(amount):
        all = lower + upper + num + symbols
        temp = random.sample(all, length)
        
        password = ''.join(temp)
        print(password)

if __name__ == '__main__':
    main()