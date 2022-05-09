import re

def login(u, s):
	rs = s.get(u+"/profile.php")
	if "mbasic_logout_button" in rs.text:
		return rs