# This is a debugger so we dont have to use print
import pdb



x=[1,2,3]
y=2
z=3

# USING 'Trace' from pdb
# it allows you to pause mid script and explore variables
# to quit - input 'q'


result= y+z
pdb.set_trace()
result2= x+y

