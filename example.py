# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_example')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_example')
    _example = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_example', [dirname(__file__)])
        except ImportError:
            import _example
            return _example
        try:
            _mod = imp.load_module('_example', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _example = swig_import_helper()
    del swig_import_helper
else:
    import _example
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def save_version(ar, path):
    return _example.save_version(ar, path)
save_version = _example.save_version

def check_version(ar, path):
    return _example.check_version(ar, path)
check_version = _example.check_version
BOSONIC = _example.BOSONIC
FERMIONIC = _example.FERMIONIC
POSITIVE_NEGATIVE = _example.POSITIVE_NEGATIVE
POSITIVE_ONLY = _example.POSITIVE_ONLY
class base_mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, base_mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, base_mesh, name)
    __repr__ = _swig_repr

    def points(self):
        return _example.base_mesh_points(self)

    def __init__(self):
        this = _example.new_base_mesh()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _example.delete_base_mesh
    __del__ = lambda self: None
base_mesh_swigregister = _example.base_mesh_swigregister
base_mesh_swigregister(base_mesh)
cvar = _example.cvar
minor_version = cvar.minor_version
major_version = cvar.major_version

class real_frequency_mesh(base_mesh):
    __swig_setmethods__ = {}
    for _s in [base_mesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, real_frequency_mesh, name, value)
    __swig_getmethods__ = {}
    for _s in [base_mesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, real_frequency_mesh, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _example.new_real_frequency_mesh()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def extent(self):
        return _example.real_frequency_mesh_extent(self)

    def __call__(self, idx):
        return _example.real_frequency_mesh___call__(self, idx)

    def save(self, ar, path):
        return _example.real_frequency_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.real_frequency_mesh_load(self, ar, path)

    def __eq__(self, mesh):
        return _example.real_frequency_mesh___eq__(self, mesh)

    def __ne__(self, mesh):
        return _example.real_frequency_mesh___ne__(self, mesh)
    __swig_destroy__ = _example.delete_real_frequency_mesh
    __del__ = lambda self: None
real_frequency_mesh_swigregister = _example.real_frequency_mesh_swigregister
real_frequency_mesh_swigregister(real_frequency_mesh)

class itime_mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, itime_mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, itime_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, beta, ntau):
        this = _example.new_itime_mesh(beta, ntau)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __call__(self, idx):
        return _example.itime_mesh___call__(self, idx)

    def extent(self):
        return _example.itime_mesh_extent(self)

    def __eq__(self, mesh):
        return _example.itime_mesh___eq__(self, mesh)

    def beta(self):
        return _example.itime_mesh_beta(self)

    def statistics(self):
        return _example.itime_mesh_statistics(self)

    def points(self):
        return _example.itime_mesh_points(self)

    def __ne__(self, mesh):
        return _example.itime_mesh___ne__(self, mesh)

    def save(self, ar, path):
        return _example.itime_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.itime_mesh_load(self, ar, path)

    def compute_points(self):
        return _example.itime_mesh_compute_points(self)
    __swig_destroy__ = _example.delete_itime_mesh
    __del__ = lambda self: None
itime_mesh_swigregister = _example.itime_mesh_swigregister
itime_mesh_swigregister(itime_mesh)

class power_mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, power_mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, power_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, beta, power, uniform):
        this = _example.new_power_mesh(beta, power, uniform)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __call__(self, idx):
        return _example.power_mesh___call__(self, idx)

    def extent(self):
        return _example.power_mesh_extent(self)

    def power(self):
        return _example.power_mesh_power(self)

    def uniform(self):
        return _example.power_mesh_uniform(self)

    def __eq__(self, mesh):
        return _example.power_mesh___eq__(self, mesh)

    def beta(self):
        return _example.power_mesh_beta(self)

    def statistics(self):
        return _example.power_mesh_statistics(self)

    def points(self):
        return _example.power_mesh_points(self)

    def weights(self):
        return _example.power_mesh_weights(self)

    def __ne__(self, mesh):
        return _example.power_mesh___ne__(self, mesh)

    def save(self, ar, path):
        return _example.power_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.power_mesh_load(self, ar, path)

    def compute_points(self):
        return _example.power_mesh_compute_points(self)

    def compute_weights(self):
        return _example.power_mesh_compute_weights(self)
    __swig_destroy__ = _example.delete_power_mesh
    __del__ = lambda self: None
