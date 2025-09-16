"""cell05"""
def main():
    """"ex10"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if len(array) != 1 or array == [""]:
        print("none") 
    else:
        find = str(array[0])
        check = str(input("What was the parameter? "))
        if find == check:
            print("Good job")
        else:
            print("Nope, sorry...")
main()
