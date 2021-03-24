"""
Entat Baptiste
exo 140 p 151
"""


def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp


def tri_par_selection(t):

    for i in range(len(t) - 1):
        #print(t) #debug fx
        m = i
        for j in range(i + 1, len(t)):
            if t[j] < t[m]:
                m = j
        echange(t, i, m)

tab = [5, 7, 6, 9, 0, 4, 1, 8, 2, 3]
tri_par_selection(tab)
print("->", tab)
