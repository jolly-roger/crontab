import subprocess
import datetime


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"

# ukrainianside
subprocess.call("tar cvf " + backupBasedir + "ukrainianside/" + now + ".tar " + gitBasedir + "ukrainianside/*", shell=True)
subprocess.call("gzip -9 " + backupBasedir + "ukrainianside/" + now + ".tar", shell=True)
#subprocess.call("rm " + backupBasedir + "ukrainianside/" + now + ".tar", shell=True)
