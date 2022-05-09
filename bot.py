# fuck You
from hentai import *
import re
func = Oppai
url = "https://mbasic.facebook.com"

def back(function):
	getattr(__import__("getpass"), "getpass")("\n > enter untuk balik ")
	function()

def run():
	global masuk
	if masuk is True:
		func.login(False)
	masuk = True
	print(" 1. chat")
	print(" 2. react")
	print(" 3. komentar")
	print(" 4. groups")
	print(" 5. friends")
	print(" 6. postingan")
	print(" 7. hapus cookie")
	print(" 0. keluar")
	sl = input("\n ?> ")
	while sl not in list("12345670"):
		sl = input(" ?> ")
	if sl == "1":
		chat_menu()
	elif sl == "2":
		react_menu()
	elif sl == "3":
		komen_menu()
	elif sl == "4":
		groups_menu()
	elif sl == "5":
		teman_menu()
	elif sl == "6":
		postingan_menu()
	elif sl == "7":
		exit(os.remove(".biskuit"))
	elif sl == "0":
		exit()

def chat_menu():
	ms = messages(url, func.ses())
	print("\n 1. mass delet chat")
	print(" 2. mass chat friends")
	print(" 3. spam chat")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("1230"):
		sl = input(" ?> ")
	if sl == "1":
		mk = ms.feed()
		for x in mk:
			print(ms.delete(x))
	elif sl == "2":
		ch = input(" ?. isi chat: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi chat: ")
		mk = ms.feed()
		for x in mk:
			id = re.findall("cid\.c.(\d+)%3A(\d+)", x["u"])[0]
			id = id[1] if id[0] == func.c["c_user"] else id[0]
			x.update({"u": "/messages/read/?fbid="+id, "c": ch})
			print(ms.send(x))
	elif sl == "3":
		id, rs = user_check(" ?. username/id: ")
		if not "/messages/thread/" in rs.text:
			exit(" !. pengguna tidak dapat di chat")
		ch = input(" ?. isi chat: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi chat: ")
		jm = input(" ?. jumlah: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah: ")
		data = dict(u="/messages/read/?fbid="+re.search("/messages/thread/(\d*)", rs.text).group(1), n=get_title(bs(rs.text)).text+"\x1b[0m", c=ch)
		for x in range(int(jm)):
			print(ms.send(data))
	elif sl == "0":
		run()
	back(run)
			
def user_check(input_param, psde=True):
	id = input(input_param)
	while not id or id == " "*len(id):
		id = input(input_param)
	if psde is False:
		assert not id.startswith("https")
		id = "profile.php?id="+id+"&v=timeline" if id.isdigit() else id+"?v=timeline"
		id = url+"/"+id
	if not id.startswith("https"):
		id = url+"/"+id
	rs = func.ses().get(id)
	if "php?rand=" in rs.text:
		exit(" !. user not found, please check again\n > url: "+id)
	return id, rs
	
