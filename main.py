#Divisores
# Get user input
number = int(input("Enter a number: "))

# Initialize a list to hold divisors
divisors = []

# Find divisors
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# Print the divisors
print(" ".join(map(str, divisors)))