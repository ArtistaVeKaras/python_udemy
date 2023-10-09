import pymysql 
from ssqatest.src.helpers.config_helpers import get_database_credentials
from ssqatest.src.configs.generic_configs import GenericConfig

def read_from_db(sql):
   
    db_cred = get_database_credentials() 

    # connect to database 
    connetion = pymysql.connect(host=db_cred['db_host'], port=db_cred['db_port'],
                                user=db_cred['db_user'], password=db_cred['db_password'])

                                
    # read from database
    try:
        # cursor = connetion.cursor(pymysql.cursors.DictCursor)
        cur = connetion.cursor()
        cur.execute(sql)
        db_data = cur.fetchall()
        cur.close()
    finally:
        connetion.close()
    
    
    # return result
    return db_data

def get_order_from_db_by_order_no(order_no):
    
    sql_1= f'SELECT * FROM quicksiteDB.wp_posts WHERE ID = {order_no} AND post_status = "publish";'
    sql_2= f'SELECT * FROM quicksiteDB.wp_posts WHERE post_status = "publish"'
    # sql = f"SELECT * FROM localdemostore.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order';"

    db_order =  read_from_db(sql_2)
    import pdb; pdb.set_trace
    
    print(db_order)

# exmaple 2 with database schema
def get_order_from_db_by_order_no_dabase_schema(order_no):
   
    db_schema = GenericConfig.DATABASE_SCHEMA 
    db_table_prefix = GenericConfig.DATABASE_TABLE_PREFIX

    sql_1= f'SELECT * FROM {db_schema}.{db_table_prefix}posts WHERE ID = {order_no} AND post_status = "publish";'

    db_order =  read_from_db(sql_1)
    import pdb; pdb.set_trace
    
    print(db_order)
# only needed if you running from from the terminal and wan to test the code
get_order_from_db_by_order_no(1)
get_order_from_db_by_order_no_dabase_schema(1)