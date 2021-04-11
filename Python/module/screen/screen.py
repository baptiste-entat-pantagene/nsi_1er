def switch(tab_1D, i, j) -> None:
    buff = tab_1D[i]
    tab_1D[i] = tab_1D[j]
    tab_1D[j] = buff

def tri_selection(tab):
    for i in range(len(tab)):
        # Trouver le mini
        mini = i
        for j in range(i + 1, len(tab)):
            if tab[mini] > tab[j]:
                mini = j

        switch(tab, i, mini)
    return tab



if __name__ == "__main__":
    exTab = [98, 22, 15, 32, 2, 74, 63, 70]

    tri_selection(exTab)

    print(exTab)