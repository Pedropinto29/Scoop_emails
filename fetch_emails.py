import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
    'type': 'service_account',
    'project_id': 'scoop-5e7ec',
    'private_key_id': '090d6dfdad9d3408f0206cbf31592464e98a0248',
    'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDRz3g9eEEFkzbt\nQcR1Z/yMnqi/GppJUBgGPGyK8X4j5OcWfS9n/Z2BXQvxiOkj4ML3AeQU+OTph36u\nZLCk9ORm9qqMHw3oh0Lv1eDcdEkrKLN8ecR6UXsKsGFfg+KI5a4BMXnkgqe5zOKK\nDX7K709bmUGr1pq+LC3SXdUj6/cYz5R524HyTBHTAUeJDGSMh5BTKVFKLLHPib5W\nzXKrltiuajh60oy/lUjxea375ZU2IpOIGlNoKItCzXlNmSYlgiW88qC7FCqdXW4J\na9NMt6LPdk/hHN+91tjfDZkrnJ50KpGJLkOqqTaq3gevpWjxTCVInB1RrXx80qa7\nzVzIROUTAgMBAAECggEAIlxU99Qy6ePTMgX8U7IFBU6SmkGUFP+d/59zs0mbe+to\nASHdWq2JVv9TDmp6rBqKM4PGw7yDWM+M6qio2UsWANrS0YHgeD12s+qWGeSdewj+\nZBtZFyMzAGwkdk0WE49x8NYWfVr8dwxb6XoOUtPgbkLqI2dRDmYT1wjw+CIT5KcG\nBAUqDcwlzZ8AHDGWTWJQr9SboNlzMvJshxg4lFQcsrOQsyLkaTLscF0k3iEnR09e\nuZi4yFW7Vd70o0nSVpwUHbn71fJ8VZ8b+DEuly3bOcVgS7t/UMXhe/dzTtXu3b8p\nItMU9H7+pZ1B5qL/DuE2NtzpaUD5MyQMivYolCNAGQKBgQD/7cuBj1XxqD2AfM/W\nGgzQzqkwJjnGWFCsXXN35lSwZc+wejW5zGVKTFU4WQpSLBoikg3cXEAMn6sfw7Ly\nBGD2cxU4eWytRKNIkHMu/xniZWnmnx9Io52WGH0sXJyZUE1iCHF2MY7TxiBGU6Ng\nKSqh4xetppANfbqMHWTKIF6flQKBgQDR3mTpZPvoQ6WQWe29GgvuemFfqymD3lGg\nSNrn19KH6M8dWEb4A2YNHb8VmlEswCw3yhpu3THAQz5W6L8Saq2hQahS6S5Eyq4K\nG4RMbM21KkdSvTyzXDdxJZ1YmXKD5UCykXPMREXXNB8zccl3JXrcAPSm23QBG+zF\n5btrsvJoBwKBgC9rcQyVcVgwUwzuk1fZRcyergyE2KmejXwSaKWroL96bcwGKNQ/\nQflNQXEKVnY5Q7JqG3VcBmYQY5WkHhDnrMudMS5gmTlVgWedlCn+DF69aazYiORd\npII+EVtZ4Y4qqdvjMpqyvgMRL8O4FYpotkR+nlGHjiNhy2HQxG8LJl0tAoGADJ0k\nTY7fQSeHtPRiwKHnI69BWQGtnhpnp42ZcqPbKIYKpMXghhmWMaWfDYpX5KusPLIu\nAonS6q5f+dNFYLL+upl6p3kSadoQudTLj9heSMxAuy1aj6E0R92t5lxasKi/ybvK\nTPWxiOy+D1aAeGPNTZnVGo5IG6T1BzP2ntODlFMCgYEAheJIkNVKVgwo8se+DwK2\n0ppgDq3SGMnXnVkOICIVrECFb+oBICBAWFVPza8y0R9P3xymTeZG13WgkqWM65xS\nbVl8EdfVwuktZkYj+I88H++TdVO98HYmnPvT94nE6kUNehDCY4HAUT8P1R6/7j1T\nnTXHpUFYDNAPj86+XlAlVhQ=\n-----END PRIVATE KEY-----\n',
    'client_email': 'firebase-adminsdk-y5usc@scoop-5e7ec.iam.gserviceaccount.com',
    'client_id': '115432729314421527994',
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y5usc%40scoop-5e7ec.iam.gserviceaccount.com',
    'universe_domain': 'googleapis.com'
}

cred = credentials.Certificate(config)
app1 = firebase_admin.initialize_app(cred, {'databaseURL': 'https://scoop-5e7ec-default-rtdb.europe-west1.firebasedatabase.app/'})

db = firestore.client()

def get_emails():
    emails = []
    sales_ref = db.collection("Sales")
    docs = sales_ref.get()
    for doc in docs:
        emails.append(doc.to_dict()['firstName'])
    
    return emails

if __name__ == "__main__":
    emails = get_emails()
    print(emails)