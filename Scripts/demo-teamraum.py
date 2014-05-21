# -*- coding: utf-8 -*-

# Damit die Pakete von github geklont werden können
import git
# Bibliothek um z.B konsolebefehle übergeben zu können Operating System
import os
# Bibliothek um Interpreter Python ansprechen zu können z.B
# maximale Rekursionstiefe

import sys
# Dem Skript können Optionen und Argumente mitgegeben werden
from optparse import OptionParser

# Das Paket buildout-base erhält die Konstante REPOURL
REPOURL = 'git@git.4teamwork.ch:egov/buildout-base.git'


# Um wichtige Abschnitte im Quellcode zu markieren
def printstars(toprint):
    print "*" * 20
    print toprint
    print "*" * 20

# OptionParser wird instanziiert
parser = OptionParser()

# sys.executable -> Das Python mit welchem ich aktuell das
# Script starte wird genommen.
parser.set_defaults(pythonpath=sys.executable)

# Option, um den Python-Pfad angeben zu können, wird hinzugefüt
# -> -p = python-path dest = unter welchem Namen der Wert er
# Option später im Programm verfügbar gemacht werden soll.
parser.add_option("-p", dest="pythonpath",
                  help="If you dont set a path to the python,"
                  " it will take the system python")

# Optionen und Argumente werden hier geparset
options, args = parser.parse_args()

# Benötige 1 Argument sonst
if len(args) != 1:
    parser.print_usage()
    print "ERROR: You must give me a target directory"
    sys.exit()

# Argument wird din Konstante DIRNAME gespeichert
DIRNAME = args[0]

# Pfad des Pythons wird dem OptionParser entnommen
PYTHONPATH = options.pythonpath

# Schleife um zu prüfen ob die Instanz schon existiert.
if not os.path.exists(DIRNAME):
    os.makedirs(DIRNAME)
    print "Folder with name '%s'" % DIRNAME
else:
    print "Folder already exists: '%s'" % DIRNAME
    # Um den Python-Interpreter zu verlassen
    sys.exit()

# Repository klonen nach hier
os.chdir(DIRNAME)

# Repository klonen nach hier
repo = git.Git()
repo.clone(REPOURL, '.')

# Branch von buildout-base wird ausgecheckt und verwendet
print "Cloned %s" % REPOURL
repo.checkout("mw-ipa_runscript")

# Wichtiger Abschnitt, Symlink auf development.cfg erstellen
printstars("Create Symlink")
os.system('ln -s development.cfg buildout.cfg')
printstars("Created buildout.cfg Symlink to development.cfg")

# Wichtiger Abschnitt, Bootstrap ausführen
printstars("Start bootstrap")
os.system(PYTHONPATH + " bootstrap.py")
printstars("End bootstrap")

printstars("Start buildout")
os.system("bin/buildout ")
printstars("End buildout")

# exisitieren Hauptelemente in der neuen Instanz?
foldercontents = os.listdir('.')
for foldername in ['bin', 'parts', 'buildout.cfg']:
    if foldername not in foldercontents:
        raise Exception('missing:' + foldername)

printstars("Starting instance")
os.system('bin/instance1 start')
