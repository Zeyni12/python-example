import numpy as np 
from scipy.optimize import linear_sum_assignment

cost_matrix = np.array([[20,30,40,50,80],
                        [4,5,6,17,20],
                        [2,3,4,38,40],
                        [5,10,15,7,12],
                        [1,3,4,5,6]])
row_ind, col_ind =linear_sum_assignment(cost_matrix)
opt_ass = col_ind 
tc = cost_matrix[row_ind, col_ind].sum()
print(opt_ass)
print('Total assignment cost is %d' %tc)