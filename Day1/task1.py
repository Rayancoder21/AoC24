with open("input.txt", "r") as file:
    data = file.read().splitlines()
a =[]
b =[]
for i in data:
    nums = [int(x) for x in i.split("   ")]
    a.append(nums[0])
    b.append(nums[1])
total_distance = 0
a.sort()
b.sort()
for i in range(len(a)):
    total_distance += abs(a[i] - b[i])

# Output the result
print(f"The total distance between the lists is: {total_distance}")
