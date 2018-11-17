import sys

print(sys.__loader__.create_module())

import zjazd_do_bazy_3.zadanie_6 as vec

vector = vec.Vector

v1 = vec.Vector(1,2)
v2 = vec.Vector(1,2)

print(v1+v2)

