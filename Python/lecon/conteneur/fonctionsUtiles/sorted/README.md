# Sorted
Python propose des outil intégré de tri, notamment avec "sorted"
```python
sorted(iterable, key=None, reverse=False)
```
iterable correspond à la liste, set ou autres
key est optionnel --> Permets
reverse et optionnel --> Permets de faire un tri inverse

------------
exemple avec les **listes**:
```python
listeSorted = sorted(listeEnVrac)
```
- Elle alors triée du plus petit au plus grand nombre ou par ordre alphabétique si la liste est de type string.

**Remarque:**
Sorted ne remplace pas la liste préexistante mais en créer une nouvelle, donc juste:
```python
sorted(listeEnVrac)
```
Ne fait rien, ne remplace pas l'ancienne liste.

------------
Liste des itérateurs qu'il peut prendre:
- list
- set
- ???
