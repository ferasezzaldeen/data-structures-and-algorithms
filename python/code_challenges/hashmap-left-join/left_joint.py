

def left_join(hash1,hash2):
    sol=[]
    for key in hash1:
        value1 = hash1[key]
        if key in hash2:
            value2 = hash2[key]

        else:
            value2 = None
        sol.append([key,value1,value2])
    return sol
    
            


if __name__ == '__main__':

    hash1 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outift': 'garb',
        'guide': 'usher',
    }

    hash2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }

    print(left_join(hash1,hash2))