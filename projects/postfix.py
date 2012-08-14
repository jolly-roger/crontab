import os


import common
import projects.base


class Postfix(projects.base.Base):
    def __init__(self):
        self.pName = "postfix"
        self.mailBasedir = '/home'
        
    def tarmail(self):
        os.chdir(self.mailBasedir)
        
        pTar = common.backupMailDir + "/" + common.now + ".tar.gz"
    
        common.writeDirToTar(pTar, 'mailer', common.mailerUid)