

def hexdump(data,inRow=16,title=None,head=True):
  S = ' \n'
  if head:
    if title:
      S += " .----[ %s ]----- \n" % title
    S += "| offset          ascii                 hex   \n"
  fmt = "| 0x%08X %-"+str(inRow)+"s \t %s\n"
  size = len(data)
  off = 0
  while True:
    chunk = data[off:off+inRow]
    hx = ''
    ch = ''
    for c in list(chunk):
      ch+= c if ord(c)>=32 and ord(c)<127 else '.'
      hx += "%02X " % ord(c)
    S += fmt % (off,ch,hx)
    off+=inRow
    if len(chunk) < inRow or off > size :
      break
  S+= "| 0x%08X \n" % off
  S+= "`-- \n"

  return S

