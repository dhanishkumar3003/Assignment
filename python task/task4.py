def calculate_frequency(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for char,freq in d.items():
        print(char,freq)

if __name__=="__main__":
    s=input("Enter string : ")
    calculate_frequency(s)