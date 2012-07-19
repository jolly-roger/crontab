import subprocess
import datetime
import tarfile


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"


def tarproject(pName):
    pTar = backupBasedir + pName + "/" + now + ".tar.gz"

    tar = tarfile.open(pTar, "w:gz")
    tar.add(gitBasedir + pName)
    tar.close()


tarproject("auth")
tarproject("crontab")
tarproject("hikesrilanka")
tarproject("hyperload")
tarproject("hyqd")
tarproject("hytcpd")
tarproject("picpuk")
tarproject("ukrainianside")