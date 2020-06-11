import json
import lambda_db

json_data = open('input.json')
event = json.load(json_data)
context = "context"

lambda_db.lambda_handler(event, context)
