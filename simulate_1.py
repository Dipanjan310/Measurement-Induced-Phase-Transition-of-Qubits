import numpy as np
import state_visualization as sv
from numba import prange, njit

@njit(cache=True,parallel=True)
def single_qubit(initial_state,op,site,N):
    
    final_state=np.zeros(2**N, dtype = np.complex128)
    r = 2**(N-site)
    for i in prange(2**N):
        
        q = int((r & i)/r)
        q_bar = 1^q
        r_bar = r^i
        final_state[i] = op[q,q]*initial_state[i] + op[q,q_bar]*initial_state[r_bar]
    return final_state

# def func():
            
#     H=np.zeros((2,2))+0*1j
    
#     H[0,0]=1
#     H[0,1]=1
#     H[1,0]=1
#     H[1,1]=-1

#     H=H/2**0.5
#     N = 3
#     m = 2 
#     initial_state = np.zeros(2**N, dtype = np.complex128)
#     initial_state[m] = 1
#     final_state=initial_state.copy()
#     for i in range(1,N+1,1):
#         site = i
        
        
#         #sv.visualize_state(single_qubit(initial_state, H, site, N), N)
#         final_state=single_qubit(final_state, H, site, N)
#     sv.visualize_state(final_state, N)

# # func()    













# def sin1(initial_state, op, site, N):
#     final_state = np.zeros(2**N, dtype = np.complex128)
#     r = 2**(N-site) 
#     for i in range(2**N):
#        q = int((r & i)/r)
#        q_bar = 1^q
#        r_bar = r^i
#        final_state[i] = op[q,q]*initial_state[i]+op[q,q_bar]*initial_state[r_bar]
#     return final_state
        
# def sin():
#     H = np.zeros((2,2))+0*1j
#     H[0,0] = 1
#     H[0,1] = 1
#     H[1,0] = 1
#     H[1,1] = -1
#     H = H/2**0.5
    
#     N = 3
#     site = 2
#     initial_state = np.zeros(2**N, dtype=np.complex128)
#     initial_state[0] = 1
#     final_state = sin1(initial_state, H, site, N)
#     sv.visualize_state(initial_state, N)
#     sv.visualize_state(final_state, N)
#     print(final_state)    
# sin()
    






    
    
    
    
    
    
    
    