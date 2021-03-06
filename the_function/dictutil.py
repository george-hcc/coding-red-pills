def dict2list(dct, keylist):
    return [dct[key] for key in keylist]

def list2dict(L, keylist):
    return {key:value for key, value in zip(keylist, L)}

def listrange2dict(L):
    return list2dict(L, range(len(L)))
