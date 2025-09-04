students={'Abhinav':'96','Priya':'89', 'Sonam':'86'}
name=input("Enter your name:")
if name in students:
    print(f"{name} marks is: {students[name]}")
else:
    print("record not found")