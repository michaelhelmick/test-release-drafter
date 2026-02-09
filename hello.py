def hello(name):
    return f"Hello, {name}!"

def today():
    from datetime import date
    return f"Today's date is {date.today()}."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(hello(name))
    print(today())
    print("Thanks!")
    print("Thanks 2!")
    print("Thanks 3!")
    print("Another one!")
    print("Anotha one!")
