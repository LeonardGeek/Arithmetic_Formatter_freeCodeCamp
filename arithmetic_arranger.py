def arithmetic_arranger(problems, answer = False):
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    # Check the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        first_operand, operator, second_operand = problem.split()
        # Check the appropriate operators
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'." 
        # Check each operand should only contain digits
        elif first_operand.isdigit() == False or second_operand.isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        # Check each operand has a max of four digits in width   
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        length = max(len(first_operand), len(second_operand))
        first_line.append(first_operand.rjust(length + 2))
        second_line.append(operator + ' ' + second_operand.rjust(length))
        third_line.append(''.rjust(length + 2, '-'))
        if answer:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))
                fourth_line.append(result.rjust(length + 2)) 
            else:
                result = str(int(first_operand) - int(second_operand))
                fourth_line.append(result.rjust(length + 2))
    if answer:
        arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line) + '\n' + '    '.join(fourth_line)
    else:
        arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(third_line)

    return arranged_problems