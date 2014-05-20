# -*- coding: utf-8 -*-

import git #Damit die Pakete von github geklont werden können
import os  #Bibliothek um z.B konsolebefehle übergeben zu können Operating System
import sys #Bibliothek um Interpreter Python ansprechen zu können z.B maximale Rekursionstiefe
from optparse import OptionParser #Dem Skript können Optionen mitgegeben werden
parser = OptionParser() #OptionParser wird instanziiert

RUNSCRIPT = "script"
REPOURL = 'git@git.4teamwork.ch:egov/buildout-base.git'
DIRNAME = "demo-teamraum"
#PYTHONPATH = "/Users/mischu/Plone/python/python-2.7/bin/python2.7"

def printstars(toprint): #Um wichtige Abschnitte im Quellcode zu markieren
    print "*" * 20
    print toprint
    print "*" * 20

#  sys.executable -> Das Python mit welchem ich aktuell das Script starte wird genommen.              
parser.set_defaults(pythonpath=sys.executable)

#Option um den Python-Pfad angeben zu können wird hinzugefüt -> -p = python-path dest = unter welchem Namen der Wert er Option später im Programm verfügbar gemacht werden soll.
parser.add_option("-p", dest="pythonpath", help="If you dont set a path to the python, it will take the system python" )


#Optionen und Argumente werden hier geparset
options, args = parser.parse_args()

#Pfad des Pythons wird dem OptionParser entnommen
PYTHONPATH = options.pythonpath 

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



    
    
    
