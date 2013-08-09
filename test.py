import unittest
import os
from crawler import Crawler

URL = "http://www.legittorrents.info/index.php?page=torrents&active=1&category=1&order=3&by=2&pages=2"


class TestCrawler(unittest.TestCase):
	
	def test_invalid_url(self):
		crawler = Crawler("abcd")
		self.assertEqual(crawler.valid,False)

	def test_valid_url(self):
		crawler = Crawler(URL)
		self.assertEqual(crawler.valid,True)

	def test_find_torrent(self):
		crawler = Crawler(URL)
		self.assertEqual(len(crawler.get_torrents()),18)
	
	def test_find_torrent_called_twice(self):
		crawler = Crawler(URL)
		self.assertEqual(len(crawler.get_torrents()),18)
		self.assertEqual(len(crawler.get_torrents()),18)

	def test_url_from_line(self):
		crawler = Crawler(URL)
		self.assertEqual(crawler.get_torrent_url_from_line('<td align="center" width="20" class="lista" style="text-align: center;"><a href="download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent"><img src="images/download.gif" border="0"  alt="torrent"/></a>'),"download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent")

	def test_get_file_name_from_url(self):
		crawler = Crawler(URL)

		FILE_URL = "http://www.legittorrents.info/download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent"
		FILE_NAME = "The+Tunnel+%282011%29+%28720p%29.torrent"

		self.assertEqual(FILE_NAME, crawler.get_file_name(FILE_URL))

	def test_download_file(self):
		crawler = Crawler(URL)
		FILE_URL = "http://www.legittorrents.info/download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent"
		FILE_NAME = "The+Tunnel+%282011%29+%28720p%29.torrent"
		self.assertEqual(crawler.download_file(FILE_URL), FILE_NAME)
		self.assertTrue(os.path.isfile(FILE_NAME))

	def test_download_file_not_found(self):
		crawler = Crawler(URL)
		self.assertRaises(IOError,crawler.download_file,"http://www.legittorrents.info/oleola")
	
	def test_download_all_files_error(self):
		crawler = Crawler("http://www.legittorrents.info/oleola")
		self.assertRaises(IOError,crawler.download_all_files)

	def test_download_all_files_success(self):
		crawler = Crawler(URL)
		listBefore = map(crawler.get_file_name,crawler.get_torrents())
		listAfter = crawler.download_all_files()
		
		self.assertEqual(sorted(listBefore), sorted(listAfter))

if __name__ == "__main__":
	unittest.main()
