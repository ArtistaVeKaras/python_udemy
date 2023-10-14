import os

def get_base_url():
    
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://demmostore.supersqa.com'
    elif env.lower() == 'production':
        return 'http://demmostore.prod.supersqa.com'
    else:
        raise Exception('Unknown environment: %s' % env)


def get_database_credentials():
    
    env = os.environ.get('ENV', 'test')

    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    if not db_user or not db_password:
        raise Exception('Environemnt variable "DB_USER" and "DB_PASSWORDi must be set!"')

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env == 'production':
        db_host = 'demostore.superqa.com'
        db_port = 3306
    else:
        raise Exception(f'Invalid environment: {env}')

    db_info = {'db_host': db_host, 'db_port': db_port,
               'db_user': db_user, 'db_password': db_password}

    return db_info