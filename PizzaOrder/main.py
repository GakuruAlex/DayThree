from order_pizza import order_pizza

def main() -> None:
    print("Welcome to Python Pizza Deliveries")
    size = input("What Pizza size  do you want ?(S, M, L) ")
    pepperoni = input("Do you want pepperoni? Y or N: ")
    cheese = input("Do you want extra cheese? Y or N: ")

    bill = order_pizza(size.upper(), pepperoni.upper(), cheese.upper())
    print("Your final bill is ${}.".format(bill))


if __name__ == "__main__":
    main()