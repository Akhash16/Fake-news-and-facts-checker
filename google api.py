from googleapiclient.discovery import build

API_KEY='AIzaSyBEbc15F1s35_bgvC8eupXt0MpGkV92PnA'
SERVICE=build("factchecktools","v1alpha1",developerKey=API_KEY)
userQuery="sunlight kills coronavirus"
request1=SERVICE.claims().search(query=userQuery)
response=request1.execute()
if not bool(response):
    print("no info")
else:
    claim = response['claims'][0]['claimReview'][0]['textualRating']
    source = response['claims'][0]['claimReview'][0]['publisher']['name']
    url = response['claims'][0]['claimReview'][0]['url']
    print(claim,'\n',source,'\n',url)