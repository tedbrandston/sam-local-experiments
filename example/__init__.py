
import json
import os

def serializable(obj):
    """Just trying to get the serializable bits of context"""
    try:
        json.dumps(obj)
        return True
    except TypeError:
        return False

def echo(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'event': event,
            'context': {
                key: getattr(context, key) for key in dir(context) if serializable(getattr(context, key))
            },
            'environ': { key: os.environ[key] for key in os.environ }
        }, indent=2)
    }


def use_table(event, context):
    # It makes sense that this is empty when running locally,
    # but if my function needs to access a table I need to handle
    # this case _somehow_.
    table = os.environ['TABLE']

    return {
        'statusCode': 200 if table else 500,
        'body': json.dumps({'table': table})
    }
