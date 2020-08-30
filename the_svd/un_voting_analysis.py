import numpy as np
import matplotlib.pyplot as plt

f = open('resources/UN_voting_data.txt')
country_list = []
voting_mat = []

for line in f:
    country, *voting_str = line.split()
    country_list.append(country)
    voting_vec = [int(string) for string in voting_str]
    voting_mat.append(voting_vec)

nof_countries = len(country_list)
nof_votes = len(voting_mat[0])
voting_arr = np.array(voting_mat)
centroid = [sum(voting_arr[j,i] for j in range(nof_countries))/nof_countries
            for i in range(nof_votes)]
norm_voting_arr = np.array([voting_arr[i] - centroid
                            for i in range(nof_countries)])
U, S, V = np.linalg.svd(norm_voting_arr, full_matrices=False)

for i, country in enumerate(country_list):
    x = norm_voting_arr[i]@V[0]
    y = norm_voting_arr[i]@V[1]
    ofs = 0.3
    plt.scatter(x, y)
    plt.text(x, y+ofs, country, fontsize=7, horizontalalignment='center')
plt.title('Plot of UN votes projected in a 2D-SVD space')
plt.show()
