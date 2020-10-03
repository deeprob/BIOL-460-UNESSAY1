import allel
import numpy as np
import matplotlib.pyplot as plt

def get_pairwise_dist(g):
    d = allel.pairwise_distance(g.to_n_alt(),metric='cityblock')
    print(f'The mean pairwise distance within the population is {round(np.mean(d),2)}')
    allel.plot_pairwise_distance(d,labels=['Individual'+str(k) for k in range(g.shape[1])])
    plt.title('Pairwise Distance Matrix')
    return 

def get_fst(s1,s2):
    ac1 = s1.count_alleles()
    ac2 = s2.count_alleles()
    num, den = allel.hudson_fst(ac1, ac2)
    fst = np.sum(num) / np.sum(den)
    print(f'The F_st value between the two populations is {round(np.abs(fst),2)}')
    return 