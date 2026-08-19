students = {"Andi" : 16,
        "Budi" : 17,
        "Clara" : 16}

add = {"Dimas" : 25}

try:
    with open("student_data.txt", "x") as file:
        for key, value in dict.items():
            file.write(f"{key:10} : {value}\n")       
except FileNotFoundError:
    print("The specified file was not found")
except FileExistsError:
    print("File was already exist")


with open("student_data.txt", "a") as file:
    for key, value in add.items():
        file.write(f"{key:10} : {value}\n")

with open("student_data.txt", "r") as file:
    print(file.read())