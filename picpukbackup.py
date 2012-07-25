import subprocess
import datetime
import tarfile
import os
import os.path


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/content/"
picpukBasedir = "/home/www/"
pName = "picpuk"


def tarpics():
    os.chdir(picpukBasedir + pName)
    
    if not os.path.isdir(backupBasedir + pName):
        os.mkdir(backupBasedir + pName)
    
    pTar = backupBasedir + pName + "/pics_" + now + ".tar.gz"

    tar = tarfile.open(pTar, "w:gz")
    tar.add("pics")
    tar.close()