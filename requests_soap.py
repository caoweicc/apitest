import requests

url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'

data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://WebXml.com.cn/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:getMobileCodeInfo>
         <!--Optional:-->
         <web:mobileCode>13797756789</web:mobileCode>
         <!--Optional:-->
         <web:userID></web:userID>
      </web:getMobileCodeInfo>
   </soapenv:Body>
</soapenv:Envelope>
'''.encode('utf-8')

headers = {'Content-Type':'text/xml;charset=UTF-8'};

res = requests.post(url=url,data=data,headers=headers)
print(res.text)