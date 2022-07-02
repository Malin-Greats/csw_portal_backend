import requests
import json
from .init import *
instructions = {
    'parts': [
        {
            'html': 'index.html',
            'assets': [
                "style.css",
                "Inter-Regular.ttf",
                "Inter-Medium.ttf",
                "Inter-Bold.ttf",
                "SpaceMono-Regular.ttf",
                "logo.svg",
					 "ribbon.svg",
            ],
        }
    ]
}
myname = open_textfile()
gen =  pillow(myname)
# response = requests.request(
#     'POST',
#     'https://api.pspdfkit.com/build',
#     headers={
#         'Authorization': 'Bearer pdf_live_SqXyF0DaGISFEpGijDem54XXkbZRT2jHhktneJxrHAp', # Replace with your API key.
#     },
#     files={
#         'index.html': open('index.html', 'myname','rb'),
#         'style.css': open('style.css', 'rb'),
#         'Inter-Regular.ttf': open('Inter-Regular.ttf', 'rb'),
#         'Inter-Medium.ttf': open('Inter-Medium.ttf', 'rb'),
#         'Inter-Bold.ttf': open('Inter-Bold.ttf', 'rb'),
#         'SpaceMono-Regular.ttf': open('SpaceMono-Regular.ttf', 'rb'),
#         'logo.svg': open('logo.svg', 'rb'),
# 		  'ribbon.svg': open('ribbon.svg', 'rb'),
#     },
#     data={
#         'instructions': json.dumps(instructions)
#     },
#     stream=True
# )

# if response.ok:
#     with open('result.pdf', 'wb') as fd:
#         for chunk in response.iter_content(chunk_size=8096):
#             fd.write(chunk)
# else:
#     print(response.text)
#     exit()