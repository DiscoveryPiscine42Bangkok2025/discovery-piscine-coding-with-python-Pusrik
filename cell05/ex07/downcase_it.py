"""cell05"""
def main():
    """"ex07"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if len(array) != 1 :
        print("none") 
    else:
        print(array[0].lower())
main()
