import pygame
import PIL
import itertools

class letMeTry(object): 
  def __init__(self, f, *a):
    self.f=f
    self.a=a
    print a

  def _p(self,v):
    print "GOT: ",`v`[:20]," ... "

  def now(self,p=None,show_error=False):
    if p is None:
      p = self._p
    for argset in itertools.product(*self.a):
      try:
        v = self.f(*argset)
        p(v)
      except Exception as e:
        if show_error:
          print "ERROR: ",`e`


def readImg(f):
  return PIL.Image.open(f)


def img2pixels(img):
  px = img.load()
  w,h = img.size
  pix = []
  for x in range(w):
    row = []
    for y in range(h):
      row.append( px[x,y] )
    pix.append(row) 
  return pix

