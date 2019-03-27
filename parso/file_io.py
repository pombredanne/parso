import os


class FileIO:
    def __init__(self, path):
        self.path = path

    def read(self):  # Returns bytes/str
        # We would like to read unicode here, but we cannot, because we are not
        # sure if it is a valid unicode file. Therefore just read whatever is
        # here.
        with open(self.path, 'rb') as f:
            return f.read()

    def get_last_modified(self):
        """
        Returns float - timestamp
        Might raise FileNotFoundError
        """
        return os.path.getmtime(self.path)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.path)


class KnownContentFileIO(FileIO):
    def __init__(self, path, content):
        super(KnownContentFileIO, self).__init__(path)
        self._content = content

    def read(self):
        return self._content
