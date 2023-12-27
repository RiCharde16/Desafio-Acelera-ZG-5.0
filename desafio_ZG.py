import requests as req


url = "https://tranquil-rex-405218.rj.r.appspot.com/hashCodeServer/"
parametros = {'nome': "RichardSilvaCosta",
           'email': 'richardsc-2004@hotmail.com',
           'cpf': "374.909.638-42"}

response = req.post(url,params=parametros)

print(response.status_code)
print()
# print(response.headers)
print(response.json())