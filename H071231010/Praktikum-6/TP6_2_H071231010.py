def cari_duplikat(arr1, arr2):
    set_arr1 = set(arr1)
    duplikat = set()
    
    for elemen in arr2:
        if elemen in set_arr1:
            duplikat.add(elemen)
            
    return list(duplikat)

arr1 = input("input array ke-1: ").split()
arr2 = input("input array ke-2: ").split()
duplikat = cari_duplikat(arr1, arr2)

if duplikat:
    print("elemen duplikat: ", duplikat)
else:
    print("tidak ada elemen duplikat.")