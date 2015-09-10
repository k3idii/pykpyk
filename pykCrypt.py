
def gen_xor_key(key, data):
  for c in data:
    yield k ^ ord(c)

def xor_key(key, data):
  return ''.join(gen_xor_key(key, data))

def gen_brute_xor_key(data):
  for k in range(0,255):
    yield xor_key(k, data)



def gen_xor_str(a,b):
  ml=max(len(a),len(b))
  a=map(ord,a[:ml])
  b=map(ord,b[:ml])
  for (x,y) in zip(a,b):
    yield chr(ord(x)^ord(y))

def xor_str(a, b):
  return ''.join( gen_xor_str(a,b) )

def gen_get_n_bit(data, bit=1):
  mask = 1 << n
  for c in data:
    yield 1 if ord(c) & mask else 0

def get_n_bit(data, bit=1):
  return list(gen_get_n_bit(data, bit))

def byte_to_strbin(byte):
  return "{0:0>b}".format(byte)

def str_to_intbin(byte):
  return [int(x) for x in byte_to_strbin(byte)]


def gen_chunks(data, size):
  for i in range(1+len(data)/size):
    yield s[i*size:(i+1)*size]

def chunks(data, size):
  return list(gen_chunks(data, size))



