"""cell05"""
import re
def main():
    """"ex09"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if len(array) < 2:
        print("none") 
    else:
        find = str(array[0])
        text = str(array[1])
        count = len(re.findall(find, text))
        print(count)
main()
