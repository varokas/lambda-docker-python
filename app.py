import requests

def handler(event, context):
  r = requests.get("https://api.covidtracking.com/v1/us/daily.json")
  j = r.json() 

  return [ {"states": r["states"], "positive": r["positive"]} for r in j]
