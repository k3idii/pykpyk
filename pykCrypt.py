
def gen_xor_str_key(data, key):
  for c in data:
    yield chr(key ^ ord(c))

def xor_key(key, data):
  return ''.join(gen_xor_str_key(data, key))

def gen_brute_xor_str_key(data):
  for k in range(0,255):
    yield xor_key(k, data)

def gen_xor_str_str(a,b):
  if len(a) != len(b):
    Warning("Length missmatch !")
  for (x,y) in zip(map(ord, a), map(ord, b)):
    yield chr(x^y)

def xor_str_str(a, b):
  return ''.join( gen_xor_str_str(a,b) )




