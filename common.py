import datetime


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/"
backupContentDir = backupBasedir + "content/"
backupDatabaseDir = backupBasedir + "database/"
backupMailDir = backupBasedir + 'mail'

mailerUid = 5003
mailerGid = 5003
