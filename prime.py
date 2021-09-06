number = int(input())

divisors = 0

for i in range(number):
    if number % (i + 1) == 0:
        divisors += 1

print("This number is prime" if divisors == 2 else "This number is not prime")
