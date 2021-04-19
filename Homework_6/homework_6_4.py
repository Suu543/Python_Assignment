import time
from MyPyPackage.myModules import MyList, MySortings

while True:
    size = int(input("\nsize of list (0 to terminate) = ").strip())
    if (size < 2):
        print("정렬을 위해서는 List 길이는 최소 2 이상 되어야 합니다")
        
    L = []
    MyList.genRandList(L, size)
    print("\nList (size: {}) before merge sorting : ".format(size))
    MyList.printListSample(L, size, 10, 2)
    t1 = time.time()
    MySortings.mergeSort(L)
    t2 = time.time()
    print("\nList (size: {}) after merge sorting : ".format(size))
    MyList.printListSample(L, size, 10, 2)
    print("Merge sorting for list of {} integers took {} sec".format(size, t2 - t1))

    MyList.shuffleList(L)
    print("\nList (size: {}) before selection sorting : ".format(size))
    MyList.printListSample(L, size, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(L)
    t2 = time.time()
    print("\nList (size: {}) after selection sorting : ".format(size))
    MyList.printListSample(L, size, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2 - t1))

