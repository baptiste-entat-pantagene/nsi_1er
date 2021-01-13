# CMakeList.txt : projet CMake pour animationASCII, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

project ("animationASCII")

# Ajoutez une source à l'exécutable de ce projet.
add_executable (animationASCII "animationASCII.cpp" "animationASCII.h" "render.h" "render.cpp")

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
