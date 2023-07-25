import boto3

sqs = boto3.client('sqs')

response = sqs.list_queues()

print('Existing queues:')
for queue_url in response['QueueUrls']:
    print(queue_url)

