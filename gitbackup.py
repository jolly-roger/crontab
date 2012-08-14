import subprocess
import datetime
import os
import os.path


import common


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"


def tarproject(pName):
    os.chdir(gitBasedir)
    
    common.makeDir(backupBasedir + pName)
    
    pTar = backupBasedir + pName + "/" + common.now + ".tar.gz"

    common.writeDirToTar(pTar, pName, common.gitUid)
    
def tarprojects():
    tarproject("auth")
    tarproject("crontab")
    tarproject("hikesrilanka")
    tarproject("hyperload")
    tarproject("hyqd")
    tarproject("hytcpd")
    tarproject("picpuk")
    tarproject("ukrainianside")