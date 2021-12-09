import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime, timedelta, date
import requests

pd.options.mode.chained_assignment = None  # default='warn'

def readSource():
    DailyDatas_columns=['Dátum','Napi Középhőmérséklet','Napi Maximumhőmérséklet','Napi Minimumhőmérséklet','Napi Csapadékösszeg','Napi Csapadékösszeg Fajtája','Napfénytartam Napi Összege','Globálsugárzás Napi Összege']
    DailyDatas = pd.read_csv('Adatforrás/Budapest/napi_adatok/BP_d.txt', sep=';', skiprows=1, names=DailyDatas_columns)
    DailyDatas['Dátum']=pd.to_datetime(DailyDatas['Dátum'])
    DailyDatas=DailyDatas.drop(['Globálsugárzás Napi Összege'], axis=1)
    return DailyDatas

def readHistoryDataExtra():
    DataFrame_columns=['Name','Date time','Maximum Temperature','Minimum Temperature','Temperature','Wind Chill','Heat Index','Precipitation','Snow','Snow Depth','Wind Speed','Wind Direction','Wind Gust','Visibility','Cloud Cover','Relative Humidity','Conditions']
    DataFrame = pd.read_csv('Adatforrás/Budapest/history_data_extra.csv', sep=',', skiprows=1, names=DataFrame_columns)
    DataFrame['Date time']=pd.to_datetime(DataFrame['Date time'])
    return DataFrame
    

def generateDateCodes(DataFrame):
    
    DateCodes=np.empty(DataFrame.index.stop,dtype=np.intc)
    i=0
    for date in DataFrame['Dátum']:
        DateCodes[i]= date.month*100 + date.day
        i=i+1
    return DateCodes

