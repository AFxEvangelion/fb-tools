from .action import *
import re

class friends:

	def __init__(self, u, s):
		self.u = u
		self.s = s

	def hovercard(self, html):
			return get_href(html, href="/friends/hovercard/mbasic/")
	
	def request(self, endpoint, string):
		ps = bs(self.s.get(self.u+endpoint).text)
		span, div = string.split("|")
		while True:
			hv = self.hovercard(ps)
			hx = get_href(ps, string=span)
			for x in range(len(hx)):
				vs = bs(self.s.get(self.u+hx[x]["href"]).text)
				vs = " berhasil" if vs.find("div", string=div) else " gagal"
				vs = hv[x].text+vs+div[10:] + "\x1b[0m"
				cr = "\x1b[0;37m [*] " if "berhasil di" in vs else "\x1b[0;31m [!] "
				print(cr+"permintaan pertemanan "+vs)
			if not ps.find("span", string="Lihat selengkapnya"):
				break
			ps = bs(self.s.get(self.u+endpoint).text)
		
	def revblo(self, endpoint, aksi):
		try:
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			ps = bs(self.s.get(self.u+endpoint).text)
			ttt = "memutus ikatan dengan " if aksi == "Konfirmasi" else "memblokir "
			rrt = "Anda tidak lagi berteman dengan" if aksi == "Konfirmasi" else "unblock_id="+re.search("bid=(\d+)", endpoint).group(1)
			date, action = get_input(ps, "/a/friends/remove/" if aksi == "Konfirmasi" else "/privacy/touch/block/id/", "fb_dtsg,jazoest")
			date["confirm" if aksi == "Konfirmasi" else "confirmed"] = aksi
			return "\x1b[0;37m [*] berhasil "+ttt if rrt in self.s.post(self.u+action, data=date).text else "\x1b[0;31m [!] gagal "+ttt
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			if "Anda dilarang menggunakan fitur ini untuk sementara." in str(ps):
				exit("\x1b[0;31m [!] limit, silahkan tunggu beberapa saat\x1b[0m")
			return "\x1b[0;31m [!] error "

	def start(self, endpoint, aksi):
		ps = bs(self.s.get(self.u+"/friends/center/friends/").text)
		while True:
			hv = self.hovercard(ps)
			for x in hv:
				rs = self.revblo(endpoint+re.search("uid=(\d+)", x["href"]).group(1), aksi)
				print(rs+x.text+"\x1b[0m")
			if not ps.find("span", string="Lihat selengkapnya"):
				break
			ps = bs(self.s.get(self.u+"/friends/center/friends/").text)
