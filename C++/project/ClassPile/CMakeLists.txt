# CMakeList.txt : projet CMake pour ClassPile, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

project ("ClassPile")

# Ajoutez une source à l'exécutable de ce projet.
add_executable (ClassPile "main.cpp" "main.h" "Pile.h" "Pile.cpp" "CmdInteract.h" "CmdInteract.cpp")

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
