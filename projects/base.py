import subprocess
import os
import os.path


import common


class Base(object):
    def tardb(self):
        common.makeDir(common.backupDatabaseDir + self.pName)
        
        pBackupDir = common.backupDatabaseDir + self.pName + "/"
        pBackupName =  self.pName + ".backup"
        
        subprocess.call("pg_dump -U postgres " + self.pName + " > " + pBackupDir + pBackupName, shell=True)    
        
        pTar = common.backupDatabaseDir + self.pName + "/" + common.now + ".tar.gz"
        
        os.chdir(pBackupDir)
        
        common.writeDirToTar(pTar, pBackupName, common.postgresUid)
        
        os.remove(pBackupName)