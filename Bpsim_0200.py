import json
import requests
import Config

def transaction_0200_POS(input_data):
    if "txt" in input_data:
        headers = {
        'Content-Type': 'text/plain',
    }
    else:
        headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(Config.THIN_CLIENT_API_URL, headers=headers, data=input_data)
    content = response.content
    #print("content of the file:\n", content)
    data = json.loads(content)
    #print("data: ",data)
    if "Timed Out" in data['Status']:
        print("bpsim response: ", data)
        return "No Response"
    if "Traffic" in data['Report']:
        print("bpsim response: ",data['Report']['Traffic'])

##############################*****************************************************************************#################################################


# print("data: ",data)
# if data['Success']:
#     raw_data = data['Report']['Traffic'][1]['FieldData']
#     fields = raw_data.split('\n')
#     for j in fields:
#         print(" ", j)
#         if 'Processing Code' in j:
#             proc_val = re.split(r'[.]+', j)
#             if len(proc_val) == 2:
#                 amount = proc_val[1]
#                 print("processing code value: ", amount)
#                 break
#     out_put_lines.close()
# else:
#     print("error: ",data)
