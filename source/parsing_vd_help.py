import json

# Initialize an empty list to store the parsed options
parsed_options = []

# Initialize variables to hold option details and state
current_option = {}

# Possible states in the state machine
START, IT_OPTION = range(2)

# Read the file line by line and parse relevant information
with open('vd_COMMANDLINE_OPTIONS.roff', 'r') as f:
    lines = f.readlines()

# Set the initial state
state = START

for line in lines:
    line = line.strip()

    if line:
        if state == START:
            if line.startswith(".It Sy"):
                # Extract long option, type, and default value for '.It Sy' block
                parts = line.split('=')
                current_option['long'] = parts[0].split()[2] if len(parts) > 0 else None
                current_option['type'] = parts[0].split('"')[1].strip() if '"' in parts[0] else None
                current_option['default'] = parts[1].split('"')[1].strip() if len(parts) > 1 and '"' in parts[1] else None
                state = IT_OPTION

        elif state == IT_OPTION:
            # Extract description for '.It Sy' block
            current_option['description'] = line

            # Save the current option and reset state
            parsed_options.append(current_option)
            current_option = {}
            state = START

# Swap 'type' and 'default' fields for each option
corrected_parsed_options = []
for option in parsed_options:
    corrected_option = option.copy()
    corrected_option['type'] = option.get('default')
    corrected_option['default'] = option.get('type')
    corrected_parsed_options.append(corrected_option)

# Save the corrected parsed options to a final JSON file
with open('parsed_options_final.json', 'w') as f:
    json.dump(corrected_parsed_options, f, indent=4)
