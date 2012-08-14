import datetime
import os
import tarfile


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/"
backupContentDir = backupBasedir + "content/"
backupDatabaseDir = backupBasedir + "database/"
backupMailDir = backupBasedir + 'mail'

mailerUid = 5003
crontabUid = 1004
crontabGid = 5004
wwwUid = 1002
postgresUid = 88
gitUid = 1001


def makeDir(dirName):
    prevUid = os.geteuid()
    os.seteuid(crontabUid)
    
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
        
    os.seteuid(prevUid)

def writeDirToTar(pTar, dirName, rUid):
    prevUid = os.geteuid()
    os.seteuid(crontabUid)
    
    tar = tarfile.open(pTar, "w:gz")
    
    os.seteuid(prevUid)
    
    prevUid = os.geteuid()
    os.seteuid(rUid)
    
    tar.add(dirName)
    
    os.seteuid(prevUid)
    
    tar.close()
