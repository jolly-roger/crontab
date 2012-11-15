#!/usr/bin/python


import gitbackup
import projects.picpuk as picpuk
import projects.postfix as postfix
import projects.uatrains as uatrains


gitbackup.tarprojects()

pPicpuk = picpuk.Picpuk()
pPicpuk.tarpics()
pPicpuk.tardb()

pPostfix = postfix.Postfix()
pPostfix.tardb()
pPostfix.tarmail()

uatrains.Uatrains()