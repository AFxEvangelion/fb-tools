from .action import *

class groups:

	def __init__(self, u, s):
		self.u = u
		self.s = s

	def feed(self, s, t):
		data = []
		s.headers.update({"Host": "graph.facebook.com", "accept": "application/json, text/plain, */*", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "origin": "https://www.facebook.com", "referer": "https://www.facebook.com"})
		rs = s.get("https://graph.facebook.com/me/groups/?limit=99999&access_token="+t).json()
		for i in rs["data"]:
			data.append({"u": "/group/leave/?group_id="+i["id"], "n": i["name"], "p": i["privacy"]})
		print("")
		return data
	
	def leave(self, data):
		try:
			group_name = data["n"]
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			ps = bs(self.s.get(self.u+data["u"]).text)
			date, action = get_input(ps, "/a/group/leave/")
			return ("\x1b[0;37m [*] berhasil keluar dari grup " if  bs(self.s.post(self.u+action, data=date).text).find("input", {"value": "Gabung ke Grup"}) else "\x1b[0;31m [!] gagal keluar dari grup ") + group_name + "\x1b[0m"
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return "\x1b[0;31m [!] error "+group_name+"\x1b[0m"
