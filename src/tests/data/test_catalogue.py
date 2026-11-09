from src.catalogue import compter_stations, filtrer_stations, MAX_STATIONS, MAX_PREFIXE

STATIONS = ["Bercy", "Montparnasse", "Gare du Nord"]


def leve_value_error(fonction, *args):
    try:
        fonction(*args)
    except ValueError:
        return True
    return False


# ---------- compter_stations ----------

# Cas normal
assert compter_stations(["Paris Nord", "Paris Est", "Lyon Part-Dieu"], "Paris") == 2
assert compter_stations(["Paris Nord", "Lyon Part-Dieu"], "Marseille") == 0

# Cas vides
assert compter_stations([], "Paris") == 0
assert compter_stations(["Paris Nord", "Lyon"], "") == 2

# Casse
assert compter_stations(["paris nord", "Paris Est", "PARIS Lyon"], "Paris") == 3
assert compter_stations(["paris nord", "Paris Est"], "paris") == 2

# Limites
assert compter_stations(["A"] * MAX_STATIONS, "A") == MAX_STATIONS
assert compter_stations(["A"], "A" * MAX_PREFIXE) == 0
assert leve_value_error(compter_stations, ["A"] * (MAX_STATIONS + 1), "A")
assert leve_value_error(compter_stations, ["A"], "A" * (MAX_PREFIXE + 1))

print("compter_stations : OK")


# ---------- filtrer_stations ----------

# Cas normal
assert filtrer_stations(STATIONS, "Bercy") == ["Bercy"]
assert filtrer_stations(STATIONS, "Saint-Gervais") == []

# Cas vides
assert filtrer_stations(STATIONS, "") == STATIONS
assert filtrer_stations([], "Test") == []

# Casse (le nom d'origine est conservé)
assert filtrer_stations(STATIONS, "bercy") == ["Bercy"]
assert filtrer_stations(["BErCy", "Montparnasse"], "bercy") == ["BErCy"]

# Limites
assert filtrer_stations(["A"] * MAX_STATIONS, "A") == ["A"] * MAX_STATIONS
assert leve_value_error(filtrer_stations, ["A"] * (MAX_STATIONS + 1), "A")
assert leve_value_error(filtrer_stations, ["A"], "A" * (MAX_PREFIXE + 1))

print("filtrer_stations : OK")
print("Tous les tests passent.")