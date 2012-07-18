import subprocess
import datetime


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"


tarproject("auth")
tarproject("crontab")
tarproject("hikesrilanka")
tarproject("hyperload")
tarproject("hyqd")
tarproject("hytcpd")
tarproject("picpuk")
tarproject("ukrainianside")


def tarproject(pName):
    pTar = backupBasedir + pName + "/" + now + ".tar"
    
    subprocess.call("tar cvf " + pTar + " " + gitBasedir + pName + "/*", shell=True)
    subprocess.call("gzip -9 " + pTar, shell=True)