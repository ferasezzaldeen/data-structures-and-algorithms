import re
def repeated_word(string):
    string=string.lower()
    string=res = re.sub(r'[^\w\s]', '', string)
    words=re.split('\s+',string)
    print(words)
    check=[]
    for i in words:
        if i in check:
            return i
        else:
            check.append(i)
    return 'there is no repetetion'


if __name__=="__main__":
    print(repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'))

