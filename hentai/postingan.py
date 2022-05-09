from .action import *
import re

class postingan:
	
	def __init__(self, u, s):
		self.u = u
		self.s = s

	def remunt(self, endpoint):
		try:
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			ps = bs(self.s.get(self.u+endpoint).text)
			fbid = "".join(re.findall("level_post_id\.(\d+)", endpoint))
			action_key = "UNTAG" if ps.find("span", string="Hapus tanda") else "DELETE"
			date, action = get_input(ps, "/nfx/basic/handle_action/", "fb_dtsg,jazoest,submit")
			date["action_key"] = action_key
			return ("\x1b[0;37m [*] berhasil meng" if not re.search("level_post_id\."+fbid, self.s.post(self.u+action, data=date).text) else "\x1b[0;31m [!] gagal meng") + " ".join([" ".join(["hapus" if action_key == "DELETE" else action_key.lower(), "postingan"]), fbid, "\x1b[0m"])
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return "\x1b[0;31m [!] error "+fbid+"\x1b[0m"
			
	def rempho(self, endpoint):
		try:
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			ps = bs(self.s.get(self.u+endpoint).text)
			fbid = endpoint.split("=")[1].split("&")[0]
			date, action = get_input(ps, "/a/photo.php")
			return ("\x1b[0;37m [*] berhasil meng" if "/albums/" in self.s.post(self.u+action, data=date).url else "\x1b[0;31m [!] gagal meng") + " ".join(["hapus photo", fbid, "\x1b[0m"])
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return "\x1b[0;31m [!] error "+fbid+"\x1b[0m"

	def start(self, endpoint):
		ps = bs(self.s.get(self.u+endpoint).text)
		while True:
			blacklist = []
			nfx = re.findall('href="(/nfx/basic/direct_actions/\?.*?)"', str(ps))
			fto = [x["href"].split("photo.php?")[1].split("&") for x in ps.findAll("a", string="Berita Lengkap") if x["href"].startswith("/photo.php")]
			for x in range(len(fto)):
				if fto[x][1].split("=")[1] == self.s.cookies["c_user"]:
					print(self.rempho("/photo.php?" + "&".join(fto[x][:2]) + "&delete="))
				else:
					blacklist.append(fto[x])
			for x in range(len(blacklist)):
				fto.remove(blacklist[x])
			fti = [x[0].split("=")[1] for x in fto]
			for x in nfx:
				if "".join(re.findall("level_post_id\.(\d+)", x)) not in fti:
					print(self.remunt(x.replace("&amp;", "&")))
			if not ps.find("span", string="Lihat Berita Lain"):
				break
			ps = bs(self.s.get(self.u+endpoint).text)

#fto = [x["href"].split("=")[1].split("&")[0] for x in ps.findAll("a", string="Berita Lengkap") if x["href"].startswith("/photo.php")]
#print(self.rempho("/photo.php?" + "&".join(b+"="+c for b,c in dict(fbid=x, id=self.s.cookies["c_user"], delete="").items())))
