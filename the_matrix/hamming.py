from resources.mat import Mat
from resources.vec import Vec
from resources.GF2 import one, zero
from resources.matutil import mat2coldict, coldict2mat
from resources.bitutil import str2bits, bits2str, bits2mat, mat2bits, noise

G = Mat((set(range(7)), set(range(4))),
        {(0,0):one, (0,2):one, (0,3):one,
         (1,0):one, (1,1):one, (1,3):one,
         (2,3):one,
         (3,0):one, (3,1):one, (3,2):one,
         (4,2):one,
         (5,1):one,
         (6,0):one,})
H = Mat((set(range(3)), set(range(7))),
        {(0,3):one, (0,4):one, (0,5):one, (0,6):one,
         (1,1):one, (1,2):one, (1,5):one, (1,6):one,
         (2,0):one, (2,2):one, (2,4):one, (2,6):one,})
R = Mat((set(range(4)), set(range(7))),
        {(0,6):one, (1,5):one, (2,4):one, (3,2):one,})

def find_error(error_synd):
    assert len(error_synd) == 3
    error_vec = Vec(set(range(7)), {})
    for col in H.D[1]:
        if sum(error_synd[row] == H[(row,col)] for row in range(3)) == 3:
            error_vec[col] = one
    return error_vec

def find_error_mat(error_synd_mat):
    coldict = mat2coldict(error_synd_mat)
    return coldict2mat({k:find_error(coldict[k]) for k in coldict})

def main():
    string = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."
    bitmat_str = bits2mat(str2bits(string))
    tx_msg = G*bitmat_str
    rx_msg = tx_msg + noise(tx_msg, 0.02)
    fixd_rx_msg = rx_msg + find_error_mat(H*rx_msg)
    rcvd_string = bits2str(mat2bits(R*rx_msg))
    fixd_rcvd_string = bits2str(mat2bits(R*fixd_rx_msg))
    print("Original message is:\n", string, "\n")
    print("Received is:\n", rcvd_string, "\n")
    print("Fixed message is:\n", fixd_rcvd_string, "\n")


if __name__ == '__main__':
    main()
