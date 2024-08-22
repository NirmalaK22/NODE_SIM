import importlib

Bpsim_0200=importlib.import_module('Bpsim_0200')
Bpnode=importlib.import_module('Bpnode')
TestrailResults=importlib.import_module('TestrailResults')

input_data_1863='{\
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
   "Amount": "1863",\
   "CashAmt": "0",\
   "Tag57": "4065870000001230=26012222222222222222",\
   "Cvc": "987",\
   "RespCode": "00",\
   "MsgOverride": [["049","A","643"],["022","A","51010151310C001"],["041","A","66000002"],["042","A","42298501010101"],["048","A","8000"],["048.1","A","6699001500000500000"],["049","A","008"]]\
  }\
 }\
}'

def C1863_Sale_Tip(testrail_run_id):
    print("C1863 test started.....")
    bpsim_out= Bpsim_0200.transaction_0200_POS(input_data_1863)
    bpnode_transaction_history= Bpnode.transactions("18") #must be correct
    bpnode_event = Bpnode.events("currency") #no events

    if bpsim_out is None and (bpnode_event is None and '18' in bpnode_transaction_history):
        print("case passed---Expected results:  response is sent back to TermApp POS bpsim device,Event is not raised,Transaction is counted,no warnings in events")
        case_id = "1863"
        status_id = "1"  # for pass
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed-C1863")
        case_id = "1863"
        status_id = "5"  # for fail
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
