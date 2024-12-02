# l1 = []
# l2 = []
# with open("input.txt", 'r') as file:
#     for line in file:
#         numbers = [int(x) for x in line.split()]
#         l1.append(numbers[0])
#         l2.append(numbers[1])

# l1.sort()
# l2.sort()
# totals = []
# total = len(l1)
# x = 0
# while x < total:
#     #print("L1 : " + str(l1[x]) + " L2 = " + str(l2[x]))
#     totals.append(abs(l2[x]-l1[x]))
#     x = x + 1
# #print(totals)
# big = 0
# for x in totals:
#     big = big + x

# print(big)



#Part two

l1 = []
l2 = []
with open("input.txt", 'r') as file:
    for line in file:
        numbers = [int(x) for x in line.split()]
        l1.append(numbers[0])
        l2.append(numbers[1])

counts = []
for x in l1:
    num = 0
    num = l2.count(x)
    if num > 0:
        counts.append(x * num)

xx = sum(counts)
print(xx)



