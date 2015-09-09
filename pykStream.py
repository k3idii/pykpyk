from StringIO import StringIO
import struct
import string
import os

CHUNK_SIZE = 1024


def glue_ex(parts, delim='', preproc=None):
  if preproc:
    if isinstance(preproc, list):
      for fn in preproc:
        parts = map(fn, parts)
    elif callable(preproc):
      parts = map(preproc, parts)
  return delim.join(parts)


def unpack_ex(fmt, data, into=None):
  size = struct.calcsize(fmt)
  parts = struct.unpack(fmt, data)
  if not parts:
    return None
  if not into:
    return parts
  if len(parts) > len(into):
    raise Exception("unpack_ex: too many values unpacked !")
  return dict((into[i], parts[i]) for i in range(len(parts)))


class ExtStrException(Exception):
  pass


class ExtStr(StringIO):
  def read_n(self, n):
    d = self.read(n)
    if not d or len(d) < n:
      raise ExtStrException("Read error : need %d bytes, got %d " % (n, len(d)))
    return d

  def read_fmt(self, fmt="", into=None):
    sz = struct.calcsize(fmt)
    d = self.read_n(sz)
    return unpack_ex(fmt, d, into)

  def read_single_fmt(self, fmt):
    v = self.read_fmt(fmt)
    if v:
      return v[0]
    else:
      return None

  def read_the_rest(self):
    s = self.getLen()
    p = self.getPos()
    d = s - p
    return self.read_n(d)

  def append(self, data):
    p = self.tell()
    self.seek(0, os.SEEK_END)
    self.write(data)
    self.seek(p)

  def append_fmt(self, fmt, *a):
    return self.append(struct.pack(fmt, *a))

  def write_fmt(self, fmt, *a):
    return self.write(struct.pack(fmt, *a))

  def read_all(self):
    p = self.tell()
    self.seek(0)
    v = self.read()
    self.seep(p)
    return v

  def dump(self):
    return self.getvalue()

  def get_rest_len(self):
    org = self.tell()
    self.seek(0, os.SEEK_END)
    end = self.tell()
    self.seek(org)
    return end

  def get_pos(self):
    return self.tell()

  def available_bytes(self):
    return self.getLen() - self.getPos()


  def hexDump(self, inRow=16, title=None, head=True):
    S = ' \n'
    if head:
      if title:
        S += " .----[ %s ]----- \n" % title
      S += "| offset          ascii                 hex   \n"
    p = self.tell()  # save
    self.seek(0)  # rewind
    fmt = "| 0x%08X %-" + str(inRow) + "s \t %s\n"
    while True:
      of = self.tell()
      chunk = self.read(inRow)
      hx = ''
      ch = ''
      for c in list(chunk):
        ch += c if ord(c) >= 32 and ord(c) < 127 else '.'
        hx += "%02X " % ord(c)
      S += fmt % (of, ch, hx)
      if len(chunk) < inRow:
        break
    S += "| 0x%08X \n" % self.tell()
    S += "`-- \n"
    self.seek(p)
    return S

