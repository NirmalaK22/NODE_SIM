import requests
import json
import Config

def post_testrail_results(run_id,case_id,status_id):
    testrail_url = f'https://eftlab.testrail.io/index.php?/api/v2/add_result_for_case/{run_id}/{case_id}'
    user = Config.TESTRAIL_USER
    API_KEY=Config.TESTRAIL_API_KEY
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'status_id': status_id,
    }

    requests.post(testrail_url, auth=(user, API_KEY), headers=headers, data=json.dumps(payload))
    print("Testrail results pushed")
