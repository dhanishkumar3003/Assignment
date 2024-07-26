import os

def main():
    file1=input("Enter file name 1")
    file2=input("Enter file name 2")
    file_1=open(file1,'r')
    file_2=open(file2,'r')

    if file_1.read()==file_2.read():
        file_1.close()
        file_2.close()
        os.remove(file2)
    
if __name__=="__main__":
    main()