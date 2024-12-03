def is_safe_report(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if all differences are in range [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in diffs):  # Increasing
        return True
    if all(-3 <= diff <= -1 for diff in diffs):  # Decreasing
        return True
    
    # Otherwise, it's unsafe
    return False

def count_safe_reports(data):
    safe_count = 0
    for line in data:
        levels = list(map(int, line.split()))  # Convert line to a list of integers
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

# Input handling
with open("input.txt") as f:
    data = f.readlines()

# Count the safe reports
safe_count = count_safe_reports(data)
print(f"Number of safe reports: {safe_count}")