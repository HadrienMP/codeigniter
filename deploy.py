#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: deploy.py

import sys
import re

if len(sys.argv) != 2:
	print "Ce script a besoin du chemin codeigniter en paramètre"
	sys.exit()

print "Analyse des paramètres"
path = sys.argv[1]
print "Chemin trouvé : " + path
path = re.sub(r'/cygdrive/(\w)/', r"\1:/", path)
print "Chemin modifié : " + path

# Lecture du fichier
print "Ouverture du fichier htdocs/index.php pour modification"
path_file = 'htdocs/index.php'
f = open(path_file,'r')
index_php = f.read()
f.close()

index_php = re.sub(r"(application_folder|system_path) = '.*(application|system)'", r"\1 = '" + path + r"/\2'", index_php)

# Réécriture dans le fichier
f = open(path_file,'w')
f.write(index_php)
f.close()

print "Fin de la modification du fichier htdocs/index.php"