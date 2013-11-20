import urllib

class Crawler(object):

    def __init__(self,url,domain):

	try:
	    self.urlop = urllib.urlopen(url).readlines()
	    #Returns IOError if invalid URL
	    self.valid = True
	    self.domain = domain
	except IOError:
	    self.valid = False

    def get_Torrent_URL(self,line):

	begin = "a href="
	end = ".torrent"
	index_begin = line.index(begin)+len(begin)+1
	#Takes the start of the URL
	index_end = line.index(end)+len(end)
	#Takes the end of the URL
	return line[index_begin:index_end]
    
    def get_Torrents_List(self):

	torrents = [] #List of torrent URLs
	for line in self.urlop:
            if ".torrent" in line:
		torrents.append(self.domain+self.get_Torrent_URL(line))
	return torrents

    def get_Filename(self,url):

	start = url.index("f=") + 2
	return url[start:]
    
    def download_File(self,url):

	if not ("f=" in url): raise IOError #Not a download URL
	myfile = self.get_Filename(url)
	(filename, headers) = urllib.urlretrieve(url, myfile)
	#Downloads the file from 'url' as 'myfile'
	#Headers stores information about the file
	if headers['content-type']=='application/x-bittorrent': return myfile
	else: raise IOError #Error on download

    def download_Page_Files(self):

	lista = self.get_Torrents_List()
	downloaded_files = []
	if len(lista) != 0:
            for torrent in lista:
		dfile = self.download_File(torrent)
		if dfile: downloaded_files.append(dfile)
            return downloaded_files #Returns this for control purposes
	else: raise IOError

