# n = 0
# for i in range(1, 500):
#     if not i % 5 or not i % 3:
#         n = n + i
# print(n)

# index = 0
# count = 0
# for i in range(1,1001):
#     if index % 3 == 0 or index % 5 == 0:
#         count += index
#     index += 1
# print(count)

i = 1
count = 0

while i >= 1 and i <= 1000:
    if i % 3 == 0 or i % 5 == 0:
        count += i
    i += 1
print(count)
