import json

print('Loading function')

def lambda_handler(event, context):

    # BELOW IS EXAMPLE CODE GENERATED BY AN AWS LAMBDA FUNCTION TEMPLATE USED FOR TESTING.
    # #print("Received event: " + json.dumps(event, indent=2))
    # print("value1 = " + event['key1'])
    # print("value2 = " + event['key2'])
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    # #raise Exception('Something went wrong')
    
    payload = json.loads(event['body'])
    html_url = payload['issue']['html_url']
    print(html_url)
