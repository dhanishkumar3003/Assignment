import os
import filecmp
def CreateFile(file_name):
    if (os.path.exists(file_name)):
        print("Filer already exists")
    else:
        file_create=open(file_name,'w')
        file_create.write(input("Enter fiel content"))

def read_file(input_filename):
    file= open(input_filename, 'r') 
    return file.read()

def write_file(output_filename, content):
    file= open(output_filename, 'w')
    file.write(content)


def comparefile(file1,file2):
    if not os.path.exists(file1) or not  os.path.exists(file2):
        print("file does not exist")
    else:
        compare = filecmp.cmp(file1,file2)
        if compare:
            print("Success files are same")
        else:
            print("files are different")


def main(input_filename, output_filename):
    content = read_file(input_filename)
    write_file(output_filename, content)
    comparefile(input_filename,output_filename)

if __name__ == "__main__":
    input_filename = input("Enter file to copy from :")  
    CreateFile(input_filename)
    output_filename = input("Enter file to write to :")
    main(input_filename, output_filename)
