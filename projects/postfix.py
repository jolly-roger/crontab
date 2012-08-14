import os
import tarfile


import common
import projects.base


class Postfix(projects.base.Base):
    def __init__(self):
        self.pName = "postfix"
        self.mailBasedir = '/home'
        
    def tarmail(self):
        #prevUid = os.geteuid()
        #os.seteuid(common.mailerUid)
        
        os.chdir(self.mailBasedir)
        
        pTar = common.backupMailDir + "/" + common.now + ".tar.gz"
    
        common.writeDirToTar(pTar, 'mailer', common.mailerUid)
        
        #os.seteuid(prevUid)