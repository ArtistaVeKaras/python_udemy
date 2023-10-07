import os

def get_base_url():
    
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://demmostore.supersqa.com'
    elif env.lower() == 'prod':
        return 'http://demmostore.prod.supersqa.com'
    else:
        raise Exception('Unknown environment: %s' % env)

