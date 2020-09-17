from googleapiclient.discovery import build

MAX_CLAIMS=3
API_KEY='AIzaSyBEbc15F1s35_bgvC8eupXt0MpGkV92PnA'
API='fsactchecktools'
SERVICE=build("factchecktools","v1alpha1",developerKey=API_KEY)
userQuery="Covid 19 test is a dangerous test, and that the nasal swab test can enter the brain and cause lasting damage"
request=SERVICE.claims().search(query=userQuery)
response=request.execute()
print(response)
