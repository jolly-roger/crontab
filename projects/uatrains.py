import urllib.request


import projects.base


class Uatrains(projects.base.Base):
    def __init__(self):
        urllib.request.urlopen('http://localhost:18050')