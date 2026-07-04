
import warnings

from collections.abc import ItemsView, KeysView, Mapping, Sequence, ValuesView
from itertools import chain

from .sortedlist import SortedList, recursive_repr
from .sortedset import SortedSet

class SortedDict(dict):

    def __init__(self, *args, **kwargs):
        if args and (args[0] is None or callable(args[0])):
            _key = self._key = args[0]
            args = args[1:]
        else:
            _key = self._key = None

        self._list = SortedList(key=_key)

        _list = self._list
        self._list_add = _list.add
        self._list_clear = _list.clear
        self._list_iter = _list.__iter__
        self._list_reversed = _list.__reversed__
        self._list_pop = _list.pop
        self._list_remove = _list.remove
        self._list_update = _list.update

        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect_right
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if _key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        self._update(*args, **kwargs)

    @property
    def key(self):
        return self._key

    @property
    def iloc(self):

        try:
            return self._iloc
        except AttributeError:
            warnings.warn(
                "sorted_dict.iloc is deprecated." " Use SortedDict.keys() instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            _iloc = self._iloc = SortedKeysView(self)
            return _iloc

    def clear(self):
        dict.clear(self)
        self._list_clear()

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._list_remove(key)

    def __iter__(self):
        return self._list_iter()

    def __reversed__(self):
        return self._list_reversed()

    def __setitem__(self, key, value):
        if key not in self:
            self._list_add(key)
        dict.__setitem__(self, key, value)

    _setitem = __setitem__

    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(self.items(), other.items())
        return self.__class__(self._key, items)

    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(other.items(), self.items())
        return self.__class__(self._key, items)

    def __ior__(self, other):
        self._update(other)
        return self

    def copy(self):
        return self.__class__(self._key, self.items())

    __copy__ = copy

    @classmethod
    def fromkeys(cls, iterable, value=None):
        return cls((key, value) for key in iterable)

    def keys(self):
        return SortedKeysView(self)

    def items(self):
        return SortedItemsView(self)

    def values(self):
        return SortedValuesView(self)

    class _NotGiven(object):

        def __repr__(self):
            return "<not-given>"

    __not_given = _NotGiven()

    def pop(self, key, default=__not_given):
        if key in self:
            self._list_remove(key)
            return dict.pop(self, key)
        else:
            if default is self.__not_given:
                raise KeyError(key)
            return default

    def popitem(self, index=-1):
        if not self:
            raise KeyError("popitem(): dictionary is empty")

        key = self._list_pop(index)
        value = dict.pop(self, key)
        return (key, value)

    def peekitem(self, index=-1):
        key = self._list[index]
        return key, self[key]

    def setdefault(self, key, default=None):
        if key in self:
            return self[key]
        dict.__setitem__(self, key, default)
        self._list_add(key)
        return default

    def update(self, *args, **kwargs):
        if not self:
            dict.update(self, *args, **kwargs)
            self._list_update(dict.__iter__(self))
            return

        if not kwargs and len(args) == 1 and isinstance(args[0], dict):
            pairs = args[0]
        else:
            pairs = dict(*args, **kwargs)

        if (10 * len(pairs)) > len(self):
            dict.update(self, pairs)
            self._list_clear()
            self._list_update(dict.__iter__(self))
        else:
            for key in pairs:
                self._setitem(key, pairs[key])

    _update = update

    def __reduce__(self):
        items = dict.copy(self)
        return (type(self), (self._key, items))

    @recursive_repr()
    def __repr__(self):
        _key = self._key
        type_name = type(self).__name__
        key_arg = "" if _key is None else "{0!r}, ".format(_key)
        item_format = "{0!r}: {1!r}".format
        items = ", ".join(item_format(key, self[key]) for key in self._list)
        return "{0}({1}{{{2}}})".format(type_name, key_arg, items)

    def _check(self):
        _list = self._list
        _list._check()
        assert len(self) == len(_list)
        assert all(key in self for key in _list)

def _view_delitem(self, index):
    _mapping = self._mapping
    _list = _mapping._list
    dict_delitem = dict.__delitem__
    if isinstance(index, slice):
        keys = _list[index]
        del _list[index]
        for key in keys:
            dict_delitem(_mapping, key)
    else:
        key = _list.pop(index)
        dict_delitem(_mapping, key)

class SortedKeysView(KeysView, Sequence):

    __slots__ = ()

    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)

    def __getitem__(self, index):
        return self._mapping._list[index]

    __delitem__ = _view_delitem

class SortedItemsView(ItemsView, Sequence):

    __slots__ = ()

    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)

    def __getitem__(self, index):
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [(key, _mapping[key]) for key in keys]

        key = _mapping_list[index]
        return key, _mapping[key]

    __delitem__ = _view_delitem

class SortedValuesView(ValuesView, Sequence):

    __slots__ = ()

    def __getitem__(self, index):
        _mapping = self._mapping
        _mapping_list = _mapping._list

        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [_mapping[key] for key in keys]

        key = _mapping_list[index]
        return _mapping[key]

    __delitem__ = _view_delitem
