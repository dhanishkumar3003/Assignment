def filtering(course,symbol):
    for i in symbol:
        if i in course:
            return False
   
    return True
def main():
 
    symbol=[",",';','$']
    courses=['','python','java',',";$",','angul;ar','php']
    print(list(filter(lambda course : filtering(course,symbol) and course!="" ,courses)))
 
if __name__ == "__main__":
    main()
 