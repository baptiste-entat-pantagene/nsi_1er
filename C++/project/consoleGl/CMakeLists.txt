# CMakeList.txt : projet CMake pour consoleGl, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

project ("consoleGl")

# Ajoutez une source à l'exécutable de ce projet.
add_executable (consoleGl "consoleGl.cpp" "consoleGl.h" "render.h")

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
