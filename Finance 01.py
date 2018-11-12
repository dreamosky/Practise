# import numpy as np
# cashFlows=np.array([-100,50,40,30])
# for cash in cashFlows:
#     print(cash)

def npv_f(rate, cashflows):
    total = 0.0
    for i in range(0,len(cashflows)):
          total += cashflows[i] / (1 + rate)**i
    return total

r=0.03
caws=[-100,-30,10,40,50,45,20]
NPV=npv_f(r,caws)
print(NPV)