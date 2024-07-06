k, g, m = map(int, input().split())

_g = 0
_m = 0

for i in range(k):
    if _g == g:
        _g = 0
    elif _m == 0:
        _m = m
    else:
        if _m < g - _g:
            _g += _m
            _m = 0
        else:
            _m -= g - _g
            _g = g

print(_g, _m)
