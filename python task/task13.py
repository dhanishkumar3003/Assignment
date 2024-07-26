import os

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

def main(input_filename, output_filename):
    content = read_file(input_filename)
    write_file(output_filename, content)

if __name__ == "__main__":
    input_filename = input("Enter file to copy from :")  
    CreateFile(input_filename)
    output_filename = input("Enter file to write to :")
    main(input_filename, output_filename)