def react_menu():
	ms = reaction(url, func.ses())
	mp = feed_post(url, func.ses())
	print("\n 1. mass react in home")
	print(" 2. mass react in pages")
	print(" 3. mass react in group")
	print(" 4. mass react in friends timeline")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("12340"):
		sl = input(" ?> ")
	if sl == "1":
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		react_type = reaction_type()
		mk = mp.get_post("/home.php", "th", "Berita Lengkap", int(jm))
		for x in mk:
			print(ms.react(x["u"], type=react_type))
	elif sl == "2":
		id, rs = user_check(" ?. page url: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		react_type = reaction_type()
		mk = mp.get_post(id.split("facebook.com")[-1], "tp", "Berita Lengkap", int(jm))
		for x in mk:
			print(ms.react(x["u"], type=react_type))
	elif sl == "3":
		id, rs = user_check(" ?. group url: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		react_type = reaction_type()
		mk = mp.get_post(id.split("facebook.com")[-1], "tg", "Berita Lengkap", int(jm))
		for x in mk:
			print(ms.react(x["u"], type=react_type))
	elif sl == "4":
		id, rs = user_check(" ?. username/id: ", psde=False)
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		react_type = reaction_type()
		mk = mp.get_post(id.split("facebook.com")[-1], "th", "Berita Lengkap", int(jm))
		for x in mk:
			print(ms.react(x["u"], type=react_type))
	elif sl == "0":
		run()
	back(run)
	
def komen_menu():
	ms = comment(url, func.ses())
	mp = feed_post(url, func.ses())
	print("\n 1. mass comment in home")
	print(" 2. mass comment in pages")
	print(" 3. mass comment in group")
	print(" 4. mass comment in friends timeline")
	print(" 5. spam comment")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("123450"):
		sl = input(" ?> ")
	if sl == "1":
		ch = input(" ?. isi komentar: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi komentar: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		mk = mp.get_post("/home.php", "th", "Berita Lengkap", int(jm))
		for x in mk:
			x["c"] = ch
			print(ms.send(x))
	elif sl == "2":
		id, rs = user_check(" ?. page url: ")
		ch = input(" ?. isi komentar: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi komentar: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		mk = mp.get_post(id.split("facebook.com")[-1], "tp", "Berita Lengkap", int(jm))
		for x in mk:
			x["c"] = ch
			print(ms.send(x))
	elif sl == "3":
		id, rs = user_check(" ?. group url: ")
		ch = input(" ?. isi komentar: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi komentar: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		mk = mp.get_post(id.split("facebook.com")[-1], "tg", "Berita Lengkap", int(jm))
		for x in mk:
			x["c"] = ch
			print(ms.send(x))
	elif sl == "4":
		id, rs = user_check(" ?. username/id: ", psde=False)
		ch = input(" ?. isi komentar: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi komentar: ")
		jm = input(" ?. jumlah postingan: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah postingan: ")
		mk = mp.get_post(id.split("facebook.com")[-1], "th", "Berita Lengkap", int(jm))
		for x in mk:
			x["c"] = ch
			print(ms.send(x))
	elif sl == "5":
		id, rs = user_check(" ?. url/id postingan: ")
		ch = input(" ?. isi komentar: ")
		while not ch or ch == " "*len(ch):
			ch = input(" ?. isi komentar: ")
		jm = input(" ?. jumlah komentar: ")
		while not jm.isdigit():
			jm = input(" ?. jumlah komentar: ")
		data = dict(u=id.split("facebook.com")[-1], c=ch)
		for x in range(int(jm)):
			print(ms.send(data))
	elif sl == "0":
		run()
	back(run)

def teman_menu():
	ms = friends(url, func.ses())
	print("\n 1. aceept friends request")
	print(" 2. unaccept friends request")
	print(" 3. remove friends")
	print(" 4. block friends")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("12340"):
		sl = input(" ?> ")
	if sl == "1":
		ms.request("/friends/center/requests/#friends_center_main", "Konfirmasi|Permintaan diterima")
	elif sl == "2":
		ms.request("/friends/center/requests/#friends_center_main", "Hapus Permintaan|Permintaan dihapus")
	elif sl == "3":
		ms.start("/removefriend.php?friend_id=", "Konfirmasi")
	elif sl == "4":
		ms.start("/privacy/touch/block/confirm/?bid=", "Blokir")
	elif sl == "0":
		run()
	back(run)

def groups_menu():
	if not e:
		exit(" .! token tidak ada")
	ms = groups(url, func.ses())
	print("\n 1. leave grup")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("120"):
		sl = input(" ?> ")
	if sl == "1":
		fields = ms.feed(func.ses(), e)
		temp = fields
		if not fields:
			exit(" !. no groups found")
		for x in range(len(fields)):
			print(f" [{x+1}] {fields[x]['n']}")
		print("\n *. gunakan ',' sebagai pemisah")
		print(" *. example: 1,2,3,4")
		print(" *. type 'all' untuk memilih semuanya")
		sl = input("\n ?> ")
		while not sl:
			sl = input(" ?> ")
		if sl != "all":
			temp = []
			for x in sl.split(","):
				if x.isdigit():
					if int(x) <= len(fields):
						temp.append(fields[int(x)-1])
			if not temp:
				exit(" !. isi yang bener dong asu")
		for x in temp:
			print(ms.leave(x))
	elif sl == "0":
		run()
	back(run)

def postingan_menu():
	ms = postingan(url, func.ses())
	print("\n 1. hapus postingan")
	print(" 2. private postingan")
	print(" 0. kembali")
	sl = input("\n ?> ")
	while sl not in list("120"):
		sl = input(" ?> ")
	if sl == "1":
		ms.start("/profile.php?v=timeline")
	elif sl == "2":
		exit(" !. fitur belum tersedia karna menurut gw kurang guna:v")
	elif sl == "0":
		run()
	back(run)

def reaction_type(type=["1", "2", "16", "4", "3", "7", "8"]):
	print('\n * reaction type\n 1. like\n 2. love\n 3. peduli\n 4. Haha\n 5. Wow\n 6. Sedih\n 7. Marah\n')
	sl = input(" ?> ")
	while not sl in [str(i) for i in range(1, len(type)+1)]:
		sl = input(" ?> ")
	return type[int(sl)-1]
	
if not os.path.exists(".biskuit"):
	masuk = True
	c = input(" # cookie: ")
	while not "c_user" in c:
		c = input(" # cookie: ")
	if c.endswith(";"):
		c = c[:-1]
else:
	masuk = False
	l = __import__("json").loads(open(".biskuit").read())
	c = l["cookie"]
	e = l["token"]

func = func(url, c)
func.login(masuk)
url = func.u
if masuk is True:
	e = func.t
	masuk = False
run()