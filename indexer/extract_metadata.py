import os
import zipfile

class Metadata(object):
    """
    Metadata class for eBooks
    """
    def __init__(self):
        """
        Create a new metadata.
        """
        self.filename = ''
        self.tags = []


class ThumbnailError(Exception):
    """
    Exception class for Thumbnails
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
    

class Thumbnail(object):
    """
    Contain thumbnail data and metadata
    """
    def __init__(self, filetype, bindata):
        """
        Create a new thumbnail object.
        Arguments:
          * filetype
            thumbnail format string such as ".png", ".jpeg", etc.
          * bindata
            thumnail's binary data
        """
        self.filetype = filetype
        self.bindata = bindata
        

def extract_thumbnail(pathname):
    """
    Extract thumbnail image from given eBook file.
    """
    image_exts = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    fp = open(pathname, 'r')
    zipf = zipfile.ZipFile(fp)

    filenames = sorted(zipf.namelist())
    for f in filenames:
        ext = os.path.splitext(f)[1]
        if ext in image_exts:
            thumb = _ext_thumb(zipf, f, ext)
            zipf.close()
            fp.close()
            return thumb

    zipf.close()
    fp.close()
    raise ThumbnailError('NotFound')
    
def _ext_thumb(zipf, name, ext):
    if ext == '.jpeg':
        ext = '.jpg'
    return Thumbnail(ext, zipf.read(name))
