"""cell06"""
def shrink(text):
    """more than 8 digit"""
    return text[:8]

def enlarge(text):
    """less than 8 digit"""
    digit = len(text)
    text = text + ("Z" * (8-digit))
    return text
    

def main():
    """"ex04"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if array == [""]:
        print("none") 
    else:
        for i in array:
            if len(i) >= 8:
                print(shrink(i))
            else:
                print(enlarge(i))
main()

