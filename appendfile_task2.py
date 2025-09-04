# Step 1: Take user input and write to a file
user_input = input("Enter some text to write to output.txt: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
more_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(more_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
