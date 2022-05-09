cvs = lambda c: ";".join("%s=%s" % (x, y) for x, y in c.items())
cvd = lambda c: dict(map(lambda i: i.split("="), c.replace("; ", ";").split(";")))