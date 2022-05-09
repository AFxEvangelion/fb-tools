from .action import *
import re

class reaction:
	
	def __init__(self, u, s):
		self.u = u
		self.s = s
		self.rt = {"1": "Suka", "2": "Super", "16": "Peduli", "4": "Haha", "3": "Wow", "7": "Sedih", "8": "Marah"}
	
	def react(self, endpoint, owner="", type="16", show_post=True):
		try:
			if show_post is True:
				ps = bs(self.s.get(self.u+endpoint).text)
				endpoint = re.search('href="(/reactions/picker/\?is_permalink=1.*?)"', str(ps)).group(1)
				owner = find_owner(ps)
			ps = bs(self.s.get(self.u+endpoint.replace("&amp;", "&")).text)
			if not ps.find("span", string="(Hapus)"):
				ufi_reaction = get_href(ps, href="reaction_type="+type, single=True)["href"]
				ps = bs(self.s.get(self.u+ufi_reaction).text)
				if "Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu guna membantu melindungi komunitas dari spam." in str(ps):
					if show_post:
						exit("\x1b[0;31m [!] limit, silahkan tunggu beberapa saat\x1b[0m")
				return ("\x1b[0;37m [*] react sukses "+owner+endpoint.split("ft_id=")[1].split("&")[0] if ps.find("span", string=self.rt[type]) else "\x1b[0;31m [!] react gagal "+owner+endpoint.split("ft_id=")[1].split("&")[0]) + "\x1b[0m"
			else:
				return "\x1b[0;33m [!] already react "+owner+endpoint.split("ft_id=")[1].split("&")[0] + "\x1b[0m"
		except Connection:
			return "\x1b[0;31m [!] connection error\x1b[0m"
		except AttributeError:
			return " [!] error "+owner+endpoint.split("ft_id=")[1].split("&")[0]
			
				