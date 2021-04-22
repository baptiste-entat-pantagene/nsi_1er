# CMakeList.txt : projet CMake pour gestionVehicules, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)

project ("gestionVehicules")

# Ajoutez une source à l'exécutable de ce projet.
add_executable (gestionVehicules "gestionVehicules.cpp" "gestionVehicules.h" "Vehicule.h" "Vehicule.cpp")

# TODO: Ajoutez des tests et installez des cibles si nécessaire.
#
#include(CTest)
#enable_testing()
#
#add_test(usage_test test)
#set_tests_properties(usage_test PROPERTIES WILL_FAIL False)
#
