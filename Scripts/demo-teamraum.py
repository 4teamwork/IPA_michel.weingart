# -*- coding: utf-8 -*-

import git #Damit die Pakete von github geklont werden können
import os  #Bibliothek um z.B konsolebefehle übergeben zu können Operating System
import sys #Bibliothek um Interpreter Python ansprechen zu können z.B maximale Rekursionstiefe

RUNSCRIPT = "script"
REPOURL = 'git@git.4teamwork.ch:egov/buildout-base.git'
DIRNAME = "ordner"
PYTHONPATH = "/Users/mischu/Plone/python/python-2.7/bin/python2.7"

def printstars(toprint): #Um wichtige Abschnitte im Quellcode zu markieren
    print "*" * 20
    print toprint
    print "*" * 20
     
#Schleife um zu prüfen ob die Instanz schon existiert.
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)
    print "Folder with name '%s'" % DIRNAME
else:
    print "Folder allready exists: '%s'" % DIRNAME
    sys.exit() #Um den Python-Interpreter zu verlassen

#Repository klonen nach hier    
os.chdir(DIRNAME)

#Repository klonen nach hier
repo = git.Git()
repo.clone(REPOURL, '.') 

#Wichtiger Abschnitt, Symlink auf development.cfg erstellen
printstars("Create Symlink")
os.system('ln -s development-ipa.cfg buildout.cfg')
printstars("Created buildout.cfg Symlink to development.cfg")

#Wichtiger Abschnitt, Bootstrap ausführen
printstars("Start bootstrap")
os.system(PYTHONPATH + " bootstrap.py")
printstars("End bootstrap")

printstars("Start buildout")
os.system("bin/buildout ")
printstars("End buildout")

#exisitieren Hauptelemente in der neuen Instanz?
foldercontents = os.listdir('.')
for foldername in ['bin', 'parts', 'buildout.cfg']:
    if foldername not in foldercontents:
        raise Exception('missing:' +foldername)
        
printstars("Starting instance")
os.system('bin/instance1 start')
        


#Dem Skript müssen Optionen mitgegeben werden können(Instanzenpfad)
#Dem Skript müssen Optionen mitgegeben werden können(python-pfad)


    
    
    
