import requests as r
from bs4 import BeautifulSoup

Connection = (r.exceptions.ConnectionError, r.exceptions.ConnectTimeout, r.exceptions.ReadTimeout)
bs = lambda x: BeautifulSoup(x, "html.parser")

def get_input(p, action=True, filter=False, **k):
	p = p.find("form", action = lambda x: action in x)
	a = p.findAll("input", {"name": True, "value": True})
	for x in a:
		k[x["name"]] = x["value"]
	if filter:
		n = {}
		for x in k.items():
			if x[0] in filter.split(","):
				n[x[0]] = x[1]
		k = n
	return k, p["action"]

def get_href(p, href=False, string=False, single=False):
	temp = []
	find = p.findAll("a", href = ((lambda i: href in i) if href else True), string=string)
	if single is True:
		return find[0]
	for x in find:
		temp.append(x)
	return temp

def find_owner(p, owner=""):
	owner = p.find("a", href=lambda i: "__tn__=" in i, class_=False)
	if owner:
		owner = (owner["href"].split("id=")[1].split("&")[0] if owner["href"].startswith("/profile.php?") else owner["href"][1:].split("?")[0].split("/")[0]) + "_"
	return str(owner)

def get_title(p):
	return p.find("title")
		
			