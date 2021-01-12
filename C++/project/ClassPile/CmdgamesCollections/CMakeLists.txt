# CMakeList.txt : projet CMake pour CmdgamesCollections, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

project ("CmdgamesCollections")

# Ajoutez une source à l'exécutable de ce projet.
add_executable (CmdgamesCollections "CmdgamesCollections.cpp" "CmdgamesCollections.h" "regulars.cpp" "regulars.h" "plusMoins.h" "plusMoins.cpp")

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
