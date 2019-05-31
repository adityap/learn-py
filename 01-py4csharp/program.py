class employee():
    def weekly_salary(self, weeklyHrs, wage):
        raise NotImplementedError("This method must be implemented by a subclass")

class permanent(employee):
    def weekly_salary(self, weeklyHrs, wage):
        #print('$' + 40 * wage)
        print('${}, Overtime paid for {}' .format(40 * wage, weeklyHrs - 40))

class contractor(employee):
    def weekly_salary(self, weeklyHrs, wage):
        #print('$' + weeklyHrs * wage)
        print('${}, Overtime paid for {}' .format(weeklyHrs * wage, weeklyHrs - 40))

def get_employees():
    some_p = permanent()
    some_c = contractor()
    everyone = [some_p, some_c]
    return everyone

def main():
    emps = get_employees()
    for e in emps:
        e.weekly_salary(50, 70)


if __name__ == "__main__":
    main()


