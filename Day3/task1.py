import re

def parse_and_calculate(filename):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Initialize the sum of results
    total_sum = 0
    
    # Read input from the file
    with open(filename, "r") as f:
        data = f.read()
    
    # Find all matches in the data
    matches = re.findall(pattern, data)
    
    # Calculate the sum of results
    for x, y in matches:
        total_sum += int(x) * int(y)
    
    return total_sum

# Run the function with the input file
input_file = "input.txt"
result = parse_and_calculate(input_file)
print(f"Sum of all results: {result}")
