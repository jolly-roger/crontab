import subprocess
import datetime


now = datetime.datetime.now().strftime("%Y-%m-%d")
backupBasedir = "/mnt/backup/git/"
gitBasedir = "/home/git/"

# ukrainianside
usTar = backupBasedir + "ukrainianside/" + now + ".tar"

subprocess.call("tar cvf " + usTar + " " + gitBasedir + "ukrainianside/*", shell=True)
subprocess.call("gzip -9 " + usTar, shell=True)

