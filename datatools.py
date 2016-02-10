import itertools
import struct

def ip4_to_int32(str_ip, order='>'):
  return struct.unpack(order+"I",struct.pack("BBBB",*map(int,str_ip.split("."))))[0]

def int32_to_ip4(big_int, order='>'):
  return '.'.join(map(str, struct.unpack("BBBB",struct.pack(order+"I",big_int))))

def gen_get_n_bit(data, bit=1):
  mask = 1 << n
  for c in data:
    yield 1 if ord(c) & mask else 0

def get_n_bit(data, bit=1):
  return list(gen_get_n_bit(data, bit))

def byte_to_bin_str(byte):
  return "{0:0>b}".format(byte)

def byte_to_bin_arr(byte):
  return [int(x) for x in byte_to_bin_str(byte)]

def gen_chunks(data, size):
  for i in range(1+len(data)/size):
    yield data[i*size:(i+1)*size]

def chunks(data, size):
  return list(gen_chunks(data, size))

def compare_collection(col, func_cmp):
  for pair in itertools.combinations(col, 2):
    if not func_cmp(*pair):
      return False
  return True

def gen_pairs(col,):
  return itertools.combinations(col,2);

