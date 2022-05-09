from .action import *
import re

class feed_post:

	def __init__(self, u, s):
		self.u = u
		self.s = s
		self.n = {"th": "Lihat Berita Lain", "tg": "Lihat Postingan Lainnya", "tp": "Tampilkan lainnya"}
	
	def get_post(self, endpoint, next=None, string=None, limit=None):
		temp = []
		temf = []
		rs = self.s.get(self.u+endpoint)
		while True:
			try:
				ps = bs(rs.text)
				href = get_href(ps, string=string)
				for x in href:
					x = "/".join(x["href"].split("/")[3:]) if "/groups/" in x["href"] else x["href"]
					x = x[1:] if x.startswith("/") else x
					if self.sesuaikan("/" + x) not in temf:
						temp.append({"u": "/" + x})
						temf.append(self.sesuaikan("/" + x))
					print(end=f"\r *. mengambil {len(temp)} postingan")
					if len(temp) == limit:
						self.n = "dibuat pada ( 01-05-2022 ) "
						break
				if not ps.find("span", string=self.n[next]):
					break
				rs = self.s.get(self.u+get_href(ps, single=True, string=self.n[next])["href"])
			except:
				break
		if not temp:
			exit(" .! gagal mengambil data postingan")
		print("\n"*1)
		return temp

	def sesuaikan(self, url):
		fbid = re.search("(permalink/\d*/)" if url.startswith("/groups/") else "(fbid=\d*)", url)
		return fbid.group() if fbid else url
		