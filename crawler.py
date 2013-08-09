import urllib

class Crawler(object):
	def __init__(self,url):
		self.valid=True
		try:
			self.urlop = urllib.urlopen(url).readlines()
		except IOError:
			self.valid=False

	def get_torrent_url_from_line(self,line):
		begin = "a href=\""
		end = ".torrent"
		index=line.index(begin)
		index2=line.index(end)
		return line[index+len(begin):index2+len(end)]

	def get_torrents(self):
		torrents = []
		domain = "http://www.legittorrents.info/"
		for line in self.urlop:
			if (".torrent" in line):
				torrents.append(domain + self.get_torrent_url_from_line(line))
		
		return torrents

	def download_file(self, url):
		if not("f=" in url): 
			raise IOError 
		myfile = self.get_file_name(url)
		(filename, headers) = urllib.urlretrieve(url, myfile)	
		if headers['content-type']=='application/x-bittorrent':
			return myfile

		else: 
			raise IOError
	
	def download_all_files(self):
		succeded = 0;
		lista = self.get_torrents()
		downloaded_files = []		

		if len(lista) != 0:
			for torrent in lista:
				file_name = self.download_file(torrent)
				if file_name:
					downloaded_files.append(file_name)
					#succeded += 1

			return downloaded_files

		else:
			raise IOError	

	def get_file_name(self,url):
			return url[url.index("f=")+ 2:]
