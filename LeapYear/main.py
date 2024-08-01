from is_leap_year import is_leap_year

def main()-> None:
    print("Welcome to leap year checker!")
    year = int(input("Year to check: "))
    is_leap = is_leap_year(year)
    
    if is_leap:
        print(f"The year {year} is leap")
    else:
        print(f"The year {year} is not leap")

if __name__ == "__main__":
    main()