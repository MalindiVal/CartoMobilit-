# CartoMobilité

## Fonctionnalités

Fonctions disponibles dans `src/catalogue.py`.

### `compter_stations(noms, prefixe)`

Compte les stations dont le nom commence par le préfixe donné.

Le nombre de station maximal est de 150 stations

La taille maximal des préfixes est de 255

| Paramètre | Type | Description |
|---|---|---|
| `noms` | `list[str]` | Liste des noms de stations |
| `prefixe` | `str` | Préfixe recherché |

**Retour :** `int`, le nombre de stations correspondantes.

```python
compter_stations(["Bercy", "Montparnasse", "Bastille"], "B")  # 2
```

### `filtrer_stations(noms, prefixe)`

Renvoie les stations dont le nom commence par le préfixe donné.

Le nombre de station maximal est de 150 stations

La taille maximal des préfixes est de 255

| Paramètre | Type | Description |
|---|---|---|
| `noms` | `list[str]` | Liste des noms de stations |
| `prefixe` | `str` | Préfixe recherché |

**Retour :** `list[str]`, les stations correspondantes, dans l'ordre d'origine.

```python
filtrer_stations(["BErCy", "Montparnasse", "Gare du Nord"], "bercy")  # ['BErCy']
```

### Comportement commun

- La comparaison **ignore la casse** (`"bercy"` correspond à `"Bercy"`).
- Un préfixe vide (`""`) correspond à toutes les stations.
- Une liste vide renvoie `0` ou `[]`.

## Tests

```bash
python -m tests.test_functions
```