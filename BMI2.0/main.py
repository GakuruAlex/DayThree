from bmi_calculator_2 import bmi_calculator,categorize_bmi
def main() -> None:
    print("Welcome to BMI calculator 2.0!")
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))

    bmi = bmi_calculator(weight, height)
    category = categorize_bmi(bmi)

    print("Your BMI({:.2f}) is {}".format(bmi, category))

if __name__ == "__main__":
    main()