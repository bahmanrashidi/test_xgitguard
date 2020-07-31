import requests

username = 'username'
apitoken = '!sampletoken0123456789'

#logging in to a server
login = requests.get('https://sampleapi123.xgitguardtestmysampleapi123.testdomain/', 
                     authentication=(username,apitoken))

#end of file
