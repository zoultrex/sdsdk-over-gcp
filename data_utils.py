import json
def get_json_request_data(request):
    request_json = json.loads(request.data)
    return json.dumps(request_json)

    # did not work
    # for i,item in enumerate(data):
    #     data[i]["id"] = i
    # return data