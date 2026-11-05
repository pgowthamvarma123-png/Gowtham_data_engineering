import json

# Input JSON file
input_file = r"C:\Users\gpenmetsa3\Desktop\gowtham\users-100.json"

# Output NDJSON file
output_file = r"C:\Users\gpenmetsa3\Desktop\gowtham\users-100-ndjson.json"

# Read the JSON array
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Write each JSON object on a separate line
with open(output_file, "w", encoding="utf-8") as file:
    for record in data:
        file.write(json.dumps(record) + "\n")

print("Conversion completed successfully!")
print("Output file:", output_file)