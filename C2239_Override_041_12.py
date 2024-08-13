import importlib

sim1=importlib.import_module('Bpsim_0200')
bp1=importlib.import_module('Bpnode')
res1=importlib.import_module('TestrailResults')

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
   "Amount": "3333",\
   "CashAmt": "0",\
   "Tag57": "4065870000001230=26012222222222222222",\
   "Cvc": "987",\
   "RespCode": "00",\
   "MsgOverride": [["041","A","12"]]\
  }\
 }\
}'


def C2239_Override_041_12(testrail_run_id):

    bpsim_out= sim1.transaction_0200_POS(input_data)

    bpnode_event= bp1.events("unknown terminal")
    bpnode_transaction_history= bp1.transactions("12", "33")
    bpnode_saf= bp1.saf_queue()

    print("raised event: ", bpnode_event, "\nTerminal found: ", bpnode_transaction_history, "\nSAF queue: ", bpnode_saf)
    if "No Response" in bpsim_out and ("unknown terminal" in bpnode_event and bpnode_transaction_history is None and bpnode_saf is None):
        print("case passed---Expected results:  No response is sent back to TermApp POS bpsim device,Event is raised,Transaction is not counted, no record stored in SAF queue")
        case_id="2239"
        status_id="1"#for pass
        res1.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed")
        case_id = "2239"
        status_id = "5"  # for fail
        res1.post_testrail_results(testrail_run_id, case_id, status_id)