x = 1
y = 1
count = 0
fib_even_sum = 0
while count <= 4000000:
    count = x + y
    x = y
    y = count
    if count % 2 == 0:
        fib_even_sum += count
print(fib_even_sum)

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1
