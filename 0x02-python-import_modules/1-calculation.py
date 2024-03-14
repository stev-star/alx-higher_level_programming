#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1

    a = 10
    b = 5

result = calculator_1.add(a, b)
result1 = calculator_1.sub(a, b)
result2 = calculator_1.mul(a, b)
result3 = calculator_1.div(a, b)
print("{:d} + {:d} = {:d}".format(a, b, result))
print("{:d} - {:d} = {:d}".format(a, b, result_1))
print("{:d} * {:d} = {:d}".format(a, b, result_2))
print("{:d} / {:d} = {:d}".format(a, b, result_3))
