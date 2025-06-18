from decimal import Decimal
import json
import ast

# Load the original data from the uploaded file
file_path = fr"C:\Users\karthim\Downloads\100.json"
with open(file_path, "r") as f:
    raw_data = f.read()

# Step 1: Convert Python-style dict string to an actual Python dictionary
# Replace Decimal('...') with float, and eval safely using ast.literal_eval
def safe_decimal_eval(obj_str):
    obj_str = obj_str.replace("Decimal('", "").replace("')", "")
    obj_str = obj_str.replace("Decimal(\"", "").replace("\")", "")
    return ast.literal_eval(obj_str)

# Step 2: Convert string lists like "[11]" to actual lists
def fix_string_lists(data):
    if isinstance(data, dict):
        return {k: fix_string_lists(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [fix_string_lists(v) for v in data]
    elif isinstance(data, str):
        # Handle stringified lists like "[11]"
        if data.startswith("[") and data.endswith("]"):
            try:
                return ast.literal_eval(data)
            except Exception:
                return data
        return data
    else:
        return data

# Step 3: Apply transformations
parsed_data = safe_decimal_eval(raw_data)
fixed_data = fix_string_lists(parsed_data)

# Step 4: Convert back to valid JSON
# output_path = fr"demo"
with open('100', "w") as f:
    json.dump(fixed_data, f, indent=2)

# output_path
