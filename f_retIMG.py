import shutil,f_logging
import pprint
from os import getcwd, path, listdir
from pathlib import Path as pathlib_path
from sys import exit


# for more information see: https://github.com/f-h-publik/dcm-jpg-html








      
def f_retDirsFiles(inlist,inpath):
    f_files=[]
    f_dirs=[]
    
    for i,f_thisfile in enumerate(inlist):
        f_thisfile=inpath+'/'+f_thisfile
        # logger.debug(f_thisfile)
        # logger.debug(path.isfile(f_thisfile))
        
        if path.isfile(f_thisfile):
            f_files.append(f_thisfile)
        else:
            f_dirs.append(f_thisfile)
    return f_dirs, f_files

def f_retEnumImg(infilnames,in_andelse='.png',in_digits=4):
    outfilenames=[]
    discarded_filenames=[]
    for i,this_fn in enumerate(infilnames):
        andelse=this_fn[-4:]
        siffrelse=this_fn[-8:-4]
        if andelse==in_andelse and siffrelse.isnumeric():
            outfilenames.append(this_fn)
        else:
            discarded_filenames.append(this_fn)

    return outfilenames,discarded_filenames

     

def f_allimg_thisfolder(inpath='EMPTY',in_andelse='.png',in_digits=4):
    
    #get all images in thisfolder

    #get all files  and sort
    if (inpath!="EMPTY"):
        thispath=inpath
    else:
        thispath=pathlib_path.cwd()
    
     f_out=listdir(thispath)
    f_out.sort()
 
     outdirs,outfiles=f_retDirsFiles(f_out,thispath)

     outfiles,disc_files=f_retEnumImg(outfiles,in_andelse,in_digits)

 


    return outfiles


 
 
