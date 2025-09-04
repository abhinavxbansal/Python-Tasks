def read_file():
    try:
        # Open the file in read mode
        with open("sample.txt", "r") as file:
            # Print each line from the file
            for line in file:
                print(line.strip())  # strip() removes extra newline characters
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")

# Run the function
read_file()
