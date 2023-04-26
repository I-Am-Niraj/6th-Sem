# Mapping of operators to their corresponding three address code instructions
ops_dict = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}

# Read input expressions from a txt file
with open('Expt8.txt', 'r') as f:
    input_str = f.read()

# Split the input string into lines by newline character
input_lines = input_str.split('\n')

# Remove any empty lines from the list
input_lines = [line for line in input_lines if line]

# Initialize the target code as an empty string
target_code = ''

# Loop over the input lines to generate the target code for each expression
for input_line in input_lines:
    # Split the input line into tokens by whitespace
    input_tokens = input_line.split()

    # Validate that the input expression is well-defined
    if len(input_tokens) < 4 or input_tokens[1] != '=':
        print(f'Error: invalid input expression {input_line}')
    else:
        # Extract the left-hand side variable
        left_var = input_tokens[0]

        # Initialize the counter for the register number
        register_counter = 0

        # Loop over the input tokens to generate the target code
        for token in input_tokens[2:]:
            if token in ops_dict:
                # If the token is an operator, save it for later use
                operator = token
            else:
                # If the token is an operand, assign it to a register and generate the appropriate three address code instruction
                target_code += f'MOV {token}, R{register_counter}\n'
                if register_counter == 0:
                    register_counter += 1
                else:
                    target_code += f'{ops_dict[operator]} R{register_counter-1}, R{register_counter}\n'
                    register_counter += 1

        # Generate the final instruction to assign the result of the expression to the left-hand side variable
        target_code += f'MOV R{register_counter-1}, {left_var}\n'

# Write the final target code to a txt file
print(target_code)