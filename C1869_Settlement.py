
import importlib

Bpsim_0200=importlib.import_module('Bpsim_0200')
Bpnode=importlib.import_module('Bpnode')
TestrailResults=importlib.import_module('TestrailResults')

#step-1->purchase,step-2-1420,step-3->1520(settlement)


input_data='{\
  "destination": "TestRunner",\
  "messageType": "Start",\
  "module": "POS",\
  "device": "TermApp POS 60020 OLTP1",\
  "data": {\
    "Name": "Nirmala test-0200",\
    "CardEntry": "Chip EMV",\
    "GetMessages": true,\
    "step1": {\
      "Transaction": "Purchase",\
      "Track2": "5077300652344412=26012222222222222222",\
      "Cvc": "987",\
      "RespCode": "000",\
      "Amount": "1869",\
      "MsgOverride": [["003","C","000000"],["022","A","51010151310C001"],["041","A","66000002"],["042","A","42298501010101"],["048","A","8000"],["048.1","A","6699001500000500000"]]\
    },\
    "step2": {\
      "Transaction": "Purchase",\
      "EmvApp": "None",\
      "Amount": "1869",\
      "CashAmt": "0",\
      "Cvc": "987",\
      "RespCode": "000",\
      "MsgOverride": [["022","A","230401234336003"],["003","C","000000"],["022","A","51010151310C001"],["041","A","66000002"],["042","A","42298501010101"],["048","A","8000"],["048.1","A","6699001500000500000"]]\
    },\
    "step2": {\
      "Transaction": "Purchase",\
      "EmvApp": "None",\
      "Amount": "1869",\
      "CashAmt": "0",\
      "Cvc": "987",\
      "RespCode": "000",\
      "MsgOverride": [["050","A","036"],["076","A","0000000000"],["003","C","000000"],["022","A","51010151310C001"],["041","A","66000002"],["042","A","42298501010101"],["048","A","8000"],["048.1","A","6699001500000500000"]]\
    }\
  }\
}'

def C1869_Settlement(testrail_run_id):
    bpsim_out = Bpsim_0200.transaction_0200_POS(input_data)
    bpnode_transaction_history = Bpnode.transactions("69")  # must be correct
    bpnode_event = Bpnode.events("currency")  # no events

    if bpsim_out is None and (bpnode_event is None and '69' in bpnode_transaction_history):
        print("case passed---Expected results:  response is sent back to TermApp POS bpsim device,Event is not raised,Transaction is counted,no warnings in events")
        case_id = "1869"
        status_id = "1"  # for pass
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed-C1869")
        case_id = "1869"
        status_id = "5"  # for fail
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)