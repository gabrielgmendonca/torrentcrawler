import unittest
import os
from crawler import Crawler

domain = "http://www.legittorrents.info/"
URL = "http://www.legittorrents.info/index.php?page=torrents&search=&category=1&active=1"
line = '<td align="center" width="20" class="lista" style="text-align: center;"><a href="download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent"><img src="images/download.gif" border="0" alt="torrent"/></a>'
url = "download.php?id=0819ccee9ebe25d7a02fe14496d58af10ef94aec&amp;f=The+Tunnel+%282011%29+%28720p%29.torrent"
filename = "The+Tunnel+%282011%29+%28720p%29.torrent"

class TestCrawler(unittest.TestCase):

    def test_invalid_url(self):

	crawler = Crawler("blau",domain)
	self.assertFalse(crawler.valid)

    def test_valid_url(self):

	crawler = Crawler(URL,domain)
	self.assertTrue(crawler.valid)

    def test_get_torrent_url(self):

        crawler = Crawler(URL,domain)
        self.assertEqual(crawler.get_Torrent_URL(line),url)

    def test_get_torrents(self):

	crawler = Crawler(URL,domain)
	self.assertEqual(len(crawler.get_Torrents_List()),18)

    def test_get_filename(self):

        crawler = Crawler(URL,domain)
        self.assertEqual(filename,crawler.get_Filename(domain+url))

    def test_download_file(self):

        crawler = Crawler(URL,domain)
        self.assertEqual(crawler.download_File(domain+url),filename)
        self.assertTrue(os.path.isfile(filename))

    def test_page_files(self):

        crawler = Crawler(URL,domain)
        target_links = map(crawler.get_Filename, crawler.get_Torrents_List())
        dloaded_links = crawler.download_Page_Files()
        self.assertEqual(sorted(target_links), sorted(dloaded_links))

if __name__ == "__main__":
    unittest.main()
