
import unittest

import indexer

class IndexerTestCase(unittest.TestCase):
    def setUp(self):
        self.testdata = ['zip/test_l.zip', 'zip/test_p.zip']

    def test_extract_thumbnail(self):
        """test extract_metadata.extract_thumbnail()"""
        thumb = indexer.extract_metadata.extract_thumbnail('zip/test_l.zip')
        self.assertEqual(thumb.filetype, '.jpg')

        fp = open('image/test_l/001.jpg', 'r')
        img = fp.read()
        fp.close()
        self.assertEqual(thumb.bindata, img)

if __name__ == '__main__':
    unittest.main()
