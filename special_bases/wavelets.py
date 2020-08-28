from math import sqrt, log2
from resources.image_mat_util import (file2image,
                                      isgray,
                                      color2gray,
                                      image2file,
                                      image2display,
                                      gray2color)

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

def forward2d(listlist):
    row_dlist = [forward(listlist[i]) for i in range(len(listlist))]
    col_ldict = dlist_transpose(row_dlist)
    return {k:forward(col_ldict[k]) for k in col_ldict}

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

def backward2d(dictdict):
    row_ldict = {k : backward(dictdict[k]) for k in dictdict}
    col_dlist = ldict_transpose(row_ldict)
    return [backward(D) for D in col_dlist]

def suppress(D, threshold):
    return dict((k,0) if (abs(D[k])<threshold) else (k,D[k]) for k in D)

def suppress2d(d_dict, threshold):
    return {k : suppress(d_dict[k], threshold) for k in d_dict}

def sparsity(D):
    return sum(1 if D[k] != 0 else 0 for k in D) / len(D)

def sparsity2d(d_dict):
    return sum(sparsity(d_dict[k]) for k in d_dict) / len(d_dict)

def dlist_transpose(dlist):
    return {k:[dlist[i][k] for i in range(len(dlist))] for k in dlist[0]}

def ldict_transpose(ldict):
    return [{k:ldict[k][i] for k in ldict} for i in range(len(ldict[(0,0)]))]

def image_round(llist):
    return [[int(round(item)) if item < 255 else 255 for item in row]
            for row in llist]

def main():
    filename = 'flag'
    img = color2gray(file2image('resources/'+filename+'.png'))
    print("Processing the ", filename, " picture;")
    wv_img = forward2d(img)
    threshold = float(input("What is the threshold? "))
    clean_wv_img = suppress2d(wv_img, threshold)
    print("The sparcity was %.2f%%;\nNow it is %.2f%%;"
          %(100*sparsity2d(wv_img), 100*sparsity2d(clean_wv_img)))
    clean_img = image_round(backward2d(clean_wv_img))
    output = filename + '_threshold_' + str(threshold) + '.png'
    image2file(clean_img, output)
    print("Image saved on '%s';" %output)

if __name__ == '__main__':
    main()

