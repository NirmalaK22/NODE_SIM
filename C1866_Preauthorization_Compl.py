import importlib

Bpsim_0200=importlib.import_module('Bpsim_0200')
Bpnode=importlib.import_module('Bpnode')
TestrailResults=importlib.import_module('TestrailResults')

input_data='{\
 "destination": "TestRunner",\
 "messageType": "Start",\
 "module": "POS",\
 "device": "TermApp POS 60020 OLTP1",\
 "data": {\
  "Name": "Nirmala test-0200",\
  "CardEntry": "In-App",\
  "GetMessages": true,\
  "step1": {\
   "Transaction": "Purchase",\
   "EmvApp": "None",\
   "Amount": "1866.0",\
   "CashAmt": "0",\
   "Tag57": "4065870000001230=26012222222222222222",\
   "Cvc": "987",\
   "RespCode": "00",\
   "MsgOverride": [["002","A","4889030000010013"],["003","C","000000"],["014","A","2501"],["022","A","210401234336003"],["023","A","434"],["024","A","100"],["025","A","1800"],["027","A","5"],["035","A","4889030000010013=25012011448360400001"],["037","A","907777777776"],["038","A","123456"],["039","A","000"],["040","A","321"],["045","A","B5183310043961234^JOHN/SMITH                ^24011010000323000"],["046","A","00036C0000020000000000C00000200036"],["049","A","036"],["059","A","12345678asd"]]\
  }\
 }\
}'

def C1866_Preauthorization_Compl(testrail_run_id):

    bpsim_out= Bpsim_0200.transaction_0200_POS(input_data)
    bpnode_transaction_history= Bpnode.transactions("18") #must be correct
    bpnode_event = Bpnode.events("currency") #no events

    if bpsim_out is None and (bpnode_event is None and '18' in bpnode_transaction_history):
        print("case passed---Expected results:  response is sent back to TermApp POS bpsim device,Event is not raised,Transaction is counted,no warnings in events")
        case_id = "1866"
        status_id = "1"  # for pass
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed-C1866")
        case_id = "1866"
        status_id = "5"  # for fail
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
