def square_numbers(n):
    ans=[]
    for i in range(1,n+1):
        ans.append(i*i)
    print(ans)
if __name__=="__main__":
    square_numbers(int(input("Enter number")))