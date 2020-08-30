import numpy as np
import matplotlib.pyplot as plt

f = open('resources/US_Senate_voting_data_109.txt')
sen_list = []
voting_mat = []

for line in f:
    sen, party, state, *voting_str = line.split()
    sen_list.append((sen, party, state))
    voting_vec = [int(string) for string in voting_str]
    voting_mat.append(voting_vec)

voting_arr = np.array(voting_mat)
centroid = [sum(voting_arr[j,i] for j in range(99))/99 for i in range(46)]
norm_voting_arr = np.array([voting_arr[i] - centroid for i in range(99)])
U, S, V = np.linalg.svd(norm_voting_arr, full_matrices=False)

for i, tup in enumerate(sen_list):
    color = 'blue' if tup[1] == 'D' else 'red'
    group = 'Democrats' if tup[1] == 'D' else 'Republicans'
    x = norm_voting_arr[i]@V[0]
    y = norm_voting_arr[i]@V[1]
    ofs = 0.1
    plt.scatter(x, y, c=color, label=group)
    plt.text(x, y+ofs, tup[0], fontsize=7, c=color)
plt.title('Plot of US Senators votes projected in a 2D-SVD space')
plt.legend(('Democrats', 'Republicans'))
plt.show()
