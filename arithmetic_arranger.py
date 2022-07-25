def arithmetic_arranger(problems, answers=False):
    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        values = problem.split(" ")
        operator = values[1]
        for item in values:
            if item == operator:
                continue
            else:
                try:
                    item = int(item)
                except:
                    return "Error: Numbers must only contain digits."
            item = str(item)
            if len(item) < 5:
                continue
            else:
                return "Error: Numbers cannot be more than four digits."

        if operator == "+" or operator == "-":
            continue
        else:
            return "Error: Operator must be '+' or '-'."

    # Empty strings for output formatting
    line = "-"
    first = ""
    second = ""
    lines = ""
    result = ""

    iteration = 0

    for problem in problems:
        # Extracting the longest number of each problem (for correct spacing)
        problem = problem.split(" ")
        operator = problem[1]
        num_of_char = max(len(problem[0]), len(problem[2])) + 2

        # Calculation
        if operator == "+":
            answer = int(problem[0]) + int(problem[2])
            answer = str(answer)
        else:
            answer = int(problem[0]) - int(problem[2])
            answer = str(answer)

        # Output formatting
        first += problem[0].rjust(num_of_char)
        second += operator + problem[2].rjust(num_of_char - 1)
        lines += line * num_of_char
        result += answer.rjust(num_of_char)

        iteration += 1

        # Adding spaces between calculations
        if len(problems) > iteration:
            first += "    "
            second += "    "
            lines += "    "
            result += "    "

    if answers:
        return first + "\n" + second + "\n" + lines + "\n" + result
    else:
        return first + "\n" + second + "\n" + lines
