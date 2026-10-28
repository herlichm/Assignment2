"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return annual_cost / SEMESTERS_PER_YEAR

    # return 0


def cost_per_month(annual_cost):
    return annual_cost / MONTHS_PER_YEAR

    # return 0


def cost_per_day(annual_cost):
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    # return 0


def cost_per_credit(annual_cost, credits):
     return annual_cost / (credits * SEMESTERS_PER_YEAR)

    # return 0


def cost_per_class(annual_cost, credits):
     return (cost_per_credit(annual_cost, credits))* CS1430_CREDITS/ CS1430_MEETINGS_PER_SEMESTER

    # return 0


# ---- PROGRAM ----

def main():
    total_cost = float(input("Enter the total cost for one year: $"))
    credits = int(input("Enter the number of credits this semester: "))

    while True:

        print("Menu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        # Add a branch for each menu option here.
        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(total_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(total_cost):.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(total_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(total_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(total_cost, credits):.2f}")
        else:
            print("Invalid choice. Please try again.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
