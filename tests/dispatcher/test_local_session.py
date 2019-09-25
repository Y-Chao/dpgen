import os,json,glob,shutil
import unittest

from .context import LocalSession
from .context import setUpModule

class TestLocalSession(unittest.TestCase):
    def test_work_path(self):
        cwd = os.getcwd()        
        wp = LocalSession({'work_path' : cwd})
        self.assertTrue(os.path.abspath(cwd), wp.get_work_root())


        
