import string
import operator


def calculate_expression(expression: str) -> int:
    '''
    Receives a string with simple formulation of a
    mathematical expression and returns an integer number which
    is the result of that expression.

    Function supports such math operations as: "додати"/"плюс",
    "відняти"/"мінус", "помножити на", "поділити на".

    Note: The function does not take into account the priority
    of math operations (watch examples)

    Expressions that are not supported by the function:
    (Function returns «Неправильний вираз!»)
    - Not supported math operations
    («Скільки буде 3 в квадраті?»)
    - Not math expressions
    («Скільки сезонів в році?»)
    - Math operations with wrong syntax
    («Скільки буде 2 2 додати?»)

    # >>> calculate_expression("How much would it be 8 minus 3?")
    # 5
    # >>> calculate_expression("How much would it be 7 plus 3 times 5?")
    # 50
    # >>> calculate_expression("How much would it be 10 divide by -2 plus 11 minus -3?")
    # 9
    # >>> calculate_expression("How much would it be cube of three?")
    # 'Wrong Expression!'
    '''
    new_expression = expression.split()
    new_exp_check = []
    lst_nums = []
    lst_operators = []
    for element in new_expression:
        element = element.lower()

        if (element == "how") or (element == "much") or \
                (element == "would") or (element == "it") or (element == "be") or \
                (element == "by"):
            continue
        # element = element.rstrip(string.punctuation)
        if element in ['+', '-', '/', 'x', '÷']:
            lst_operators.append(element)
            new_exp_check.append(element)
        else:
            lst_nums.append(float(element))
            new_exp_check.append(float(element))

    for index in range(len(new_exp_check) - 1):
        if type(new_exp_check[index]) == type(new_exp_check[index + 1]):
            return 'Wrong Expression!'

    if len(new_exp_check) == 1 and type(new_exp_check[-1]) is float:
        return int(new_exp_check[-1])

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "x": operator.mul,
        "/": operator.truediv,
        "÷": operator.truediv
    }

    for operations in lst_operators:
        if operations not in ops:
            return 'Wrong Expression!'

    operation = 0
    result = 0
    start = lst_nums[0]
    for index in range(len(lst_nums)):
        if index == (len(lst_nums) - 1):
            break
        try:
            result = ops[lst_operators[operation]](start, lst_nums[index + 1])
        except ZeroDivisionError:
            return 'Wrong Expression!'
        operation += 1
        start = result
    return result

