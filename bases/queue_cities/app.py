import os

import boto3


def lambda_handler(event, context):
    sqs = boto3.resource("sqs")
    queue_name = os.environ["QUEUE_NAME"]
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    response = queue.send_message(MessageBody="Hello from Lambda!")
    return response
