import subprocess
import tarfile
import os
import os.path


import common


class Base(object):
    def tardb(self):
        if not os.path.isdir(common.backupDatabaseDir + self.pName):
            os.mkdir(common.backupDatabaseDir + self.pName)
        
        pBackupDir = common.backupDatabaseDir + self.pName + "/"
        pBackupName =  self.pName + ".backup"
        
        subprocess.call("pg_dump -U postgres " + self.pName + " > " + pBackupDir + pBackupName, shell=True)    
        
        pTar = common.backupDatabaseDir + self.pName + "/" + common.now + ".tar.gz"
        
        os.chdir(pBackupDir)
        
        tar = tarfile.open(pTar, "w:gz")
        tar.add(pBackupName)
        tar.close()
        
        os.remove(pBackupName)