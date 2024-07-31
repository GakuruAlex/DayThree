from is_even import is_even

def main() -> None:
    print(f"Welcome to even or odd number checker!")

    number_to_check = int(input("Number to check: "))

    results = is_even(number_to_check)

    if results:
        print(f"{number_to_check} is even!")
    else:
        print(f"{number_to_check} is odd!")

if __name__ == "__main__":
    main()