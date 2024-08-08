def countstringfrequency(filename, searchstring):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
        return

    contentlower = content.lower()
    searchstringlower = searchstring.lower()

    frequency = contentlower.count(searchstringlower)

    print(f"The string '{searchstring}' appears {frequency} times")
    
def main():
    filename = input("Enter the file name: ")
    searchstring = input("Enter the string to search for: ")
    countstringfrequency(filename, searchstring)

if __name__=="__main__":
    main()