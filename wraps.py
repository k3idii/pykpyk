

# decorator
def fix_kwarg(kwarg_name, func, *func_a, **func_kw):  # <- so awesome !
  def _wrap1(f):
    def _wrap2(*a, **kw):
      if kwarg_name in kw:
        kw[kwarg_name] = func(kw[kwarg_name], *func_a, **func_kw)
      else:
        idx = f.func_code.co_varnames.index(kwarg_name)
        a = list(a)
        print func, a[idx], func_a, func_kw
        a[idx] = func(a[idx], *func_a, **func_kw)
      return f(*a, **kw)
    if kwarg_name not in f.func_code.co_varnames:
      raise Exception("{0} not in arg names of {1}".format(kwarg_name, str(f)))
    return _wrap2
  return _wrap1

