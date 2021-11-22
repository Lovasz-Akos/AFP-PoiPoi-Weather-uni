import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
pd.options.mode.chained_assignment = None  # default='warn'

def readSource():
    DailyDatas_columns=['Dátum','Napi Középhőmérséklet','Napi Maximumhőmérséklet','Napi Minimumhőmérséklet','Napi Csapadékösszeg','Napi Csapadékösszeg Fajtája','Napfénytartam Napi Összege','Globálsugárzás Napi Összege']
    DailyDatas = pd.read_csv('Adatforrás/Budapest/napi_adatok/BP_d.txt', sep=';', skiprows=1, names=DailyDatas_columns)
    print("A fájl beolvasás sikeres")
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
    
def weatherForecastWithLinearRegression(DataFrame):
    X=pd.DataFrame(DataFrame['DátumKód'],columns=['DátumKód'])
    y=pd.DataFrame(DataFrame['Napi Középhőmérséklet'],columns=['Napi Középhőmérséklet'])   
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.5)   
    linearreg=LinearRegression()
    linearreg.fit(X_train,y_train)
    return linearreg
    
def weatherForecastWithDecisionTree(DataFrame):
    X=pd.DataFrame(DataFrame['DátumKód'],columns=['DátumKód'])
    y=pd.DataFrame(DataFrame['Napi Középhőmérséklet'],columns=['Napi Középhőmérséklet'])   
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.5)   
    treeModel=DecisionTreeRegressor()
    treeModel.fit(X_train,y_train)
    return treeModel

def weatherForecastByDate(model):
    print("\n")
    print("Add meg az előrejelzés dátumát:")
    print("\n")
    Input = input("Év: ")
    Input = input("Hónap(1-12): ")
    month = Input
    Input = input("Nap (01-31): ")
    day = Input
    PredDate=[month+day]
    PredDate=pd.DataFrame(PredDate,columns=['DátumKód'])
    return model.predict(PredDate)[0]
    

        
def main():
    Input = 0
    while Input != '1' and Input != '2':
        print("\n")
        print("Válassz a két opció közül:")
        print("1. Dátum alapú előrejelzés")
        print("2. Egy napos előrejelzés mostani éghajlati adatok alapján")
        print("\n")
        Input = input("Válaszd ki a megfelelő opció sorszámát (1-2): ")
    if(Input == '1'):
        DailyDatas = readSource()
        DateCodes=pd.DataFrame(generateDateCodes(DailyDatas),columns=['DátumKód'])
        DailyDatas['DátumKód']=DateCodes
        NK_Predictors=generateNKPredictors(DailyDatas)
        treeModel=weatherForecastWithDecisionTree(NK_Predictors)
        print("\nEzen a napon a napi középhőmérséklet a következő lesz: " + str(format(weatherForecastByDate(treeModel), '.2f')) + " °C " + "\n")
    elif(Input == '2'):
        DailyDatas=readHistoryDataExtra()
        print(DailyDatas)
    
    
    
main()
    