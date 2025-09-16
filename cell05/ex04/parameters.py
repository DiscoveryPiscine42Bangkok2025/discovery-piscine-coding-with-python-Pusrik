"""cell05"""
def main():
    """"ex04"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    count = 0
    if array != [""]:
        for _ in array:
            count += 1       
    print(f"Number of parameter: {count}.")
main()
