def sumoflist(arr):
    ans=0
    for i in arr:
        ans+=i
    print("Sum ",ans)
def maxoflist(arr):
    ans=arr[0]
    for i in arr:
        if ans<i:
            ans=i
    print("Max ",ans)
def main():
    arr=[]
    n=int(input("Enter number of elements in list"))
    for i in range(0,n):
        arr.append(int(input(f"Enter element {i} ")))
    sumoflist(arr)
    maxoflist(arr)
if __name__=="__main__":
    main()