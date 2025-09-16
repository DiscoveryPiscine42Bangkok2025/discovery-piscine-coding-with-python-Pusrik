"""cell05"""
import re
def main():
    """"ex12"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if len(array) != 1 or array == [""]:
        print("none") 
    else:
        text = str(array[0])
        found = re.findall("z", text)
        for i in found:
            print(f"{i}", end="")
main()
