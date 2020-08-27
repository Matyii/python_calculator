# Program make a simple calculator

print("----------------------")
print("[SZÁMOLÓGÉP]")
print("----------------------")
# A két szám hozzáadása
def add(x, y):
    return x + y

# Kivonás function
def subtract(x, y):
        return x - y

# Szorzás function
def multiply(x, y):
    return x * y

# Osztás function
def divide(x, y):
    return x / y


print("Válassz!")
print("1. Összeadás")
print("2. Kivonás")
print("3. Szorzás")
print("4. Osztás")

while True:
    # Take input from the user
    choice = input("Válassz! (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Első szám: "))
        num2 = float(input("Második szám: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Rossz válasz")

input("Nyomj Entert a kilépéshez!")