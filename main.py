import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_set = ''

    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character types selected for password generation")

    password = ''.join(random.choice(character_set) for _ in range(length))

    return password

def get_password_length(password_type):
    if password_type == 'strong':
        return random.randint(12, 16)
    elif password_type == 'medium':
        return random.randint(8, 11)
    elif password_type == 'weak':
        return random.randint(5, 7)
    else:
        raise ValueError("Invalid password type selected")

def main():
    print("Welcome to the Password Generator!")

    try:
        password_type = input("Select password type (strong/medium/weak): ").lower()
        length = get_password_length(password_type)

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
