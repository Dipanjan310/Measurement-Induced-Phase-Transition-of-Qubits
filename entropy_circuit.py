import numpy as np
import single_qubit_gates as sqg
import two_qubit_gates as tqg
import simulate_1 as s1   
import simulate_2 as s2
import entropy as e
import matplotlib.pyplot as plt
import measurement as mt

# def sequantial_one_qubit_gate(initial_state, N):
#     X = sqg.X_gate()
#     H = sqg.Hadamard()
#     T = sqg.T_gate()
#     #Y = sqg.Y_gate()
    
#     for i in range(N):
#         a = np.random.randint(3)
#         if a==0:
#             initial_state = s1.single_qubit(initial_state, X, i+1, N)
#         elif a==1:
#             initial_state = s1.single_qubit(initial_state, H, i+1, N)
#         else:
#             initial_state = s1.single_qubit(initial_state, T, i+1, N)
            
#     return initial_state
    
# def sequential_two_qubit_gate(initial_state, N):
#     CX = tqg.CX_gate()
#     for i in range(N-1):
#         initial_state = s2.two_qubit(initial_state, CX, i+1, i+2, N)
#     return initial_state

# def measurement_layer(N, initial_state, p):
#     for i in range(1,N+1,1):
#         r = np.random.rand()
#         if r<= p:
#             initial_state , q =  mt.measurement(initial_state, i ,N)
            
#     return initial_state 

# '''measurement always reduces the entanglement, we are controlling the measurement using probability.
# if probability is 1 then we are measuring all the time thus there will be no entanglement.
# close to zero probability more entanglement. '''
    

# def final_operation(N, p):
#     E = [] 
#     # F = []
#     initial_state = np.zeros(2**N, dtype = np.complex128)
#     initial_state[0] = 1
#     for i in range(30):
#         initial_state = sequantial_one_qubit_gate(initial_state, N)
#         initial_state = sequential_two_qubit_gate(initial_state, N)
#         initial_state = measurement_layer(N, initial_state, p)
#         E.append(e.calculate_entropy(initial_state, int(N/2), N))
#         # cp = abs(initial_state)**2
#         # cq = -np.sum(cp*np.log(cp+1e-45))
#         # F.append(cq)
#   # return E, F
      # return E

# N = 10
# M = (N/2)*np.log(2)-1/2
# P = N*np.log(2)-1+0.577
# num_step = np.arange(1,31,1)
# # A, B = final_operation(N, 0.001)
# A = final_operation(N, 0.001)
# plt.plot(num_step,A)
# # plt.plot(num_step,B) 
# plt.axhline(M) 
# # plt.axhline(P)
# plt.show()
 
# ''' "blue" line indicates the how much entangled it is,
# and "orange" line indicates how much use the hilbert space'''














 



def one_q(initial_state, N):
    X =sqg.X_gate()
    H = sqg.Hadamard()
    T = sqg.T_gate()
    for i in range(N):
        a = np.random.randint(3)
        if a == 0:
            initial_state = s1.single_qubit(initial_state,X, i+1, N) 
        elif a == 1:
            initial_state = s1.single_qubit(initial_state,H, i+1, N) 
        else:
            initial_state = s1.single_qubit(initial_state,T, i+1, N) 
    return initial_state
    
def two_q(initial_state, N):
    CX = tqg.CX_gate()
    for i in range(N-1):
        initial_state = s2.two_qubit(initial_state, CX, i+1, i+2, N)
    return initial_state

def measurement(initial_state, p, N):
    for i in range(1, N+1, 1):
        r = np.random.rand()
        if r<=p:
            initial_state, q = mt.measurement(initial_state, i, N)
        return initial_state 
        

def total_func(N, p):
    E = []
    initial_state = np.zeros(2**N, dtype = np.complex128)
    initial_state[0] = 1
    for i in range(50):
        initial_state = one_q(initial_state, N)
        initial_state = two_q(initial_state, N)
        initial_state = measurement(initial_state, p, N)
        E.append(e.calculate_entropy(initial_state, int(N/2), N))
    return E

# def avg_many_time(N,p):
#     A = []
#     for i in range(100):
#         A.append(total_func(N, p))
#     B = np.zeros(50)
#     for i in range(100):
#         for j in range(50):
#             B[j] += A[i][j]
#     return B/100

N = 10
M = (N/2)*np.log(2) - 1/2
# P = N*np.log(2)-1+0.577
num_step = np.arange(1, 51, 1)
A = total_func(N, 0.0001)
# A = avg_many_time(N, 0.2)
plt.plot(num_step, A)
plt.axhline(M)
plt.show()


'''
total funtion run for 100 times store 100 array results in one array
add 
    '''
    