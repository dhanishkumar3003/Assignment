import os

def appendfile(filename):
    if (os.path.exists(filename)):
        file= open(filename,'a')
        file.write(input("Enter content to append"))
    else:
        print("File does not exist")
def main():
    filename= input("Enter file to append :")  
    appendfile(filename)

if __name__ == "__main__":
    main()