from math_utils import add, multiply, power, root

def main():
    print("Добре дошъл в мини калкулатора!")
    print("Избери операция:")
    print("1. Събиране")
    print("2. Умножение")
    print("3. Степенуване")
    print("4. Коренуване")
    
    choice = input("Въведи номера на операцията (1-4): ")

    a = float(input("Въведи първо число: "))
    b = float(input("Въведи второ число: "))

    if choice == "1":
        result = add(a, b)
        print(f"{a} + {b} = {result}")

    elif choice == "2":
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")

    elif choice == "3":
        result = power(a, b)
        print(f"{a} ^ {b} = {result}")

    elif choice == "4":
        result = root(a, b)
        print(f"{b}-ти корен от {a} = {result}")

    else:
        print("Невалиден избор! Опитай пак.")

if __name__ == "__main__":
    main()
