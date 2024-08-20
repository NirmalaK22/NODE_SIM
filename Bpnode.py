import requests
from datetime import datetime, timezone,timedelta
import json
import Config


current_time = datetime.now(timezone.utc)
time_few_mins_ago = current_time - timedelta(0,30)
formatted_time = time_few_mins_ago.strftime("%Y-%m-%d %H:%M:%S.%f0 +02:00")
current_time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S.%f0 +02:00")

batch_cmd={
  "destination":"BatchManager",
   "messageType":"BatchEntitiesRead",
   "apiKey":Config.BPNODE_API_KEY,
   "data":{
      "parameters":{
         "from":"2024-07-22 08:51:00.0000000 +02:00",
         "to":"2024-07-22 09:52:12.1530000 +02:00"
      }
   }
}

transaction_cmd_from_to={
  "destination":"Transaction",
   "messageType":"TransactionsRead",
   "apiKey":Config.BPNODE_API_KEY,
   "data":{
      "parameters":{
         "from": formatted_time,
         "to": current_time_formatted
      }
   }
}
transaction_cmd={
  "destination":"Transaction",
   "messageType":"TransactionsRead",
   "apiKey":Config.BPNODE_API_KEY,
   "data":{
      "parameters":{

      }
   }
}

eventHandler_cmd={
  "destination":"EventHandler",
   "messageType":"EventsRead",
   "apiKey":Config.BPNODE_API_KEY,
   "data":{
      "parameters":{
         "from":formatted_time,
         "to":current_time_formatted
      }
   }
}
saf_cmd={
   "destination":"StoreAndForwardQueue",
   "messageType":"QueuesRead",
   "apiKey":Config.BPNODE_API_KEY
}
url =Config.BPNODE_API_URL

def events(message1=None):
    r = requests.post(url, json=eventHandler_cmd, verify=False)
    print(r.status_code)
    if r.status_code ==200:
        bpnode_content=json.loads(r.text)
        bpnode_events=bpnode_content['events']
        for i in range(len(bpnode_events)):
            #print("event message: ",bpnode_events[i])
            if message1 in bpnode_events[i]["message"]:
                event_message=bpnode_events[i]['message']
                print("Event raised ")
                return event_message
def transactions(amountValue=None):
    global terminal_id,terminal_value
    r = requests.post(url, json=transaction_cmd, verify=False)
    print(r.status_code)
    if r.status_code == 200:
        bpnode_content = json.loads(r.text)
        transaction_message = bpnode_content['data']
        for i in range(len(transaction_message)):
            #print("transaction.json message read: ",transaction_message[i])
            if amountValue in transaction_message[i]['amountValue']:
                terminal_value=transaction_message[i]['amountValue']
                #print("amount value: ",terminal_value)
                return terminal_value

def saf_queue():
    global saf_queue_name
    r = requests.post(url, json=saf_cmd, verify=False)
    print(r.status_code)
    if r.status_code == 200:
        bpnode_content = json.loads(r.text)
        if len(bpnode_content['queues']) > 1:
            saf_queue_name=bpnode_content['queues'][1]['name']
            print("SAF queue: ",bpnode_content['queues'][1]['name'])
            return saf_queue_name
        else:
            print("only default SAF queue found")
            return None




