import importlib
import sys

t1=importlib.import_module('C2239_Override_041_12')
t2=importlib.import_module('C2240_Override_052_differentValue')
t3=importlib.import_module('C2241_Reversal_drop')


args=sys.argv[1]
t1.C2239_Override_041_12(args)
print("********Testcase-1 completed*************")
t2.C2240_Override_052_differentValue(args)
print("********Testcase-2 completed*************")
t3.C2241_Reversal_drop(args)
print("********Testcase-3 completed*************")


