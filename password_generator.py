import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "⚠️ Weak"

    elif score <= 4:
        return "🟡 Medium"

    else:
        return "🟢 Strong"


def password_generator():
    while True:
        print("\n" + "=" * 55)
        print("             🔐 SMART PASSWORD GENERATOR")
        print("=" * 55)

        print("1. 🔑 Generate Password")
        print("2. 🚪 Exit")

        print("=" * 55)

        choice = input("Enter your choice: ").strip()

        if choice == "2":
            print("\n👋 Thank you for using Password Generator!")
            break

        if choice != "1":
            print("\n❌ Invalid choice. Please select 1 or 2.")
            continue

        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("❌ Password length should be at least 4.")
                continue

            password = generate_password(length)
            strength = check_strength(password)

            print("\n" + "-" * 55)
            print("🔐 Generated Password:")
            print(password)
            print(f"\n🛡️ Strength: {strength}")
            print("-" * 55)

        except ValueError:
            print("\n❌ Please enter a valid number.")


password_generator()