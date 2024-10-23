import boto3
import requests
from aws_lambda_powertools.utilities.data_classes import SQSEvent, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext


@event_source(data_class=SQSEvent)
def lambda_handler(event: SQSEvent, context: LambdaContext):
    payload: dict = {
        "FunctionName": "check_nws_api",
        "InvocationType": "LocalIncocation",
    }
    response = requests.post("https://httpbin.org/post", json=payload)
    return response.json()
