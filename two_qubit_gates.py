import numpy as np
from numba import njit

#Controlled X gate (also called C-NOT or Controlled NOT gate
# )
@njit(cache=True)
def CX_gate():

    CX=np.zeros((4,4))+0*1j

    CX[0,0]=1
    CX[1,1]=1
    CX[2,3]=1
    CX[3,2]=1

    return CX

#Controlled Y gate
@njit(cache=True)
def CY_gate():

    CY=np.zeros((4,4))+0*1j

    CY[0,0]=1
    CY[1,1]=1
    CY[2,3]=-1j
    CY[3,2]=1j

    return CY

#Controlled Z gate
@njit(cache=True)
def CZ_gate():

    CZ=np.zeros((4,4))+0*1j

    CZ[0,0]=1
    CZ[1,1]=1
    CZ[2,2]=1
    CZ[3,3]=-1

    return CZ

@njit(cache=True)
def SWAP_gate():

    swap=np.zeros((4,4))+0*1j

    swap[0,0]=1
    swap[3,3]=1
    swap[1,2]=1
    swap[2,1]=1

    return swap

@njit(cache=True)
def PHASE_gate(theta):
    
    CP = np.zeros((4,4))+0*1j
    
    CP[0,0] = 1
    CP[1,1] = 1
    CP[2,2] = 1
    CP[3,3] = np.exp(-1j * theta)
    
    return CP

@njit(cache=True)
def PSWAP_gate(theta):

    S=SWAP_gate()

    I4=np.eye(4)

    PS=np.cos(theta)*I4 - 1j*np.sin(theta)*S

    return PS


