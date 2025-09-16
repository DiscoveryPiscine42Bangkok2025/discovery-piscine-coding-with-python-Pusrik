"""cell05"""
def main():
    """"ex08"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    array.reverse()
    if len(array) <= 2:
        print("none") 
    else:
        for i in array:
            print(i)
main()
