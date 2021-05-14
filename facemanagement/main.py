from aip import AipFace
import base64

APP_ID = '24172652'
API_KEY = 'YrVIVr6xshUXjm9onYwpUDbE'
SECRET_KEY = 'usYC5mWN7WHGWgBkzDsovdqzHq5Dhihp'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        data = str(base64.b64encode(fp.read()),'utf-8')
        #print(data)
        return data

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
image = get_file_content('tom2.jpeg')
result = client.addUser(image,image_type='BASE64',group_id='hakD',user_id='TomCruise')
print(result)



