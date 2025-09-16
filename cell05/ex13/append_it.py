"""cell05"""
def main():
    """"ex13"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if array == [""]:
        print("none") 
    else:
        for i in array:
            if i[-3:] != "ism":
                print(f"{i}ism")
main()
