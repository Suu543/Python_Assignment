import time
from MyPyPackage.myModules import MyList, MySortings
from array import array

AR = array('i')
L = []
size = 50000
MyList.genRandList(L, size)

for x in L:
    AR.append(x)

print("Array (size: {}) before sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)
t1 = time.time()
MySortings.selectionSort(AR)
t2 = time.time()
print("Array (size: {}) after sorting : ".format(size))
MyList.printListSample(AR, size, 10, 2)
print("Selection sorting for array of {} integers took {} sec".format(size, t2 - t1))

print("List (size: {}) before sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)
t1 = time.time()
MySortings.selectionSort(L)
t2 = time.time()
print("List (size: {}) after sorting : ".format(size))
MyList.printListSample(L, size, 10, 2)
print("Selection sorting for array of {} integers took {} sec".format(size, t2-t1))