power_mesh_swigregister = _example.power_mesh_swigregister
power_mesh_swigregister(power_mesh)

class momentum_realspace_index_mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, momentum_realspace_index_mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, momentum_realspace_index_mesh, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def extent(self):
        return _example.momentum_realspace_index_mesh_extent(self)

    def dimension(self):
        return _example.momentum_realspace_index_mesh_dimension(self)

    def kind(self):
        return _example.momentum_realspace_index_mesh_kind(self)

    def __eq__(self, mesh):
        return _example.momentum_realspace_index_mesh___eq__(self, mesh)

    def __ne__(self, mesh):
        return _example.momentum_realspace_index_mesh___ne__(self, mesh)

    def points(self):
        return _example.momentum_realspace_index_mesh_points(self)

    def save(self, ar, path):
        return _example.momentum_realspace_index_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.momentum_realspace_index_mesh_load(self, ar, path)
    __swig_destroy__ = _example.delete_momentum_realspace_index_mesh
    __del__ = lambda self: None
momentum_realspace_index_mesh_swigregister = _example.momentum_realspace_index_mesh_swigregister
momentum_realspace_index_mesh_swigregister(momentum_realspace_index_mesh)

class momentum_index_mesh(momentum_realspace_index_mesh):
    __swig_setmethods__ = {}
    for _s in [momentum_realspace_index_mesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, momentum_index_mesh, name, value)
    __swig_getmethods__ = {}
    for _s in [momentum_realspace_index_mesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, momentum_index_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _example.new_momentum_index_mesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __call__(self, idx):
        return _example.momentum_index_mesh___call__(self, idx)
    __swig_destroy__ = _example.delete_momentum_index_mesh
    __del__ = lambda self: None
momentum_index_mesh_swigregister = _example.momentum_index_mesh_swigregister
momentum_index_mesh_swigregister(momentum_index_mesh)

class real_space_index_mesh(momentum_realspace_index_mesh):
    __swig_setmethods__ = {}
    for _s in [momentum_realspace_index_mesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, real_space_index_mesh, name, value)
    __swig_getmethods__ = {}
    for _s in [momentum_realspace_index_mesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, real_space_index_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _example.new_real_space_index_mesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __call__(self, idx):
        return _example.real_space_index_mesh___call__(self, idx)
    __swig_destroy__ = _example.delete_real_space_index_mesh
    __del__ = lambda self: None
real_space_index_mesh_swigregister = _example.real_space_index_mesh_swigregister
real_space_index_mesh_swigregister(real_space_index_mesh)

class index_mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, index_mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, index_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, np):
        this = _example.new_index_mesh(np)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def extent(self):
        return _example.index_mesh_extent(self)

    def __call__(self, idx):
        return _example.index_mesh___call__(self, idx)

    def points(self):
        return _example.index_mesh_points(self)

    def __eq__(self, mesh):
        return _example.index_mesh___eq__(self, mesh)

    def __ne__(self, mesh):
        return _example.index_mesh___ne__(self, mesh)

    def save(self, ar, path):
        return _example.index_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.index_mesh_load(self, ar, path)

    def compute_points(self):
        return _example.index_mesh_compute_points(self)
    __swig_destroy__ = _example.delete_index_mesh
    __del__ = lambda self: None
index_mesh_swigregister = _example.index_mesh_swigregister
index_mesh_swigregister(index_mesh)

class legendre_mesh(base_mesh):
    __swig_setmethods__ = {}
    for _s in [base_mesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, legendre_mesh, name, value)
    __swig_getmethods__ = {}
    for _s in [base_mesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, legendre_mesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _example.new_legendre_mesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def extent(self):
        return _example.legendre_mesh_extent(self)

    def __call__(self, idx):
        return _example.legendre_mesh___call__(self, idx)

    def __eq__(self, mesh):
        return _example.legendre_mesh___eq__(self, mesh)

    def __ne__(self, mesh):
        return _example.legendre_mesh___ne__(self, mesh)

    def beta(self):
        return _example.legendre_mesh_beta(self)

    def statistics(self):
        return _example.legendre_mesh_statistics(self)

    def swap(self, other):
        return _example.legendre_mesh_swap(self, other)

    def save(self, ar, path):
        return _example.legendre_mesh_save(self, ar, path)

    def load(self, ar, path):
        return _example.legendre_mesh_load(self, ar, path)

    def check_range(self):
        return _example.legendre_mesh_check_range(self)

    def compute_points(self):
        return _example.legendre_mesh_compute_points(self)
    __swig_destroy__ = _example.delete_legendre_mesh
    __del__ = lambda self: None
legendre_mesh_swigregister = _example.legendre_mesh_swigregister
legendre_mesh_swigregister(legendre_mesh)


def __lshift__(*args):
    return _example.__lshift__(*args)
__lshift__ = _example.__lshift__
class can_have_tail_yes(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, can_have_tail_yes, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, can_have_tail_yes, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _example.new_can_have_tail_yes()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _example.delete_can_have_tail_yes
    __del__ = lambda self: None
can_have_tail_yes_swigregister = _example.can_have_tail_yes_swigregister
can_have_tail_yes_swigregister(can_have_tail_yes)

class can_have_tail_no(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, can_have_tail_no, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, can_have_tail_no, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _example.new_can_have_tail_no()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _example.delete_can_have_tail_no
    __del__ = lambda self: None
can_have_tail_no_swigregister = _example.can_have_tail_no_swigregister
can_have_tail_no_swigregister(can_have_tail_no)


def __lshift__(s, data):
    return _example.__lshift__(s, data)
__lshift__ = _example.__lshift__
class LegendreGF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LegendreGF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LegendreGF, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _example.new_LegendreGF(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def data(self):
        return _example.LegendreGF_data(self)

    def mesh1(self):
        return _example.LegendreGF_mesh1(self)

    def __call__(self, *args):
        return _example.LegendreGF___call__(self, *args)

    def initialize(self):
        return _example.LegendreGF_initialize(self)

    def norm(self):
        return _example.LegendreGF_norm(self)

    def __iadd__(self, rhs):
        return _example.LegendreGF___iadd__(self, rhs)

    def __isub__(self, rhs):
        return _example.LegendreGF___isub__(self, rhs)

    def __imul__(self, scalar):
        return _example.LegendreGF___imul__(self, scalar)

    def __itruediv__(self, *args):
        return _example.LegendreGF___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __neg__(self):
        return _example.LegendreGF___neg__(self)

    def save(self, ar, path):
        return _example.LegendreGF_save(self, ar, path)

    def load(self, ar, path):
        return _example.LegendreGF_load(self, ar, path)
    __swig_destroy__ = _example.delete_LegendreGF
    __del__ = lambda self: None
LegendreGF_swigregister = _example.LegendreGF_swigregister
LegendreGF_swigregister(LegendreGF)

class OmegaGF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OmegaGF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OmegaGF, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _example.new_OmegaGF(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def data(self):
        return _example.OmegaGF_data(self)

    def mesh1(self):
        return _example.OmegaGF_mesh1(self)

    def __call__(self, *args):
        return _example.OmegaGF___call__(self, *args)

    def initialize(self):
        return _example.OmegaGF_initialize(self)

    def norm(self):
        return _example.OmegaGF_norm(self)

    def __iadd__(self, rhs):
        return _example.OmegaGF___iadd__(self, rhs)

    def __isub__(self, rhs):
        return _example.OmegaGF___isub__(self, rhs)

    def __imul__(self, scalar):
        return _example.OmegaGF___imul__(self, scalar)

    def __itruediv__(self, *args):
        return _example.OmegaGF___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __neg__(self):
        return _example.OmegaGF___neg__(self)

    def save(self, ar, path):
        return _example.OmegaGF_save(self, ar, path)

    def load(self, ar, path):
        return _example.OmegaGF_load(self, ar, path)
    __swig_destroy__ = _example.delete_OmegaGF
    __del__ = lambda self: None
OmegaGF_swigregister = _example.OmegaGF_swigregister
OmegaGF_swigregister(OmegaGF)

# This file is compatible with both classic and new-style classes.


