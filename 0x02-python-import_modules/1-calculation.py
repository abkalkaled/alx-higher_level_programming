#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum = add(a, b)
diff = sub(a, b)
mult = mul(a, b)
divd = div(a, b)
print('{:d} + {:d} = {:d}'.format(a, b, sum))
print('{:d} - {:d} = {:d}'.format(a, b, diff))
print('{:d} * {:d} = {:d}'.format(a, b, mult))
print('{:d} / {:d} = {:d}'.format(a, b, divd))
