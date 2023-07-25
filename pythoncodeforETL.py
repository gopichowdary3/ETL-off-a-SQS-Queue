import boto3
import hashlib
import json
import psycopg2
from psycopg2.extras import execute_values

# Establish a session with LocalStack SQS using boto3
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')

# Get the Queue URL
queue_url = 'http://localhost:4566/000000000000/login-queue'

# Define method to mask PII data (device_id and IP)
def mask_data(data):
    return hashlib.md5(data.encode()).hexdigest()

# Establish a connection to Postgres
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='postgres',
    user='postgres',
    password='postgres'
)

# Fetch message from SQS Queue
def fetch_message_from_queue():
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)

    # Process if messages exist
    if 'Messages' in messages:
        for message in messages['Messages']:
            msg_body = json.loads(message['Body'])

            # Check if keys exist in the message body
            if 'device_id' in msg_body and 'ip' in msg_body:
                # Mask PII data
                msg_body['masked_device_id'] = mask_data(msg_body.pop('device_id'))  # pop will remove the original keys
                msg_body['masked_ip'] = mask_data(msg_body.pop('ip'))  # pop will remove the original keys

                # Write to Postgres
                write_to_postgres(msg_body)

                # Delete processed message from the queue
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])


# Write records to Postgres
def write_to_postgres(record):
    # Establish connection
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")

    # Create a new cursor
    cur = conn.cursor()

    # Prepare the INSERT statement
    sql = "INSERT INTO user_logins(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    # Prepare the values
    values = [
        (
            record.get('user_id'),
            record.get('device_type'),
            record.get('masked_ip'),
            record.get('masked_device_id'),
            record.get('locale'),
            record.get('app_version'),
            record.get('create_date')
        )
    ]

    # Execute the INSERT statement
    cur.executemany(sql, values)

    # Commit changes and close
    conn.commit()
    cur.close()
    conn.close()


# Main Execution
if __name__ == '__main__':
    while True:
        fetch_message_from_queue()

