# Les listes
Une liste est un conteneur qui peut contenir n'importe qu'elle type de variable python et il est possible de les mélanger.
**! les cases en mémoire sont numéroté à partir de 0 et non 1. **

**syntaxe:**
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

```python
len(liste) #--> renvoie la longueur de la liste
liste.append(object) #--> Insert un élément à la fin de la liste
liste.insert(position, object) #--> Insert un élément a la position donnée
```

**déclaration de liste  par comprehension**:
Python propose un outil rapide et puisant de génération de listes: la génération par compréhension.

```python
listeBasic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste = [x for x in range(11)]
#output--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Dans cet exemple on crée une liste de façon basique, puis la même par compréhension.
La génération par compréhension permet donc de générer de grandes listes liste rapidement, exemple:
```python
liste = [x for x in range(500)]
#génère une liste comme la précédente mais jusqu'à 500
```
il est possible re jouter des conditions pour avoir des listes plus pousser, exemple:
Remplie le tableau de 0 à 10 et seulement si les valeurs sont paires
```python
listeDeNbPair = [x for x in range(0, 11) if x%2==0]
#output--> [0, 2, 4, 6, 8, 10]
```

**Les listes de listes ou multidimensionnelles**:
**syntaxe:**
```python
liste2D = [ [ ], [ ] ]
liste3D = [ [ ], [ ], [ ] ]
```
Faire de liste de listes revient à créer un tableau ou une matrice, ces nouveaux objets se comportent comme des listes classiques.
```python
tableau = [[0, 1, 2], [3, 4, 5]]
matrice = [[0, 2], [3, 4], [5, 6]]
```