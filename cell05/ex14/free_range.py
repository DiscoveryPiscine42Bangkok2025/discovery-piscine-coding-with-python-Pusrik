"""cell05"""
def main():
    """"ex14"""
    num = str(input())
    array = [i for i in num.split()]
    if len(array) == 2:
        num1 = int(array[0])
        num2 = int(array[1])
        ans = []
        for i in range(num1, num2+1, 1):
            ans.append(i)
        print(ans)
    else:
        print("none") 
main()
