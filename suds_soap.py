from suds.client import Client

# 连接到webservice服务，获取查询手机号码归属地服务方法
client = Client('http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl')
# 输出服务方法
print(client)
# Suds ( https://fedorahosted.org/suds/ )  version: 0.8.3
#
# Service ( MobileCodeWS ) tns="http://WebXml.com.cn/"
#    Prefixes (1)
#       ns0 = "http://WebXml.com.cn/"
#    Ports (2):
#       (MobileCodeWSSoap)
#          Methods (2):
#             getDatabaseInfo()
#             getMobileCodeInfo(xs:string mobileCode, xs:string userID)
#          Types (1):
#             ArrayOfString
#       (MobileCodeWSSoap12)
#          Methods (2):
#             getDatabaseInfo()
#             getMobileCodeInfo(xs:string mobileCode, xs:string userID)
#          Types (1):
#             ArrayOfString

# 一共有两个方法 getDatabaseInfo()   getMobileCodeInfo(xs:string mobileCode, xs:string userID)
# 具体含义请看 http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx

# 查询手机号码归属地
print(client.service.getMobileCodeInfo("18388888888",""))
# 18388888888：云南 昆明 云南移动全球通卡
