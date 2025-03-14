import numpy as np
import simulate_1 as s1
import single_qubit_gates as sqg

def measurement(initial_state,pos, N):
    a = (np.eye(2)+sqg.Z_gate())/2
    b = (np.eye(2)-sqg.Z_gate())/2
    p1 = s1.single_qubit(initial_state, a, pos, N)
    p = np.vdot(initial_state, p1)
    r = np.random.rand()
    if r<p:
        final_state = p1/np.sqrt(p)
        outcome = 1
    else:
        p2 = s1.single_qubit(initial_state, b, pos, N)
        final_state = p2/np.sqrt(1-p)
        outcome = -1
    return final_state, outcome    



# def measure(initial_state, op, site, N):
#     p1 = (np.eye(2)+sqg.Z_gate())
#     p2 = (np.eye(2)+sqg.Z_gate())
#     p3 = s2.two_qubit(initial_state, p1, site, N)
#     p = np.vdot(initial_state,p3)
#     r = np.random.rand()
#     if r<p:
#         final_state = p1/np.sqrt(p)
#         outcome = 1
#     else:
#         p4 = s2.two_qubit(initial_state, p2, site, N)
#         final_state = p2/np.sqrt(1-p)
#         outcome = -1
#     return final_state, outcome