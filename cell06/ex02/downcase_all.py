"""cell06"""
def downcase_it(mess):
    """Dowcase"""
    return mess.lower()

def main():
    """"ex02"""
    mess = str(input())
    array = [i.strip("\"") for i in mess.split('" "')]
    if array == [""]:
        print("none") 
    else:
        for i in array:
            print(downcase_it(i))
main()
