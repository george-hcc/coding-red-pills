from resources.cancer_data import read_training_data
from resources.vec import Vec
from resources.matutil import mat2rowdict

def signum(u):
    sign = lambda x : 1 if x >= 0 else -1
    return Vec(u.D, {k:sign(u[k]) for k in u.D})

def fraction_wrong(A, b, w):
    return ((b*signum(A*w)/len(b))-1)/(-2)

def find_loss(A, b, w):
    h_y = A*w
    return sum((h_y[k]-b[k])**2 for k in b.D)

def find_grad(A, b, w):
    R = b.D
    C = w.D
    h_y = A*w
    return Vec(C, {c:2*sum((h_y[r]-b[r])*A[r,c] for r in R) for c in C})

def gradient_descent(A, b, w, step, T):
    for i in range(T):
        if i % 25 == 0:
            print(find_loss(A,b,w), fraction_wrong(A,b,w))
        change = -step*(find_grad(A, b, w))
        w += change
    return w

def main():
    # Training
    A, b = read_training_data('resources/train.data')
    init = Vec(A.D[1], {k:0 for k in A.D[1]})
    step = (10**(-9))
    iterations = 10000
    w = gradient_descent(A, b, init, step, iterations)
    print('Training Loss: ', find_loss(A, b, w))
    print('Training Wrong%: ', fraction_wrong(A, b, w)*100)
    # Validation
    A, b = read_training_data('resources/validate.data')
    print('Validation Loss: ', find_loss(A, b, w))
    print('Validation Wrong%: ', fraction_wrong(A, b, w)*100)    

if __name__ == '__main__':
    main()
