import pygame 

def val2clr(v):
  return ( int(v)%255,int(v)%255,int(v)%255 )



class vis():
  def __init__(self,w=640,h=480):
    pygame.init()
    self.w=w
    self.h=h
    self.screen = pygame.display.set_mode( (w,h) )
  
  def clear(self,c=(0,0,0)):
    self.screen.fill( c )
    pygame.display.flip()
    
  def pixel(self,x,y,c=(255,255,255),s=1,draw=False):
    self.screen.fill( c , (x*s,y*s,s,s) )
    if draw:
      pygame.display.flip()

  def matrix(self,m,v2c=val2clr,scale=-1):
    if scale==-1:
      height = len(m)
      width = len(m[0])
      scale = 1 
      while height*scale < self.h and width*scale < self.w:
        scale+=1
    for row in range(len(m)):
      r = m[row]
      for col in range(len(r)):
        self.pixel(col,row, v2c(r[col]), scale )
    pygame.display.flip()     


  def loop(self):
    while True:
      ev = pygame.event.poll()
      if ev.type == pygame.QUIT:
        break


