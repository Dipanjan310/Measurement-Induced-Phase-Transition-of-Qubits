import numpy as np


def visualize_state(state, N):

    configs=np.nonzero(state)[0]
    coeffs=state[configs]

    num_configs=len(configs)

    for i in range(num_configs):


        s='|'+f'{configs[i]:0{N}b}'+'>'

        print (round(coeffs[i],14), ' '+s)





    




