import requests
import json
import numpy as np

from PIL import Image

input = {
	"instances": [
		{
			"data": "USA war with China"
		}
	]
}

headers= {
	"Host": "torchserve-default.example.com"
}

url = "http://a219453e143f04b8b9cbfe75d0c0f716-919af9260dacb516.elb.ap-south-1.amazonaws.com:80/v1/models/sdxl:predict"

response = requests.post(url, data=json.dumps(input), headers=headers)

# with open("raw.txt", "w") as f:
# 	f.write(response.text)

# with open("raw.txt", "r") as f:
# 	a = f.read()

image = Image.fromarray(np.array(json.loads(response.text)['predictions'][0], dtype="uint8"))
image.save("./Output/USA.jpg")