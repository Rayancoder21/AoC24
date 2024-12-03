def is_safe_report(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if all differences are in range [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in diffs):  # Increasing
        return True
    if all(-3 <= diff <= -1 for diff in diffs):  # Decreasing
        return True
    
    # Otherwise, it's unsafe
    return False

def is_safe_with_dampener(levels):
    # Check if the original report is safe
    if is_safe_report(levels):
        return True

    # Try removing one level at a time and check if it becomes safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]  # Remove level at index i
        if is_safe_report(modified_levels):
            return True

    # If no single-level removal makes it safe, it's unsafe
    return False

def count_safe_reports_with_dampener(data):
    safe_count = 0
    for line in data:
        levels = list(map(int, line.split()))  # Convert line to a list of integers
        if is_safe_with_dampener(levels):
            safe_count += 1
    return safe_count

# Input handling
with open("input.txt") as f:
    data = f.readlines()

# Count the safe reports with the Problem Dampener
safe_count_with_dampener = count_safe_reports_with_dampener(data)
print(f"Number of safe reports (with dampener): {safe_count_with_dampener}")