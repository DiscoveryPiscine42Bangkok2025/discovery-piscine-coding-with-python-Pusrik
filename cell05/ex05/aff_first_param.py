"""cell05"""
def main():
    """"ex05"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if array != [""]:
        print(array[0])
    else:
        print("none")
main()
