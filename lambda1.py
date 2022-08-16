# import the JSON utility package since we will be working with a JSON object
import json
import sys
import os
import logging
import pymysql

host="mm-xpand1.mdb0001358.db.skysql.net"
port="5002"
user="DB00006940"
password="XXXX"
database="travel"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host='mm-xpand1.mdb0001358.db.skysql.net', port=5002, user='DB00006940',
                           passwd="Admin777!", db='travel', ssl={'ca':'/opt/python/skysql_chainXpand.pem'}, connect_timeout=10)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    
    # extract values from the event object we got from the Lambda service
    delay1 = event['d1']
    delay2 = event['d2']
    logger.info ("d1 is " + delay1)
    logger.info ("d2 is " + delay2)
    
    sqlString = "select count(dep_delay) from flights where dep_delay > " + delay1 + " and  dep_delay < " + delay2

    with conn.cursor() as cur:
        cur.execute(sqlString)
        res1 = cur.fetchone()
    
# return a properly formatted JSON object
    return {
        
        'statusCode': 200,
        'body': json.dumps('Your answer is ' + '' + str(res1[0]))
    }