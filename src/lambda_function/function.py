import boto3
import json
import logging.config

from uuid import uuid4

CLIENT = boto3.client('stepfunctions')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Processing event :{}'.format(json.dumps(event)))
    response = CLIENT.start_execution(
        stateMachineArn=event['stateMachineArn'],
        name=event.get('name', str(uuid4())),
        input=json.dumps(
            event.get('input', {}), 
            seperators=(',', ':')
        )
    )
    response['startDate'] = response['startDate'].isoformat()
    return response
