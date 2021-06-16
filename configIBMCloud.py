#Name bucket
BUCKET = '2020sd'

#IBM Cloud
config = {'lithops' : {'storage_bucket' : BUCKET},

          'ibm_cf':  {'endpoint': 'https://s3.eu-de.cloud-object-storage.appdomain.cloud',
                      'namespace': 'guillem.gorgori@estudiants.urv.cat_dev',
                      'api_key': 'hUKJ-4H0JyETfezS8XpZVEy8p6-BYhCsyPO8K8i_FVE9'},

          'ibm_cos': {'region': 'eu-de',
                      'api_key': 'hUKJ-4H0JyETfezS8XpZVEy8p6-BYhCsyPO8K8i_FVE9'}}