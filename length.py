# collect 2 input:
# Enter the acceleration (a)
# Enter the speed (v)
# find the length using the formula

a = float(input(" Enter the acceleration (a) "))

v = float(input(" Enter the speed (v) "))

length = ((v**2) / (2 * a))

print("The minimum runaway length for this airplane is ", round(length,2))

