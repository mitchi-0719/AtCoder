
from collections.abc import MutableSet, Sequence, Set
from itertools import chain
from operator import eq, ne, gt, ge, lt, le

from .sortedlist import SortedList, recursive_repr

class SortedSet(MutableSet, Sequence):

    def __init__(self, iterable=None, key=None):
        self._key = key

        if not hasattr(self, "_set"):
            self._set = set()

        self._list = SortedList(self._set, key=key)

        _set = self._set
        self.isdisjoint = _set.isdisjoint
        self.issubset = _set.issubset
        self.issuperset = _set.issuperset

        _list = self._list
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset

        if key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key

        if iterable is not None:
            self._update(iterable)

    @classmethod
    def _fromset(cls, values, key=None):
        sorted_set = object.__new__(cls)
        sorted_set._set = values
        sorted_set.__init__(key=key)
        return sorted_set

    @property
    def key(self):
        return self._key

    def __contains__(self, value):
        return value in self._set

    def __getitem__(self, index):
        return self._list[index]

    def __delitem__(self, index):
        _set = self._set
        _list = self._list
        if isinstance(index, slice):
            values = _list[index]
            _set.difference_update(values)
        else:
            value = _list[index]
            _set.remove(value)
        del _list[index]

    def __make_cmp(set_op):
        def comparer(self, other):
            if isinstance(other, SortedSet):
                return set_op(self._set, other._set)
            elif isinstance(other, Set):
                return set_op(self._set, other)
            return NotImplemented

        set_op_name = set_op.__name__
        comparer.__name__ = "__{0}__".format(set_op_name)
        return comparer

    __eq__ = __make_cmp(eq)
    __ne__ = __make_cmp(ne)
    __lt__ = __make_cmp(lt)
    __gt__ = __make_cmp(gt)
    __le__ = __make_cmp(le)
    __ge__ = __make_cmp(ge)

    def __len__(self):
        return len(self._set)

    def __iter__(self):
        return iter(self._list)

    def __reversed__(self):
        return reversed(self._list)

    def add(self, value):
        _set = self._set
        if value not in _set:
            _set.add(value)
            self._list.add(value)

    _add = add

    def clear(self):
        self._set.clear()
        self._list.clear()

    def copy(self):
        return self._fromset(set(self._set), key=self._key)

    __copy__ = copy

    def count(self, value):
        return 1 if value in self._set else 0

    def discard(self, value):
        _set = self._set
        if value in _set:
            _set.remove(value)
            self._list.remove(value)

    _discard = discard

    def pop(self, index=-1):

        value = self._list.pop(index)
        self._set.remove(value)
        return value

    def remove(self, value):
        self._set.remove(value)
        self._list.remove(value)

    def difference(self, *iterables):
        diff = self._set.difference(*iterables)
        return self._fromset(diff, key=self._key)

    __sub__ = difference

    def difference_update(self, *iterables):
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _set.difference_update(values)
            _list.clear()
            _list.update(_set)
        else:
            _discard = self._discard
            for value in values:
                _discard(value)
        return self

    __isub__ = difference_update

    def intersection(self, *iterables):
        intersect = self._set.intersection(*iterables)
        return self._fromset(intersect, key=self._key)

    __and__ = intersection
    __rand__ = __and__

    def intersection_update(self, *iterables):
        _set = self._set
        _list = self._list
        _set.intersection_update(*iterables)
        _list.clear()
        _list.update(_set)
        return self

    __iand__ = intersection_update

    def symmetric_difference(self, other):
        diff = self._set.symmetric_difference(other)
        return self._fromset(diff, key=self._key)

    __xor__ = symmetric_difference
    __rxor__ = __xor__

    def symmetric_difference_update(self, other):
        _set = self._set
        _list = self._list
        _set.symmetric_difference_update(other)
        _list.clear()
        _list.update(_set)
        return self

    __ixor__ = symmetric_difference_update

    def union(self, *iterables):
        return self.__class__(chain(iter(self), *iterables), key=self._key)

    __or__ = union
    __ror__ = __or__

    def update(self, *iterables):
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _list = self._list
            _set.update(values)
            _list.clear()
            _list.update(_set)
        else:
            _add = self._add
            for value in values:
                _add(value)
        return self

    __ior__ = update
    _update = update

    def __reduce__(self):
        return (type(self), (self._set, self._key))

    @recursive_repr()
    def __repr__(self):
        _key = self._key
        key = "" if _key is None else ", key={0!r}".format(_key)
        type_name = type(self).__name__
        return "{0}({1!r}{2})".format(type_name, list(self), key)

    def _check(self):
        _set = self._set
        _list = self._list
        _list._check()
        assert len(_set) == len(_list)
        assert all(value in _set for value in _list)
