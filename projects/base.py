import subprocess
import tarfile
import os
import os.path


import common


class Base(object):
    def tardb(self):
        if not os.path.isdir(common.backupDatabaseDir + self.pName):
            os.mkdir(common.backupDatabaseDir + self.pName)
        
        pBackup = common.backupDatabaseDir + self.pName + "/" + self.pName + ".backup"
        
        subprocess.call("pg_dump -U postgres " + self.pName + " > " + pBackup, shell=True)    
        
        pTar = common.backupDatabaseDir + self.pName + "/" + common.now + ".tar.gz"
        
        tar = tarfile.open(pTar, "w:gz")
        tar.add(pBackup)
        tar.close()
        
        os.remove(pBackup)