def generateFiveInputNKPredictors(DataFrame):
    Temp_Predictors=DataFrame
    Temp_Predictors=Temp_Predictors.drop(['Name'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Date time'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Wind Chill'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Heat Index'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Precipitation'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Snow'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Snow Depth'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Wind Speed'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Wind Direction'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Wind Gust'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Conditions'], axis=1)
    # Inputs for Temperature: Maximum Temperature | Minimum Temperature | Visibility | Cloud Cover | Relative Humidity
    # Ez a ciklus létrehozza az új oszlopokat a DataFrame-ben a megfelelő névvel
    # Minimum Temperature_1 nevű oszlop pl. az aktuális elemhez képest, ez előző elem Minimum Hőmérsékletét tartalmazza
    # A Minimum Temperature_4 pedig az aktuális elemhez képest, 4 indexxel korábbi nap Minimum hőmérsékeltét
    for j in range(4):
            col_name='Maximum Temperature_'+str(j+1)
            Temp_Predictors[col_name]=""
            col_name='Minimum Temperature_'+str(j+1)
            Temp_Predictors[col_name]=""
            col_name='Visibility_'+str(j+1)
            Temp_Predictors[col_name]=""
            col_name='Cloud Cover_'+str(j+1)
            Temp_Predictors[col_name]=""
            col_name='Relative Humidity_'+str(j+1)
            Temp_Predictors[col_name]=""
    
    i=4
    # Az i-t azért 4-re állítom mert csak a 4. elemtől tudom elkezdeni 4 napig visszamenő adat gyűjtést
    # Az új, fentebb említett oszlopok itt töltődnek fel adatokkal
    while i < len(Temp_Predictors):
        for j in range(4):
            col_name='Maximum Temperature_'+str(j+1)
            Temp_Predictors[col_name][i]=Temp_Predictors['Maximum Temperature'][i-(j+1)]
            
            col_name='Minimum Temperature_'+str(j+1)
            Temp_Predictors[col_name][i]=Temp_Predictors['Minimum Temperature'][i-(j+1)]
            
            col_name='Visibility_'+str(j+1)
            Temp_Predictors[col_name][i]=Temp_Predictors['Visibility'][i-(j+1)]
            
            col_name='Cloud Cover_'+str(j+1)
            Temp_Predictors[col_name][i]=Temp_Predictors['Cloud Cover'][i-(j+1)]
            
            col_name='Relative Humidity_'+str(j+1)
            Temp_Predictors[col_name][i]=Temp_Predictors['Relative Humidity'][i-(j+1)]
        i=i+1;
    
    # Az első 4 sor "eldobása"
    Temp_Predictors = Temp_Predictors.drop(labels=[0,1,2,3], axis=0)
    
    # Újra indexelés, mivel ha ez nem történne meg, 4-től kezdőde a DataFrame indexelése
    Temp_Predictors=Temp_Predictors.reset_index(drop=True)
    
    #számunkra már fölösleges oszlopok eldobása
    Temp_Predictors=Temp_Predictors.drop(['Maximum Temperature'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Minimum Temperature'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Visibility'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Cloud Cover'], axis=1)
    Temp_Predictors=Temp_Predictors.drop(['Relative Humidity'], axis=1)
    
    return Temp_Predictors

def generateNKPredictors(DataFrame):
    # Az NK_Predictors névben az NK a Napi Középhőmérsékletre utal
    NK_Predictors = DataFrame
    NK_Predictors = NK_Predictors.drop(['Dátum'],axis=1)
    NK_Predictors = NK_Predictors.drop(['Napi Maximumhőmérséklet'],axis=1)
    NK_Predictors = NK_Predictors.drop(['Napi Minimumhőmérséklet'],axis=1)
    NK_Predictors = NK_Predictors.drop(['Napi Csapadékösszeg'],axis=1)                              
    NK_Predictors = NK_Predictors.drop(['Napi Csapadékösszeg Fajtája'],axis=1)
    NK_Predictors = NK_Predictors.drop(['Napfénytartam Napi Összege'],axis=1)
    return NK_Predictors   

def GetHistoricalWeatherData(inputDate):
    startDate = inputDate.today()
    endDate = startDate - timedelta(days=3)
    queryURL="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?aggregateHours=24&combinationMethod=aggregate&startDateTime="+str(endDate.year)+"-"+str(endDate.month)+"-"+str(endDate.day)+"T00%3A00%3A00&endDateTime="+str(startDate.year)+"-"+str(startDate.month)+"-"+str(startDate.day)+"T00%3A00%3A00&maxStations=-1&maxDistance=-1&contentType=json&unitGroup=metric&locationMode=single&key=T735TQNAUCYZNFTQGDSSHTTSA&dataElements=default&locations=Budapest"
    foreCastQueryURL="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?aggregateHours=24&combinationMethod=aggregate&contentType=json&unitGroup=metric&locationMode=single&key=T735TQNAUCYZNFTQGDSSHTTSA&dataElements=default&locations=Budapest"
    df = pd.read_json(queryURL)
    foreCastDF= pd.read_json(foreCastQueryURL)
    df=createFiveInputPredictionData(df, foreCastDF)
    return df 

def createFiveInputPredictionData(df, foreCastDF):
    DataFrame = pd.DataFrame(index=[0])  
    for j in range(4):
            col_name='Maximum Temperature_'+str(j+1)
            DataFrame[col_name]=""
            col_name='Minimum Temperature_'+str(j+1)
            DataFrame[col_name]=""
            col_name='Visibility_'+str(j+1)
            DataFrame[col_name]=""
            col_name='Cloud Cover_'+str(j+1)
            DataFrame[col_name]=""
            col_name='Relative Humidity_'+str(j+1)
            DataFrame[col_name]=""
    i=4        
    for j in range(3):
        col_name='Maximum Temperature_'+str(i)
        DataFrame[col_name][0]=df['location']['values'][j]['maxt']
            
        col_name='Minimum Temperature_'+str(i)
        DataFrame[col_name][0]=df['location']['values'][j]['mint']
            
        col_name='Visibility_'+str(i)
        DataFrame[col_name][0]=df['location']['values'][j]['visibility']
            
        col_name='Cloud Cover_'+str(i)
        DataFrame[col_name][0]=df['location']['values'][j]['cloudcover']
            
        col_name='Relative Humidity_'+str(i)
        DataFrame[col_name][0]=df['location']['values'][j]['humidity']
        i=i-1; 
    DataFrame['Maximum Temperature_1'][0]=foreCastDF['location']['values'][0]['maxt']
    DataFrame['Minimum Temperature_1'][0]=foreCastDF['location']['values'][0]['mint']
    DataFrame['Visibility_1'][0]=foreCastDF['location']['values'][0]['visibility']
    DataFrame['Cloud Cover_1'][0]=foreCastDF['location']['values'][0]['cloudcover']
    DataFrame['Relative Humidity_1'][0]=foreCastDF['location']['values'][0]['humidity']     
    return DataFrame
    
def weatherForecastWithLinearRegression(X,y):
    linearreg=LinearRegression()
    linearreg.fit(X,y)
    return linearreg
    
def weatherForecastWithDecisionTree(X,y): 
    treeModel=DecisionTreeRegressor()
    treeModel.fit(X,y)
    return treeModel

def weatherForecastByDate(model):
    print("\n")
    print("Add meg az előrejelzés dátumát:")
    print("\n")
    LeapYears=[1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,]
    Input = 0
    while Input < 1901 or Input > 2030:
        num = input("Év(1901-2030): ")
        Input=int(num)
        if(Input < 1901 or Input > 2030):
          print("Hibás Évszám")
    year=Input
    Input = 0
    while Input < 1 or Input > 12:
        num = input("Hónap(1-12): ")
        Input=int(num)
        if(Input < 1 or Input > 12):
          print("Hibás Hónap")
    month = Input
    Input = 0
    if(month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month==10 or month==12):
        while Input < 1 or Input > 31:
            num = input("Nap (01-31): ")
            Input=int(num)
            if(Input < 1 or Input > 31):
              print("Hibás Nap")
    elif(month == 2 and year in LeapYears):
         while Input < 1 or Input > 29:
                num = input("Nap (01-29): ")
                Input=int(num)
                if(Input < 1 or Input > 29):
                  print("Hibás Nap")
    elif(month == 2 and year not in LeapYears):
         while Input < 1 or Input > 28:
                num = input("Nap (01-28): ")
                Input=int(num)
                if(Input < 1 or Input > 28):
                  print("Hibás Nap")
    else:
         while Input < 1 or Input > 30:
                num = input("Nap (01-30): ")
                Input=int(num)
                if(Input < 1 or Input > 30):
                  print("Hibás Nap")
    day = Input
    PredDate=[month+day]
    PredDate=pd.DataFrame(PredDate,columns=['DátumKód'])
    return model.predict(PredDate)[0]
    
def sourcePreProcessForLSTM(DataFrame):
    DataFrame.index = pd.to_datetime(DataFrame['Dátum'], format='%Y-%m-%d')
    DataFrame = DataFrame.drop('Dátum', axis=1)
    DataFrame = DataFrame.drop(['Napi Csapadékösszeg'],axis=1)                              
    DataFrame = DataFrame.drop(['Napi Csapadékösszeg Fajtája'],axis=1)
    DataFrame = DataFrame.drop(['Napfénytartam Napi Összege'],axis=1)
    DataFrame['Másodpercek'] = DataFrame.index.map(pd.Timestamp.timestamp)
    SecondsPerDay=60*60*24
    SecondsPerYear=365.25*SecondsPerDay
    DataFrame['Nap Szinusza']=np.sin(DataFrame['Másodpercek'] * (2* np.pi / SecondsPerDay))
    DataFrame['Nap Koszinusza']=np.cos(DataFrame['Másodpercek'] * (2* np.pi / SecondsPerDay))
    DataFrame['Év Szinusza']=np.sin(DataFrame['Másodpercek'] * (2* np.pi / SecondsPerYear))
    DataFrame['Év Koszinusza']=np.cos(DataFrame['Másodpercek'] * (2* np.pi / SecondsPerYear))
    DataFrame = DataFrame.drop('Másodpercek', axis=1)
    print(DataFrame)
    X,y = generateMatrixForLSTM(DataFrame)
    return X,y

def generateMatrixForLSTM(DataFrame, WindowSize=5):
    DataFrameAsNumpy= DataFrame.to_numpy()
    X=[]
    y=[]
    for i in range(len(DataFrameAsNumpy)-WindowSize):
        # 5 nap közép, max, min hőmérséklete és a dátum szinuszok és koszinuszok bekerűlnek az X-be
        row = [r for r in DataFrameAsNumpy[i:i+WindowSize]]
        X.append(row)
        # Az 6. nap középhőmérséklete belekerül az y-ba
        tempData = DataFrameAsNumpy[i+WindowSize][0]
        y.append(tempData)
    return np.array(X),np.array(y)  


def main():
    Input = 0
    while Input != '1' and Input != '2' and Input != '3':
        print("\n")
        print("Válassz a két opció közül:")
        print("1. Dátum alapú előrejelzés")
        print("2. Egy napos előrejelzés mostani éghajlati adatok alapján, döntési fával")
        print("3. Egy napos előrejelzés mostani éghajlati adatok alapján, LSTM modellel")
        print("\n")
        Input = input("Válaszd ki a megfelelő opció sorszámát (1-3): ")
    if(Input == '1'):
        DailyDatas = readSource()
        DateCodes=pd.DataFrame(generateDateCodes(DailyDatas),columns=['DátumKód'])
        DailyDatas['DátumKód']=DateCodes
        NK_Predictors=generateNKPredictors(DailyDatas)
        treeModel=weatherForecastWithDecisionTree(NK_Predictors[['DátumKód']] ,NK_Predictors[['Napi Középhőmérséklet']] )
        print("\nEzen a napon a napi középhőmérséklet a következő lesz: " + str(format(weatherForecastByDate(treeModel), '.2f')) + " °C " + "\n")
    elif(Input == '2'):
        DailyDatas=readHistoryDataExtra()
        FiveInputNK_Predictors = generateFiveInputNKPredictors(DailyDatas)
        treeModel=weatherForecastWithDecisionTree(FiveInputNK_Predictors[['Maximum Temperature_1','Minimum Temperature_1','Visibility_1','Cloud Cover_1','Relative Humidity_1','Maximum Temperature_2','Minimum Temperature_2','Visibility_2','Cloud Cover_2','Relative Humidity_2','Maximum Temperature_3','Minimum Temperature_3','Visibility_3','Cloud Cover_3','Relative Humidity_3','Maximum Temperature_4','Minimum Temperature_4','Visibility_4','Cloud Cover_4','Relative Humidity_4']],FiveInputNK_Predictors[['Temperature']] )
        #testData=FiveInputNK_Predictors
        #testData=testData.drop(['Temperature'], axis=1)        
        testData= GetHistoricalWeatherData(date.today())
        print("A holnapi középhőmérséklet ennyi lesz: "+str(treeModel.predict(testData)[0])+"°C")
    elif(Input == '3'):
        DailyDatas=readSource()
        X,y=sourcePreProcessForLSTM(DailyDatas)
        
        
       
    
    
main()
    