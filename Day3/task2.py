import re

def parse_and_calculate_with_conditions(filename):
    # Regular expressions for instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initialize the sum of results and enabled state
    total_sum = 0
    enabled = True
    
    # Read input from the file
    with open(filename, "r") as f:
        data = f.read()
    
    # Sequentially process the input
    index = 0
    while index < len(data):
        # Check for 'do()' instruction
        if re.match(do_pattern, data[index:]):
            enabled = True
            index += len("do()")
        
        # Check for 'don't()' instruction
        elif re.match(dont_pattern, data[index:]):
            enabled = False
            index += len("don't()")
        
        # Check for 'mul(X,Y)' instruction
        elif (match := re.match(mul_pattern, data[index:])):
            if enabled:
                x, y = map(int, match.groups())
                total_sum += x * y
            index += len(match.group(0))
        
        # Skip other characters
        else:
            index += 1
    
    return total_sum

# Run the function with the input file
input_file = "input.txt"
result = parse_and_calculate_with_conditions(input_file)
print(f"Sum of enabled results: {result}")
