"""cell05"""
def main():
    """"ex06"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if len(array) != 1 or array == [""]:
        print("none") 
    else:
        print(array[0].upper())
main()
