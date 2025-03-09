n = int(input("Enter a Number : "))
def recur_factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * recur_factorial(n - 1)
print(f"Factorial of {n} is : {recur_factorial(n)}")
