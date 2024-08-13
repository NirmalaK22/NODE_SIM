
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
    "CardEntry": "Chip EMV",\
    "GetMessages": true,\
    "step1": {\
      "Transaction": "Purchase",\
      "Track2": "5077300652344412=26012222222222222222",\
      "Cvc": "987",\
      "RespCode": "000",\
      "Amount": "1234",\
      "MsgOverride": [["022","A","50010120310C001"],["003","A","200000"]]\
    },\
    "step2": {\
      "Transaction": "Reversal",\
      "EmvApp": "None",\
      "Amount": "1234",\
      "CashAmt": "0",\
      "Cvc": "987",\
      "RespCode": "000",\
      "IssuerCmd": "Discard Message"\
    }\
  }\
}'

def C2241_Reversal_drop(testrail_run_id):
    bpsim_out = Bpsim_0200.transaction_0200_POS(input_data)
    bpnode_transaction_history = Bpnode.transactions('', "1234")
    bpnode_saf = Bpnode.saf_queue()
    print("Terminal found: ", bpnode_transaction_history, "\nSAF queue: ", bpnode_saf)

    if bpsim_out is None and ("1234" in bpnode_transaction_history and bpnode_saf is not None):
        print("TestCase passed---Expected results: transaction is counted to batch totals, response send back to TermApp POS device, record stored in store and forward queue")
        case_id = "2241"
        status_id = "1"  # for pass
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)
    else:
        print("testcase failed")
        case_id = "2241"
        status_id = "5"  # for fail
        TestrailResults.post_testrail_results(testrail_run_id, case_id, status_id)