MAX_STATIONS = 150
MAX_PREFIXE = 255

def _verifier_entrees(noms, prefixe):
    if len(noms) > MAX_STATIONS:
        raise ValueError(f"Trop de stations : {len(noms)} (max {MAX_STATIONS})")
    if len(prefixe) > MAX_PREFIXE:
        raise ValueError(f"Préfixe trop long : {len(prefixe)} caractères (max {MAX_PREFIXE})")

def compter_stations(noms, prefixe):
    """
    Compte les stations dont le nom commence par le préfixe donné.

    La comparaison ignore la casse ("bercy" correspond à "Bercy").
    Un préfixe vide correspond à toutes les stations.

    Args:
        noms (list[str]): Liste des noms de stations.
        prefixe (str): Préfixe recherché.

    Returns:
        int: Nombre de stations dont le nom commence par le préfixe.

    Exemples:
        >>> compter_stations(["Bercy", "Montparnasse", "Bastille"], "B")
        2
        >>> compter_stations([], "Bercy")
        0
    """
    resultat = 0
    prefixe = prefixe.casefold()
    for nom in noms:
        if nom.casefold().startswith(prefixe):
            resultat += 1
    return resultat


def filtrer_stations(noms, prefixe):
    """
    Renvoie les stations dont le nom commence par le préfixe donné.

    La comparaison ignore la casse, mais les noms sont renvoyés tels
    qu'ils apparaissent dans la liste d'origine, dans le même ordre.
    Un préfixe vide renvoie toutes les stations.

    Args:
        noms (list[str]): Liste des noms de stations.
        prefixe (str): Préfixe recherché.

    Returns:
        list[str]: Nouvelle liste des stations correspondantes
        (vide si aucune ne correspond).

    Exemples:
        >>> filtrer_stations(["BErCy", "Montparnasse", "Gare du Nord"], "bercy")
        ['BErCy']
        >>> filtrer_stations([], "Test")
        []
    """
    prefixe = prefixe.casefold()
    resultats = []
    for nom in noms:
        if nom.casefold().startswith(prefixe):
            resultats.append(nom)
    return resultats