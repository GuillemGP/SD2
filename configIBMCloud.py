#Name bucket
BUCKET = '2020sd'


#IBM Cloud
config = {'lithops' : {'storage_bucket' : BUCKET},

          'ibm_cf':  {'endpoint': 'https://eu-de.functions.cloud.ibm.com',
                      'namespace': 'guillem.gorgori@estudiants.urv.cat_dev',
                      'api_key': '8473827c-1f14-4d61-9d02-16593ea15ed1:QHiEdcARKZeTsckGMJFZ75kfPuvmS9eZ7GEmIy5s3AkU6VVMMrWnSXFQYVE0kEEt'},

          'ibm_cos': {'region': 'eu-de',
                      'api_key': '8473827c-1f14-4d61-9d02-16593ea15ed1:QHiEdcARKZeTsckGMJFZ75kfPuvmS9eZ7GEmIy5s3AkU6VVMMrWnSXFQYVE0kEEt'}}

#Obtencio del credencials:
#api_key
#https://cloud.ibm.com/functions/namespace-settings