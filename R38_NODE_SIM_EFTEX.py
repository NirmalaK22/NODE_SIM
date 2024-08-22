import importlib

# t1=importlib.import_module('C2239_Override_041_12')
# t2=importlib.import_module('C2240_Override_052_differentValue')
# t3=importlib.import_module('C2241_Reversal_drop')
#args=sys.argv[1]
# args=43
# t1.C2239_Override_041_12(args)
# print("********Testcase-1 Completed*************")
# t2.C2240_Override_052_differentValue(args)
# print("********Testcase-2 completed*************")
# t3.C2241_Reversal_drop(args)
# print("********Testcase-3 completed*************")

saleTest=importlib.import_module('C1862_Sale')
saleTipTest=importlib.import_module('C1863_Sale_Tip')
onlineRefund=importlib.import_module('C1864_Online_refund')
preauthorization=importlib.import_module('C1865_Preauthorization')
preauthorizationCompl=importlib.import_module('C1866_Preauthorization_Compl')
preauthorizationComplDCurr=importlib.import_module('C1867_Preauthorization_Compl_Diff_Currency')
cancellation=importlib.import_module('C1868_Cancellation')
settlement=importlib.import_module('C1869_Settlement')




args=44
saleTest.C1862_Sale(args)
print("********Testcase-1862 completed*************")
saleTipTest.C1863_Sale_Tip(args)
print("********Testcase-1863 completed*************")
onlineRefund.C1864_Onine_Refund(args)
print("********Testcase-1864 completed*************")
preauthorization.C1865_Preauthorization(args)
print("********Testcase-1865 completed*************")
preauthorizationCompl.C1866_Preauthorization_Compl(args)
print("********Testcase-1866 completed*************")
preauthorizationComplDCurr.C1867_Preauthorization_Compl_Diff_Currency(args)
print("********Testcase-1867 completed*************")
cancellation.C1868_Cancellation(args)
print("********Testcase-1868 completed*************")
settlement.C1869_Settlement(args)
print("********Testcase-1869 completed*************")