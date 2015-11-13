import os.path
import unittest

import indexer


class IndexerTestCase(unittest.TestCase):
    def setUp(self):
        self.testdir = os.path.dirname(__file__)
        self.testdata = ['zip/test_l.zip', 'zip/test_p.zip']

    def _get_rpath(self, fpath):
        return os.path.join(self.testdir, fpath)

    def test_extract_thumbnail(self):
        """test extract_metadata.extract_thumbnail()"""
        thumb = indexer.extract_metadata.extract_thumbnail(self._get_rpath('zip/test_l.zip'))
        self.assertEqual(thumb.filetype, '.jpg')

        fp = open(self._get_rpath('image/test_l/001.jpg'), 'rb')
        img = fp.read()
        fp.close()
        self.assertEqual(thumb.bindata, img)

if __name__ == '__main__':
    unittest.main()
