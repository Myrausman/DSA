from hashtable import HashTable
M=13
H=HashTable(M)
H.setprobfunc('double')

print('Size of Hash Table: ',len(H))
print('Load factor is defined {0}%: '.format(H.getLF()*100))
print('second hashkey constant: ',H.get2ndhkc())
print('probing method: ',H.getprobfunc())

data =[765, 431, 96, 142, 579, 226, 903, 388]
#data =[765, 431, 96, 142, 579, 226, 903, 388, 992,681,255,373,19,5,0]
for item in data:
    key = H.hashfunction(item,M)
    #print("h("+str(item)+") --> "+str(key))
    H.add(item)
H.add(19)
print(H.slots)
print(H.data)
print("New size of the hash table: ",len(H))

print('Search key : ',H.searchKey(7))
print('Search item: ',H.searchItem(2))
