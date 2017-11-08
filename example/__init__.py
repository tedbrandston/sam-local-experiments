
import json

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
            }
        }, indent=2)
    }