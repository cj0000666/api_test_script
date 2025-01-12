import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
formater = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')
filehandler = logging.FileHandler("api_test.log")
filehandler.setFormatter(formater)
logger.addHandler(filehandler)


class ApiHadler():

    BASE_URL="http://127.0.0.1:8000/"
    def get(self, object):
        url = self.url_hudler(object)
        
        try:
            response = requests.get(url)
        except Exception as err:
            logger.error(f"Unexpectd {err} of type: {type(err)}")
            
        else:
            return response
    
    def post(self, object, data):
        url = self.url_hudler(object)
        try:
            response = requests.post(url, json=data)
            
        except Exception as err:
            logger.error(f"{err} type:{type(err)}")
            
        else:
            return response
    
    def put(self, object, data):
        url = self.url_hudler(object)
        try:
            response = requests.put(url, json=data)
            
        except Exception as err:
            logger.error(f"{err} type:{type(err)}")
            
        return response
    
    def delete(self, object):
        url = self.url_hudler(object)
        try:
            response = requests.delete(url)
            
        except Exception as err:
            logger.error(f"{err} type: {type*err} ")
    
    def url_hudler(self, url):
        return f"{self.BASE_URL}{url}"
    
    

data ={"name":"jp laptop", "brand":"Hp", "quality":"elitbook","unit_quantity":1.00, "unit_cost":43000.00, "available_units":100.00}

my_heders = []

hadler = ApiHadler()
data = hadler.get("products/")

products=[]

if data.status_code == 200:
    for prd in data.json():

        product=[]
        for key, value in prd.items():
            product.append(value)
     
        products.append(product)
            
    
    keys_heders = list(prd.keys())
    print(keys_heders)
    print(products)
    
    
elif data.status_code==404:
    logger.warning("404 bad request")