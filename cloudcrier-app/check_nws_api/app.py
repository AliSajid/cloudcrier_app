import boto3
import requests


def lambda_handler(event, context):
    response = requests.get("https://httpbin.org/status/200")
    return response
