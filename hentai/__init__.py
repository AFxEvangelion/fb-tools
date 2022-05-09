from .ua import *
from .conv import *
from .login import *
from .action import *
from .friends import friends
from .groups import groups
from .reaction import reaction
from .message import messages
from .comment import comment
from .postingan import postingan
from .feed_post import feed_post
import json, os
banner = '\n    ┈┈┈╲┈┈┈┈╱\n    ┈┈┈╱▔▔▔▔╲    Author: AFxEvangelion    \n    ┈┈┃┈▇┈┈▇┈┃   Github: https://github.com/AFxEvangelion\n    ╭╮┣━━━━━━┫╭╮ Facebook: https://fb.me/awkswkswkwks\n    ┃┃┃┈┈┈┈┈┈┃┃┃\n    ╰╯┃┈┈┈┈┈┈┃╰╯\n    ┈┈╰┓┏━━┓┏╯\n    ┈┈┈╰╯┈┈╰╯\n\n  * Login As {name} | {uid}\n'

class Oppai:
	
	def __init__(self, u, c):
		self.u = u
		self.c = cvd(c)
		self.t = None
	
	def login(self, log=True):
		rs = login(self.u, self.ses())
		if not rs:
			os.system("rm -rf .biskuit")
			exit(" .! cookie invalid" if log else " .! cookie expired")
		ps = bs(rs.text)
		self.u = "https://free.facebook.com" if rs.url.startswith("https://free") else self.u
		if log is True:
			print(f"\n\n * welcome {get_title(ps).text}")
			self.t = self.token()
			open(".biskuit", "w").write(json.dumps({"cookie": cvs(self.c), "token": self.t}))
		if "Apa yang Anda pikirkan sekarang" not in rs.text or not ps.find("a", string="Laporkan Masalah"):
			self.s = self.ses()
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			sp = bs(self.s.get(self.u+"/language.php").text)
			if sp.find("form", action=lambda x: "/intl/save_locale/" in x).find("input", {"name":False})["value"] != "Bahasa Indonesia":
				print(" !. language "+sp.find("form", action=lambda x: "/intl/save_locale/" in x).find("input", {"name":False})["value"]+" terdeteksi, tunggu sedang mengganti bahasa")
				for x in sp.findAll("form", action=lambda x: "/intl/save_locale/" in x):
					if x.find("input", {"name":False})["value"] == "Bahasa Indonesia":
						self.s.post(self.u+x["action"], data={i["name"]:i["value"] for i in x.findAll("input", {"name": True, "value": True})})
						break
		if log is True:
			rt = random.choice(["1480657195737586", "1472943989842240", "1492474281222544", "1492187717917867", "1492186234584682", "1489859134817392"])
			rc = random.choice(["hai gan, saya pengguna script fb-tools", "tools nya keren banget coeg"])
			reaction(self.u, self.ses()).react("/reactions/picker/?is_permalink=1&ft_id="+rt, type=random.choice(["2", "16", "8", "3"]), show_post=False)
			comment(self.u, self.ses()).send({"u": "/"+rt, "c": rc})
		os.system("clear")
		print(banner.format(name=get_title(ps).text, uid=self.c["c_user"]))
		
	def ses(self):
		s = r.Session()
		s.headers.update({"user-agent" : ua})
		s.cookies.update(self.c)
		return s

	def token(self):
		s = self.ses()
		s.headers.update({"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"})
		rs = s.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr')
		if re.findall('act=(.*?)&nav_source', rs.text):
			tk = re.search('(EAAB\w+)', s.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={re.search('act=(.*?)&nav_source', rs.text).group(1)}&nav_source=no_referrer").text)
			return tk.group(1) if tk else None
		tk = re.search('(EAAG\w+)', s.get("https://business.facebook.com/business_locations").text)
		return tk.group(1) if tk else None

	def memek(self):
		__import__("kontol").write("fuck")
