import requests

username = 'username'
token = 'sampletoken0123456789'

#logging in to a server
login = requests.get('https://sampleapi123.testmysampleapi123.com/', authentication=(username,token))

#end of file
