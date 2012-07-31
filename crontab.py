import gitbackup
import projects.picpuk as picpuk
import projects.postfix as postfix


gitbackup.tarprojects()

pPicpuk = picpuk.Picpuc()
pPicpuk.tarpics()
pPicpuk.tardb()

pPostfix = postfix.Postfix()
pPostfix.tardb()