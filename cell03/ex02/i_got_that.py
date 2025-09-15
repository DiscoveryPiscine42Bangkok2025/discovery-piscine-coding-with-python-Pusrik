"""cell03"""
def main():
    """"ex02"""
    hello = str(input("What you gotta say? : "))
    if hello != "STOP":
        while True:
            mess = str(input("I got that! Anything else? : "))
            if mess == "STOP":
                break
main()
