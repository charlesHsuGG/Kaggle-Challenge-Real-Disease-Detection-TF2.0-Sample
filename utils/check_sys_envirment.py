from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import platform

class Exam_Sys_Envir(object):

    def is_linux_envirment(self):
        if platform.system() == "Linux":
            return True
        else:
            return False

    def is_ipynb_envirment(self):
        try:
            cfg = get_ipython().config 
            if cfg['IPKernelApp']:
                return True
            else:
                return False
        except NameError:
            return False