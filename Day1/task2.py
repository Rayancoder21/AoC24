from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read().splitlines()
a =[]
b =[]
total = 0
for i in data:
    nums = [int(x) for x in i.split("   ")]
    a.append(nums[0])
    b.append(nums[1])
counts = defaultdict(int)
for x in b:
    counts[x] += 1
for x in a:
    total += counts[x]* x
# Output the result
print(f"The total distance between the lists is: {total}")



    