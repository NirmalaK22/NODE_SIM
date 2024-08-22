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
   "Amount": "1865.0",\
   "CashAmt": "0",\
   "Tag57": "4065870000001230=26012222222222222222",\
   "Cvc": "987",\
   "RespCode": "00",\
   "MsgOverride": [["003","C","000000"],["022","A","51010151310C001"],["041","A","66000002"],["042","A","42298501010101"],["048","A","8000"],["048.1","A","6699001500000500000"]]\
  }\
 }\
}'

def C1865_Preauthorization(testrail_run_id):

    bpsim_out= Bpsim_0200.transaction_0200_POS(input_data)
    bpnode_transaction_history= Bpnode.transactions("65") #must be correct
    bpnode_event = Bpnode.events("currency") #no events

    if bpsim_out is None and (bpnode_event is None and '65' in bpnode_transaction_history):
        print("case passed---Expected results:  response is sent back to TermApp POS bpsim device,Event is not raised,Transaction is counted,no warnings in events")
        case_id = "1865"
        status_id = "1"  # for pass
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed-C1865")
        case_id = "1865"
        status_id = "5"  # for fail
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
