"""cell07"""
def famous_births(persons):
    """order by birth"""
    result = sorted(persons.items(), key=lambda x: x[1]["date_of_birth"])
    return result

def main():
    """ex03"""
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    ans = famous_births(women_scientists)
    print(ans)
main()