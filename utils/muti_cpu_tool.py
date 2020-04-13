from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import multiprocessing
from multiprocessing import Pool

import numpy as np

from utils.check_sys_envirment import Exam_Sys_Envir

if Exam_Sys_Envir().is_ipynb_envirment():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm


def imap_unordered_bar(func, args, n_processes = multiprocessing.cpu_count()):
    return imap_unordered_bar_with_gen(func, args ,len(args))


def imap_unordered_bar_with_gen(func, args, total_len, n_processes = multiprocessing.cpu_count()):
    p = Pool(n_processes)
    res_list = []
    with tqdm(total = total_len) as pbar:
        for i, res in tqdm(enumerate(p.imap_unordered(func, args))):
            pbar.update()
            res_list.append(res)
    pbar.close()
    p.close()
    p.join()
    return res_list

def parallel_dataframe(func, df, n_processes = multiprocessing.cpu_count()):
    return imap_unordered_bar_with_gen(func, df.iterrows() ,len(df))
