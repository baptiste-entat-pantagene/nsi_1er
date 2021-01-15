// animationASCII.h : fichier Include pour les fichiers Include système standard,
// ou les fichiers Include spécifiques aux projets.

#pragma once

#include <iostream>
#include <string>
#include <thread>         // std::this_thread::sleep_for
#include <chrono>         // std::chrono::seconds

// TODO: Référencez ici les en-têtes supplémentaires nécessaires à votre programme.
#include "Render.h"


void addToRender(std::string  render[10][10], std::string  obj[4][3], int x, int y);
void clearRender(std::string  render[10][10]);
void extractRender(std::string& buff, std::string  render[10][10]);