from math import sqrt, log2

def forward_no_normalization(vec):
    if len(vec) == 1:
        return {(0,0) : vec[0]}
    width = len(vec)//2
    v = [(vec[2*i]+vec[2*i+1])/2 for i in range(width)]
    w = {(width,i) : vec[2*i]-vec[2*i+1] for i in range(width)}
    return {**forward_no_normalization(v), **w}

def normalize_coefficients(n, D):
    return {(0,0):D[(0,0)]*sqrt(n),
            **{k : D[k]*sqrt(n/(4*k[0])) for k in D if k[0] != 0}}

def forward(v):
    return normalize_coefficients(len(v), forward_no_normalization(v))

def backward_no_normalization(D):
    n = len(D)
    v = [D[(0,0)]]*n
    forlist = [2**i for i in range(int(log2(n)))]
    for (i, rev_i) in zip(forlist, reversed(forlist)):
        w = sum([ [D[(i,j)]/2]*rev_i + [-D[(i,j)]/2]*rev_i
                  for j in range(i) ], [])
        v = [v[i]+w[i] for i in range(n)]
    return v

def unnormalize_coefficients(n, D):
    return {(0,0):D[(0,0)]/sqrt(n),
            **{k : D[k]/sqrt(n/(4*k[0])) for k in D if k[0] != 0}}

def backward(D):
    return backward_no_normalization(unnormalize_coefficients(len(D),D))

def suppress(D, threshold):
    return dict((k,0) if (abs(D[k])<threshold) else (k,D[k]) for k in D)

def sparsity(D):
    return sum(1 if D[k] != 0 else 0 for k in D) / len(D)

v = list(map(float, [4,5,3,7,4,5,2,3,9,7,3,5,0,0,0,0]))
w = list(map(float, [1,2,3,4]))

wvlet = forward(v)
rev_wvlet = backward(wvlet)
print(v)
print(wvlet)
print(rev_wvlet)
print(v == rev_wvlet)
