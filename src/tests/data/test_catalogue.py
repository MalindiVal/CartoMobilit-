from src.catalogue import compter_stations,filtrer_stations,MAX_STATIONS,MAX_PREFIXE

# Cas normal
assert compter_stations(["Paris Nord", "Paris Est", "Lyon Part-Dieu"], "Paris") == 2
assert compter_stations(["Paris Nord", "Lyon Part-Dieu"], "Marseille") == 0
assert compter_stations(["Paris Nord", "Paris Est"], "Paris") == 2

# Cas vides
assert compter_stations([], "Paris") == 0
assert compter_stations(["Paris Nord", "Lyon"], "") == 2   # tout nom commence par ""

# Casse
assert compter_stations(["paris nord", "Paris Est", "PARIS Lyon"], "Paris") == 1
assert compter_stations(["paris nord", "Paris Est"], "paris") == 1

print("Tous les tests pour passent.")



assert filtrer_stations(["Bercy","Montparnasse","Gare du Nord"],"Bercy") == ["Bercy"]

assert filtrer_stations(["Bercy","Montparnasse","Gare du Nord"],"bercy") == ["Bercy"]

assert filtrer_stations(["Bercy","Montparnasse","Gare du Nord"],"Saint-Gervais") == []

assert filtrer_stations(["Bercy","Montparnasse","Gare du Nord"],"") == ["Bercy","Montparnasse","Gare du Nord"]

assert filtrer_stations([],"Test") == []

print("Tous les tests passent.")