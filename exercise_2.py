string_input = input("Enter a string: ")

reversed_string = ""

for i in string_input:
    reversed_string = i + reversed_string

print("The original string is: ", string_input)
print("The reversed string is: ", reversed_string)


