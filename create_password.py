import string
import random

def paswrd_length():
    ln = int(input("Enter the length of the password: "))
    return ln

def create_paswrd(len):
    char1 = string.ascii_letters
    char2 = string.digits
    char3 = string.punctuation
    
    character = char1 + char2 + char3 
    print(character)
    paswrd = ''.join(random.choice(character) for i in range(len))
    return paswrd

def main():
    ln = paswrd_length()
    paswrd = create_paswrd(ln)
    print(f"Generated password: {paswrd}")
    
if __name__ == "__main__":
    main()
