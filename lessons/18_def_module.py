from module import test1
from module.test2 import mod_2_test2
from module.test2 import mod_2_test3 as mt2


print(test1.mod_1_test2('roman'))

print(mod_2_test2('romanov'))

print(mt2('romanov roman'))