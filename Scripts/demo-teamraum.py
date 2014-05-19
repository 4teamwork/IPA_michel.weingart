# -*- coding: utf-8 -*-

import git #Damit die Pakete von github geklont werden können
import os  #Bibliothek um z.B konsolebefehle übergeben zu können

RUNSCRIPT = "script"
REPOURL = 'git@git.4teamwork.ch:egov/buildout-base.git'
DIRNAME = "ordner"

def printstars(toprint): #Um wichtige Abschnitte im Quellcode zu markieren
    print "*" * 20
    print toprint
    print "*" * 20
    
#Schleife um zu prüfen ob der Ordner schon existiert.
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)
    print "Folder with name '%s'" % DIRNAME
else:
    print "Folder allready exists: '%s'" % DIRNAME
    sys.exit()

print "We are currently in %s " % os.getcwd()
os.chdir(DIRNAME)
print "We are currently in %s " % os.getcwd()

#Repository klonen nach hier
repo = git.Git()
repo.clone(REPOURL, '.') 




#Dem Skript müssen Optionen mitgegeben werden können(python-pfad)


    
    
    
