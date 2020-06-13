#!/usr/bin/python

# Pa-229 5/2 -> 5/2 parity changing decay rates.

E_gamma=10.e-6 # MeV
A=229

# Decay rates for transition types (formulae from Loveland, Morrissey,
# Seaborn Table 9.2)

E1=1.03e14*A**(2./3.)*E_gamma**3
M2=2.24e7*A**(4./3.)*E_gamma**5
E3=3.39e1*A**2*E_gamma**7
M4=3.27e-6*A**2*E_gamma**9
E5=2.40e-12*A**(10./3.)*E_gamma**11

print('For a photon energy of %e MeV'%E_gamma)
print('and for mass number A = %d'%A)
print('The E1 decay rate is %e s^{-1}'%E1)
print('The M2 decay rate is %e s^{-1}'%M2)
print('The E3 decay rate is %e s^{-1}'%E3)
print('The M4 decay rate is %e s^{-1}'%M4)
print('The E5 decay rate is %e s^{-1}'%E5)
