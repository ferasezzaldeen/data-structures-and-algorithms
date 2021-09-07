
from hash import *


def left_join(hash1: HashTable,hash2:HashTable):
    sol=[]
    if hash1._buckets:
        for x in hash1._buckets:
            if x:
                current=x.head
                key=current.value[0]
                left_value=current.value[1]
                if hash2.get(key):
                    right_value=hash2.get(key)
                else:
                    right_value=None
                sol.append([key,left_value,right_value])
        return sol
    else:
        return 'left hashtable is empty'

            


if __name__ == '__main__':

    hash1 = HashTable()
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')
    hash1.add('diligent', 'employed')
    hash1.add('outfit', 'garb')
    hash1.add('guide', 'usher')

    hash2 = HashTable()
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')

    print(left_join(hash1, hash2))
            
