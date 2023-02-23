# This is the mandatory assignment 1

#Task 1
Directors = {
    "Benny",
    "Hans",
    "Tine",
    "Mille",
    "Torben",
    "Troels",
    "Søren"
}

Management = {
    "Tine",
    "Trunte",
    "Rane"
}

Employees = {
    "Niels",
    "Anna",
    "Tine",
    "Ole",
    "Trunte",
    "Bent",
    "Rane",
    "Allan",
    "Stine",
    "Claus",
    "James",
    "Lars"
}
# Who in the board of directors is not an employee?
board_not_employee = Directors - Employees
print("Who in the board of directors is not an employee")
print(board_not_employee)

# Who in the board of directors is also an employee?
board_is_employee = Directors & Employees
print("Who in the board of directors is also an employee")
print(board_is_employee)

# How many of the management is also member of the board?
management_member = Directors & Management
amount_of_management_in_board = len(management_member)
print("How many of the management is also member of the board")
print(amount_of_management_in_board)

# All members of the managent also an employee
management_employee = Employees & Management
print("All members of the managent also an employee")
print(management_employee)

# All members of the management also in the board?
management_member = Directors & Management
print("All members of the management also in the board")
print(management_member)

# Who is an employee, member of the management, and a member of the board?
employee_management_member = Directors & Management & Employees
print("Who is an employee, member of the management, and a member of the board")
print(employee_management_member)

# Who of the employee is neither a memeber or the board or management?
employee_neither_member_management = Employees - Directors - Management
print("Who of the employee is neither a memeber or the board or management")
print(employee_neither_member_management)

# Task 2
tuple_list_alphabet = {"a": "Alpha", "b": "Beta", "g": "Gamma"}
print("Alphabet list:")
print(tuple_list_alphabet)

# Task 3
eng_letters = {"a", "e", "i", "o", "u", "y"}
print("English letters:")
print(eng_letters)
dk_letters = {"a", "e", "i", "o", "u", "y", "æ", "ø", "å"}
print("Danish letters:")
print(dk_letters)

# Union of the two
def Union(eng_letters, dk_letters):
    final_list = list(set(eng_letters) | set(dk_letters))
    final_list_sorted = sorted(final_list)
    return final_list_sorted
print("Union of the two:")
print(Union(eng_letters, dk_letters))

# Symmetric difference of the two
def symmetric_diff(eng_letters, dk_letters):
    (_eng_letters, _dk_letters) = (set(eng_letters), set(dk_letters))
    return [item for item in eng_letters if item not in _dk_letters] + [item for item in dk_letters
          if item not in _eng_letters]
print("Symmetric difference equals:")
print(symmetric_diff(eng_letters, dk_letters))

# Difference of the two
s = set(eng_letters)
difference = [x for x in dk_letters if x not in s]
print("Difference equals:")
print(difference)

# Disjoint of the two
disjoint = eng_letters & dk_letters
print("Disjoint equals:")
print(disjoint)

# Task 4 Date Decoder
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

#Create a dict suitable for decoding month names to numbers.

#Create a function which uses string operations to split the date into 3 items using the "-" character.

#Translate the month, correct the year to include all of the digits.

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

def change_date(convert_date):
    the_changed_data_list = []

    months = {"JAN" : 1, "FEB" : 2, "MAR" : 3,"APR" : 4, "MAY" : 5,
                       "JUN"  :6, "JUL" : 7,"AUG" : 8, "SEP" : 9,"OCT" : 10,
                       "NOV" : 11,"DEC" : 12}

    input_split = convert_date.split('-')

    #Find the year:
    if int(input_split[2])>=0:
        year = '20' + input_split[2]
    else:
        year = '19' + input_split[2]

    the_changed_data_list.append(year)

    #Find the month:
    month = months[input_split[1].upper()]
    the_changed_data_list.append(month)

    #Find the day:
    day = input_split[0]
    the_changed_data_list.append(day)

    changed_date_list = [str(item) for item in changed_date_list]
    return the_changed_data_list


def main():
    user_date = input("Enter a date in this format: dd-MMM-yy \n") # 8-MAR-85
    print(','.join((change_date(user_date))))

main()
