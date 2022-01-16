#!/usr/bin/env python
# coding: utf-8

# In[1]:

def cover_modify(path=None,outdir='./cover.jpg'):
    import os
    from glob import glob
    from PIL import Image
    from PIL.ImageFilter import GaussianBlur
    import matplotlib.pyplot as plt
    
    def GUI_select(verbose=0):
        import win32ui
        flg=win32ui.CreateFileDialog(1)
        flg.DoModal()
        
        fname=flg.GetPathName()
        if verbose:
            print(fname)
        return fname
    
    def filt_ext(name):
        ext=os.path.splitext(name)[1]
        return (ext not in ['.mkv','.mp4'])
    
    
    if path is None:
        path=GUI_select()
    
    names=glob(path)
    if len(names) == 0:
        raise AssertionError("Cannot find files with name",path)
    
    names=[i for i in filter(filt_ext,names)]
    print(names)
    assert(len(names) == 1)
    
    name=names[0]
    mode='pad'
    
    def blur(im):
        border=w//9*10*0.05
        im=im.crop([border, 0 , border+w, h//9*10])
        im=im.filter(GaussianBlur(radius=10))
        return im
    
    with Image.open(name) as img:
        print(img.size)
        w,h=img.size
        if mode == 'resize':
            im=img.resize([w,h//9*10])
        else:
            im=img.resize([w//9*10,h//9*10])
            im=blur(im)
            im.paste(img,[0,h//9*10//20])
        plt.imshow(im)
    
    im.save(outdir)
    
if 1:
    cover_modify()
