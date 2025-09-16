"""cell07"""
def array_of_names(person):
    """name"""
    result = [f"{first.capitalize()} {last.capitalize()}" for first, last in person.items()]
    return result

def main():
    """ex00"""
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
main()
