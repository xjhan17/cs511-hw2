# wff1 is the DNF
# wff2 is the CNF
from z3 import *

p1, p2, p3, p4 = Bools('p1 p2 p3 p4')

wff1 = Or(And(p1,p2,p3,p4), And(Not(p1),Not(p2),Not(p3),p4), \
		  And(Not(p1),Not(p2),p3,Not(p4)), And(Not(p1),p2,Not(p3),Not(p4)), \
		  And(p1,Not(p2),Not(p3),Not(p4)), And(p1,p2,Not(p3),Not(p4)), \
		  And(p1,Not(p2),Not(p3),p4), And(Not(p1),Not(p2),p3,p4), \
		  And(Not(p1),p2,p3,Not(p4)), And(p1,Not(p2),p3,Not(p4)), \
		  And(Not(p1),p2,Not(p3),p4), And(Not(p1),p2,p3,p4), \
		  And(p1,p2,p3,Not(p4)), And(p1,Not(p2),p3,p4), \
		  And(p1,p2,Not(p3),p4), And(Not(p1),Not(p2),Not(p3),Not(p4)))

wff2 = And(Or(p1,p2,p3,p4), Or(Not(p1),Not(p2),Not(p3),p4), \
		  Or(Not(p1),Not(p2),p3,Not(p4)), Or(Not(p1),p2,Not(p3),Not(p4)), \
		  Or(p1,Not(p2),Not(p3),Not(p4)), Or(p1,p2,Not(p3),Not(p4)), \
		  Or(p1,Not(p2),Not(p3),p4), Or(Not(p1),Not(p2),p3,p4), \
		  Or(Not(p1),p2,p3,Not(p4)), Or(p1,Not(p2),p3,Not(p4)), \
		  Or(Not(p1),p2,Not(p3),p4), Or(Not(p1),p2,p3,p4), \
		  Or(p1,p2,p3,Not(p4)), Or(p1,Not(p2),p3,p4), \
		  Or(p1,p2,Not(p3),p4), Or(Not(p1),Not(p2),Not(p3),Not(p4)))

wff3 = Not(Not((And(Or(p1,p2,p3,p4), Or(Not(p1),Not(p2),Not(p3),p4), \
		  Or(Not(p1),Not(p2),p3,Not(p4)), Or(Not(p1),p2,Not(p3),Not(p4)), \
		  Or(p1,Not(p2),Not(p3),Not(p4)), Or(p1,p2,Not(p3),Not(p4)), \
		  Or(p1,Not(p2),Not(p3),p4), Or(Not(p1),Not(p2),p3,p4), \
		  Or(Not(p1),p2,p3,Not(p4)), Or(p1,Not(p2),p3,Not(p4)), \
		  Or(Not(p1),p2,Not(p3),p4), Or(Not(p1),p2,p3,p4), \
		  Or(p1,p2,p3,Not(p4)), Or(p1,Not(p2),p3,p4), \
		  Or(p1,p2,Not(p3),p4), Or(Not(p1),Not(p2),Not(p3),Not(p4))))))


s = Solver()
s.add(wff2 == wff3)

print (s.check())


