#Name bucket
BUCKET = 'my-bucket'

#IBM Cloud
config = {'lithops' : {'storage_bucket' : BUCKET},

          'ibm_cf':  {'endpoint': 'my-endpoint',
                      'namespace': 'my-namespace',
                      'api_key': 'my-api_key'},

          'ibm_cos': {'region': 'my-region',
                      'api_key': 'my-api_key'}}
