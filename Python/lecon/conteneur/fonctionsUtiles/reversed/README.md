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
Depuis python 3 l'interpréteur ne fait plus une copie de l'objet à itérer, la fonction créer avec l'objet de base un nouvel itérateur. Ce qui fait que la liste n'est plus véritablement une liste puisque son type à changer.
```python
print(reversed(listeEnVrac)) #output --> <list_reverseiterator object at 0x000001D2F41CA070>
```
Ainsi en pratique, faire ce print ne fonctionne pas puisque la liste n'est plus de types `list` mais `list_reverseiterator`

Pour corriger ce potentiel problème il faut convertir cet objet:
```python
print(list(reversed(liste))) #output --> [5, 4, 1, 4, 3]
```
llist() --> convertie `list_reverseiterator` en `list`

------------
Liste des itérateurs qu'il peut prendre:
- list
- range
- string
- tuple

