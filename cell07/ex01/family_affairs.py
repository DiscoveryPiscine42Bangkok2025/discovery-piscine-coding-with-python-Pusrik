"""cell07"""
def find_the_redheads(family):
    """find red hair"""
    result = [i for i in family if family[i] == "red"]
    return result

def main():
    """ex01"""
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
main()