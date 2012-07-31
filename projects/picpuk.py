import tarfile
import os
import os.path


import common
import projects.base


class Picpuk(projects.base.Base):
    def __init__(self):
        self.wwwBasedir = "/home/www/"
        self.pName = "picpuk"
    
    def tarpics(self):
        os.chdir(self.wwwBasedir + self.pName)
        
        if not os.path.isdir(common.backupContentDir + self.pName):
            os.mkdir(common.backupContentDir + self.pName)
        
        pTar = common.backupContentDir + self.pName + "/pics_" + common.now + ".tar.gz"
    
        tar = tarfile.open(pTar, "w:gz")
        tar.add("pics")
        tar.close()