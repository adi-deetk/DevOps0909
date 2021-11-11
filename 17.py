def div_numbers(a, b):
    print(int(a/b))
try:
    div_numbers(8,2)
    div_numbers(9,0)
except ZeroDivisionError as e:
    print(e.args)
    print("something went terribly worng")
print("aviel")

