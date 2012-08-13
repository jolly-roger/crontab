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


def writeDirToTar(pTar, dirName):
    #prevGids = os.getresgid()
    #prevUids = os.getresuid()
    #
    #os.setresgid(prevGids[0], prevGids[1], crontabGid)
    #os.setresuid(prevUids[0], prevUids[1], crontabUid)
    
    tar = tarfile.open(pTar, "w:gz")
    tar.add(dirName)
    tar.close()
    
    #os.setresgid(*prevGids)
    #os.setresuid(*prevUids)
