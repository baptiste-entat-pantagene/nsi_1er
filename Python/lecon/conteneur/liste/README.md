# Les listes
Une liste est un conteneur qui peut contenir n'importe qu'elle type de variable python et il est possible de les mélanger.

**syntaxce:**
```python
liste = []
#--> liste vide
liste = [1, 3, "cafet"]
``` 

```python
variableGet = liste [0]
print(liste [0])
#--> Récupère la valeur stockée dans la première case préciser entre les crochets
``` 

**! les cases en mémoire sont numéroté à partir de 0 et non 1. **


**declaration de liste  par comprehension**:
listeDeNbPair = [x for x in range(0, 11) if x%2==0] #Remplie le tableau de 0 à 10 et seulement si les valeurs sont paires


**liste multidimensionnel**:
tableau = [[0, 1, 2], [3, 4, 5]]
matrice = [[0, 2], [3, 4], [5, 6]]