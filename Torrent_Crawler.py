from crawler import Crawler
import os
import urllib
import shutil

#Use the following variables to set up the program's settings:

domain = "http://www.legittorrents.info/"
#Set the domain's url

first_page = "http://www.legittorrents.info/index.php?page=torrents&active=1&category=1&order=3&by=2&pages=1"
#Set a link to the first search page

n_pages = 2
#Set how many pages should be searched. Zero defaults to all.

target_path = "/media/141C-7592/Torrent Crawler/torrents"
#Set where to save the torrent files. Leave blank for local directory.

files = []

if n_pages!=0:

    count = 1
    while count < abs(n_pages)+1:
        crawler = Crawler(first_page[:-1]+str(count),domain)
        if not(crawler.valid): break
        print "Downloading page %d..." % (count)
        files+=crawler.download_Page_Files()
        count+=1

else:

    count = 1
    while True:
        crawler = Crawler(first_page[:-1]+str(count),domain)
        if not(crawler.valid): break
        if crawler.get_Torrents_List==[]: break
        files+=crawler.download_Page_Files()
        count+=1

if target_path != "":
	print "Moving files..."
	for torrent in files:
		source_path = os.path.abspath(torrent)
		#os.rename(source_path,target_path)
		#Will not work for different disks
		try: shutil.move(source_path,target_path)
		except shutil.Error:
			os.remove(target_path+"/"+torrent)
			shutil.move(source_path, target_path)

print "\nDONE!"
