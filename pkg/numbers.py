import os
def add_5_to_file():
    if os.path.exists("number.txt") == False:
        with open("number.txt","w") as file:
            file.write("0")

    with open("number.txt","r") as file:
        a =  int(file.read())

    with open("number.txt","w") as file:
        a += 5
        file.write(str(a))

def main():
    add_5_to_file()

if __name__ == "__main__":
    main()