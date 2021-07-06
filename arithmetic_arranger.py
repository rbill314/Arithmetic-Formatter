def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for index, value in enumerate(problems):
        # ["32", "+", "8"]
        operation = value.split(" ")

        if operation[1] not in "-+":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            value_1 = int(operation[0])
            value_2 = int(operation[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2

        L1 = f"{operation[0]:>{width}}"
        L2 = operation[1] + f"{operation[2]:>{width-1}}"
        d = '-'*width

        try:
            arranged_problems[0] += (' ' * 4) + L1
        except IndexError:
            arranged_problems.append(L1)

        try:
            arranged_problems[1] += (' ' * 4) + L2
        except IndexError:
            arranged_problems.append(L2)

        try:
            arranged_problems[2] += (' ' * 4) + d
        except IndexError:
            arranged_problems.append(d)

        if args:

            ans = int(operation[0]) + int(operation[2]
                                          ) if operation[1] == '+' else int(operation[0]) - int(operation[2])

            a = f"{str(ans):>{width}}"

            try:
                arranged_problems[3] += (' ' * 4) + a
            except IndexError:
                arranged_problems.append(a)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"

    output = output + f"\n{arranged_problems[3]}" if args else output

    return output

    # Thanks to Gwen Faraday who walked me through this FreeCodeCamp Project.
    # The video I watched that (which she was kind enough to take the time to provide)
    # is at her youTube channel Faraday Academy.. https://www.youtube.com/c/FaradayAcademy/featured
    # The link is https://www.youtube.com/watch?v=ZBJUihOVvVM
    # This is my first time with python and I will come back to this project as I
    # further skills through the other projects.
    # 7/4/2021
    # Done on VS Code
