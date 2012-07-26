import subprocess
import datetime
import tarfile
import os
import os.path


import common


wwwBasedir = "/home/www/"
pName = "picpuk"


def tarpics():
    os.chdir(wwwBasedir + pName)
    
    if not os.path.isdir(common.backupContentDir + pName):
        os.mkdir(common.backupContentDir + pName)
    
    pTar = common.backupContentDir + pName + "/pics_" + common.now + ".tar.gz"

    tar = tarfile.open(pTar, "w:gz")
    tar.add("pics")
    tar.close()
    
def tardb():
    if not os.path.isdir(common.backupDatabaseDir + pName):
        os.mkdir(common.backupDatabaseDir + pName)
    
    pBackup = common.backupDatabaseDir + pName + "/picpuk.backup"
    
    subprocess.call("pg_dump -U postgres picpuk > " + pBackup, shell=True)    
    
    pTar = common.backupDatabaseDir + pName + "/" + common.now + ".tar.gz"
    
    tar = tarfile.open(pTar, "w:gz")
    tar.add(pBackup)
    tar.close()
    
    os.remove(pBackup)