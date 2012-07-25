import subprocess
import datetime
import tarfile
import os
import os.path


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"


def tarproject(pName):
    os.chdir(gitBasedir)
    
    if not os.path.isdir(backupBasedir + pName):
        os.mkdir(backupBasedir + pName)
    
    pTar = backupBasedir + pName + "/" + now + ".tar.gz"

    tar = tarfile.open(pTar, "w:gz")
    tar.add(pName)
    tar.close()
    
def tarprojects():
    tarproject("auth")
    tarproject("crontab")
    tarproject("hikesrilanka")
    tarproject("hyperload")
    tarproject("hyqd")
    tarproject("hytcpd")
    tarproject("picpuk")
    tarproject("ukrainianside")