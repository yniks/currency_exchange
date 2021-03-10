from datetime import date 
from json import dumps, loads
from requests import get as fetch
from debug import Debug
log=Debug()

'''
    class Symbols:
        functions:
            1. to provide symbols of all possible currencies as : symbol.symbols
            2. to provide rate data of all possible currencies : as symbol.data
            3. to privide full name of the currency: as symbol.name
            4. caching of datewise exchange values
'''
class CurrencyProvider:
    data={}
    symbols=[]
    names={}
    def __init__(self):
        try:
            with open("currency.json") as file:
                    self.names={ key:value['name'] for (key,value) in loads(file.read()).items()}
        except:
            self.names={}
        self.symbols=list(self.names.keys())

    def _name(self,symbol):
        return self.names.get(symbol,symbol)
            
    def __load(self,date):
        with open(date+'.json') as file:
            return loads(file.read())

    def __save(self,data):
        with open(data['date']+'.json',"wt") as file:
            file.write(dumps(data))

    def loadvalues(self):
        try:
            log("loading file for today")
            data=self.__load(date.today().strftime("%Y-%m-%d"))
            log("loaded data from filesystem")
        except:
            ''' fetch latest, save for later use '''
            log("will fetch data from API")
            data=fetch('https://api.exchangerate-api.com/v4/latest/USD').json()
            self.__save(data)
            log("fetched and saved data from API")
        
        ''' Create a list of currency short name  '''
        self.data=data['rates']

