#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5

    result_add = calculator.add(a, b)
    result_sub = calculator.sub(a, b)
    result_mul = calculator.mul(a, b)
    result_div = calculator.div(a, b)

    print("{} + {} = {}\n{} - {} = {}".format(a, b, result_add, a, b, result_sub))
    print("{} * {} = {}\n{} / {} = {}".format(a, b, result_mul, a, b, result_div))
