import os
def add_5_to_file():
    if os.path.exists("number.txt") == False:
        with open("number.txt","w") as file:
            file.write("0")

    with open("number.txt","r") as file:
        a =  file.read()
    
    if a == "":
        with open("number.txt","w") as file:
            file.write("0")

    else:
        with open("number.txt","r") as file:
            a =  int(file.read())
            a += 5
    
        with open("number.txt","w") as file:
            file.write(str(a))

def main():
    add_5_to_file()

if __name__ == "__main__":
    main()