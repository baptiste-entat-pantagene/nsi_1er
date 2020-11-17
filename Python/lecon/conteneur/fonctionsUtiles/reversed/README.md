# Reversed

Python propose une fonction qui permet de renvoyer l'itérateur dans son ordre inverse avec "reversed":
```python
reversed(sequence)
```
**remarque:**
- doit être une séquence comme une liste, pas un tableau.

------------
## exemple avec les **listes**:
```python
listeReversed = reversed(listeEnVrac)
```
- L'ordre des éléments de la liste sont alors inversés.

**Remarque:**
reversed ne remplace pas la liste préexistante mais en créer une nouvelle, donc juste:
```python
reversed(listeEnVrac)
```
Ne fait rien, ne remplace pas l'ancienne liste.

------------
Liste des itérateurs qu'il peut prendre:
- list
- set
- ???

