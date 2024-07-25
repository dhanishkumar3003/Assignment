def calculate_grads(mark):
    if mark>=90:
        mark=90
    elif mark>=80:
        mark=80
    elif mark>=70:
        mark=70
    elif mark>=60:
        mark=60
    elif mark>=40:
        mark=40
    else:
        mark=39
    grade={
        90:"A",
        80:"B",
        70:"C",
        60:"D",
        40:"E",
        39:"Fail",
    }
    print("Your grade is ",grade[mark])
    
if __name__ == "__main__":
    calculate_grads(int(input("Enter your mark : ")))