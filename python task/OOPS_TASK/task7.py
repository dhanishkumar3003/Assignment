class nums:
    def __init__(self, value):
        self.Value = value
    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        if self.Value <= 0:
            return False
        return self.SumFactors() == self.Value
    
    def Factors(self):
        factors = []
        for i in range(1, self.Value):
            if self.Value % i == 0:
                factors.append(i)
        return factors
    
    def SumFactors(self):
        sumOfFactors=0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sumOfFactors+=i
        return sumOfFactors
    
    def DisplayFactors(self):
        factors = self.Factors()
        print(f"Factors of {self.Value} are: {factors}")

def main():
    num = int(input("Enter a num: "))
    obj = nums(num)

    if obj.ChkPrime():
        print(f"{num} is a prime num.")
    else:
        print(f"{num} is not a prime num.")

    if obj.ChkPerfect():
        print(f"{num} is a perfect num.")
    else:
        print(f"{num} is not a perfect num.")

    obj.DisplayFactors()

    sum_factors = obj.SumFactors()
    print(f"Sum of factors of {num} is: {sum_factors}")

if __name__ == "__main__":
    main()
