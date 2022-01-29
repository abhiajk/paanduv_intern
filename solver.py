import numpy as np

class solve():
    def __init__(self, d1, d2):
        self.d1 = d1; #dia of pod
        self.d2 = d2;  #dia of tube
    def eqn_solver(self):
        d1=self.d1; #dia of pod
        d2=self.d2;  #dia of tube
        r = (d1**2/d2**2)
        a = 1/(1-r)*(1.728)
        b = -a
        coeff=[0.008,0,0.12,0,0.6,b,1]
        return np.roots(coeff).round(4)
        #for i in range(6):
            #print(s[i].round(4))

#s = solve(2,4)
#s.eqn_solver()
#display polynomial
#p = np.poly1d(coeff)
#print(p)
