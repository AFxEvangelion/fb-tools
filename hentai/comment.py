from .action import *
import re

class comment:
	
	def __init__(self, u, s):
		self.u = u
		self.s = s
	
	def send(self, data, owner="", fbid=""):
		try:
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			ps = bs(self.s.get(self.u+data["u"]).text)
			owner = find_owner(ps)
			fbid = re.search("/permalink/(\d+)/" if data["u"].startswith("/groups/") else "fbid=(\d+)", data["u"])
			fbid = (fbid.group(1) if fbid else "") + "\x1b[0m"
			date, action = get_input(ps, "/a/comment.php", "fb_dtsg,jazoest")
			date["comment_text"] = data["c"].replace("<^>", "\n")
			return "\x1b[0;37m [*] sukses berkomentar ke "+owner+fbid if data["c"] in self.s.post(self.u+action, data=date).text else "\x1b[0;31m [!] gagal berkomentar ke "+owner+fbid
		except AttributeError:
			return "\x1b[0;31m [!] error "+fbid
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
			
			