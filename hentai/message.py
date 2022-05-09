from .action import *

class messages:
	
	def __init__(self, u, s):
		self.u = u
		self.s = s

	def feed(self, endpoint="/messages/"):
		temp = []
		rs = self.s.get(self.u+endpoint)
		if ">Tidak Ada Pesan<" in rs.text:
			exit(" !. tidak ada pesan ditemukan")
		while True:
			try:
				ps = bs(rs.text)
				ms = get_href(ps, href="/messages/read/")
				for i in ms:
					temp.append({"u": i["href"], "n": i.text+"\x1b[0m"})
				print(end=f"\r * mengambil {len(temp)} pesan")
				if not ps.find("span", string="Lihat Pesan Sebelumnya"):
					break
				rs = self.s.get(self.u+get_href(ps, single=True, string="Lihat Pesan Sebelumnya")["href"])
			except:
				break
		if not temp:
			exit("\x1b[0;31m .! gagal mengambil data pesan")
		print("\n"*1)
		return temp

	def delete(self, data):
		try:
			people = data["n"]
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			date, action = get_input(bs(self.s.get(self.u+data["u"]).text), "/messages/action_redirect", "fb_dtsg,jazoest,delete")
			href = get_href(bs(self.s.post(self.u+action, data=date).text), single=True, string="Hapus")["href"]
			return "\x1b[0;37m [*] remove "+people if "messages" in self.s.get(self.u+href).url else "\x1b[0;31m [!] failed to remove "+people
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return "\x1b[0;31m [!] error "+people
			
	def send(self, data):
		try:
			uid = data["u"].split("=")[-1]
			people = data["n"]
			self.s.headers.update({"content-type": "application/x-www-form-urlencoded"})
			date, action = get_input(bs(self.s.get(self.u+data["u"]).text), "/messages/send", "fb_dtsg,jazoest,ids[{uid}],text_ids[{uid}]".format(uid=uid))
			date.update({"body": data["c"], "Send": "Kirim"})
			return "\x1b[0;37m [*] sukses mengirim pesan ke "+people if "send_success" in self.s.post(self.u+action, data=date).url else "\x1b[0;31m [!] gagal mengirim pesan ke "+people
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return "\x1b[0;31m [!] error "+people