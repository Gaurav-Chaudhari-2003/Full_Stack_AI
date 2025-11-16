# 2)Dictionary Student Record
# Topics: Dictionary Create, Access, Add, Update, Remove, Keys, Values, Clear
# Problem:
# Create a dictionary storing student data: {"name":"Shri", "age":25, "course":"Python"}
# Add key “marks”
# Update age
# Remove course
# Print all keys and values
# Clear dictionary

print("\nCreate a dictionary storing student data:")
studentData = {
    "name":"Shri",
    "age":25,
    "course":"Python"
}
print(studentData)

print("\nAdd key 'marks':")
studentData["marks"] = 90
print(studentData)

print("\nUpdate age:")
studentData["age"] = 26
print(studentData)

print("\nRemove key 'course':")
studentData.pop("course")
print(studentData)

print("\nPrint all keys and values:")
for key, value in studentData.items():
    print(f"Key({key}) : Value({value})")

print("\nClear dictionary:")
studentData.clear()
print(studentData)
