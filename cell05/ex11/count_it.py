"""cell05"""
def main():
    """"ex11"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    count = 0
    if array != [""]:
        for _ in array:
            count += 1       
    print(f"Number of parameter: {count}.")
    for i in array:
        print(f"{i}: {len(i)}")
main()
