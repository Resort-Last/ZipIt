from os import getcwd, mkdir, path, listdir
import pyminizip
import shutil


class PyZipper(object):
    """arguments:
    source file OR list of source files,
    file_name(str),
    password(str)
    return:
    pw protected zip file source
    """
    def __init__(self, src, file_name, password):
        self.src = src
        self.file_name = file_name
        self.password = password
        self.folder = getcwd()
        self.archive = self.create_folder

    def zip(self):
        if type(self.src) == list:
            pyminizip.compress_multiple(self.src, '', f'{self.file_name}.zip', self.password, 1)
        else:
            pyminizip.compress(self.src, '', f'{self.file_name}.zip', self.password, 1)
        shutil.move(f'{self.folder}\\{self.file_name}.zip', f'{self.archive}\\{self.file_name}.zip')
        return f'{self.archive}\\{self.file_name}.zip'

    def create_folder(self):
        archive_name = 'Archive'
        archive_fold = path.join(self.folder, archive_name)
        if archive_name not in listdir(self.folder):
            mkdir(archive_fold)
        return archive_fold
