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
        #prevUid = os.geteuid()
        #os.seteuid(common.wwwUid)
        
        os.chdir(self.wwwBasedir + self.pName)
        
        if not os.path.isdir(common.backupContentDir + self.pName):
            os.mkdir(common.backupContentDir + self.pName)
        
        pTar = common.backupContentDir + self.pName + "/pics_" + common.now + ".tar.gz"
    
        common.writeDirToTar(pTar, 'pics', common.wwwUid)
        
        #os.seteuid(prevUid)