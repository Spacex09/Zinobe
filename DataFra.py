import  requests, json
import pandas as pd
import hashlib

url= requests.get("https://restcountries.com/v3.1/translation/Mexico")
text = url.text
data = json.loads(text)


user = data[0]

region = user['region']
capital =user['capital'][0]
languages =user['languages']['spa']
lan_encri =languages
con_cifrado = hashlib.sha1(lan_encri.encode())

data1 = {'Region':[region],
         'City Name':[capital],
         'Languaje':con_cifrado.hexdigest()}

df = pd.DataFrame(data1)

print("--------TABLA CON PANDA DATAFRAME_________")
print(df)
print("-----------JSON------------")
print(data1)
print("----------Time_Fila-------------")
print(df.count().to_json())
print("---------Time_Descrip----------")
print(df.describe())







