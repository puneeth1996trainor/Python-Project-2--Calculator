import sys

class Operation:
    def __init__(self, operation, numbers):
        self.operation = operation;
        self.numbers = numbers;

def introduction():
    print("\n=== PYTHON CALCULATOR ===\n\n")

def print_instructions():
    instructions = "Type your command in this format: add 1,2"
    instructions += "\nPossible operations : add subtract multiply division"
    print(instructions)

def get_user_input():
    user_input = raw_input("Enter your command: ")
    print(user_input)
    return user_input


def parse_input(user_input):
    #add 30,50  === 80
    #^ op.  ^ Num. list
    #["a","b","c"] <=== List

    #Split string into op. and numbers
    user_input_parsed = user_input.split(" ")
    # ["add", "30,50"]
    #Make a list of numbers (that is eary to execute)
    user_input_numbers = user_input_parsed[1].split(",")
    user_input_numbers_int = []
    for number in user_input_numbers:
        user_input_numbers_int.append(int(number))


    operation = Operation(user_input_parsed[0], user_input_numbers_int)
    return operation



def run_operation(task):
    if task.operation == "add":
        #set a variable for the final answer
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        #Loop through numbers list
        for number in numbers:
            answer += number
        print(answer)
        # Add it to the final answer

    if task.operation == "subtract":
        #set a variable for the final answer
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        #Loop through numbers list
        for number in numbers:
            answer -= number
        print(answer)
        # Add it to the final answer

    if task.operation == "multiply":
        #set a variable for the final answer
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        #Loop through numbers list
        for number in numbers:
            answer *= number
        print(answer)
        # Add it to the final answer

    if task.operation == "division":
        #set a variable for the final answer
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        #Loop through numbers list
        for number in numbers:
            answer /= number
        print(answer)
        # Add it to the final answer

def answer_user(solution):
    answer = "\nYour answer is: "
    answer += str(solution)
    answer +="\n"
    print(answer)


def ask_again():
    again = raw_input("Would you like to enter another command : ")
    #if yes, returm True
    if again[0] == "y":
        return True
    if again[0] == "n":
        sys.exit()
    #If no, return false


def main():

    while True:
        introduction()
        print_instructions()
        user_input = get_user_input()
        operation = parse_input(user_input)
        answer = run_operation(operation)
        answer_user(answer)
        ask_again()

main()
