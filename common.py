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


def writeDirToTar(pTar, dirName, rUid):
    #prevGids = os.getresgid()
    #prevUids = os.getresuid()
    #
    #os.setresgid(prevGids[0], crontabGid, crontabGid)
    #os.setresuid(prevUids[0], crontabUid, crontabUid)
    
    prevUid = os.geteuid()
    os.seteuid(crontabUid)
    
    tar = tarfile.open(pTar, "w:gz")
    
    os.seteuid(prevUid)
    
    prevUid = os.seteuid(rUid)
    os.seteuid()
    
    tar.add(dirName)
    
    os.seteuid(prevUid)
    
    tar.close()
    
    
    
    #os.setresgid(*prevGids)
    #os.setresuid(*prevUids)
