import time

def brute_force_attack(password_list, target_password):

    print("Starting brute-force simulation")
    attempts = 0

    for guess in password_list:
        attempts += 1
        print(f"Trying password: {guess}")

        if guess == target_password:
            print("Password found!")
            print(f"Target password: {guess}")
            print(f"Total attempts: {attempts}")
            return guess

    print("Password not found in the list.")
    return None


if __name__ == "__main__":
    possible_passwords = [
        "123456",
        "password",
        "admin",
        "letmein",
        "welcome",
        "qwerty",
        "abc123",
        "hello",
        "monkey",
        "dragon"
    ]

    target = "welcome"

    brute_force_attack(possible_passwords, target)