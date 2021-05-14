from aip import AipImageClassify

APP_ID = '24172633'
API_KEY = 'A8pFXNf9kDjb6x1iNPlLDRVd'
SECRET_KEY = 'G82Ee1rTA7pcFQTMWdVuZgD8nn6oBw5R'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

options = {}
options["baike_num"] = 5

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        data = fp.read()
        return data

image = get_file_content('tom.jpeg')

result = client.advancedGeneral(image)
print(result)

