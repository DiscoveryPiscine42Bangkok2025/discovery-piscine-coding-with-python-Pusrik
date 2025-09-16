"""cell05"""
def main():
    """"ex02"""
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    new = [i + 2 for i in array if i > 5]
    print(f"Original array: {array}")
    print(f"New array: {new}")
main()
