import os

def deletefile(filename):
    if (os.path.exists(filename)):
        os.remove(filename)
        if (os.path.exists(filename)):
            print("Failed to delete the file")
        else:
            print("File deleted successfully")
    else:
        print("File does not exist")
def main():
    filename= input("Enter file to delete :")  
    deletefile(filename)
    pass

if __name__ == "__main__":
    main()