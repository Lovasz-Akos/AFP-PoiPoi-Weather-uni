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
    Temp_Predictors['Maximum Temperature_1']=""
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
        treeModel=weatherForecastWithDecisionTree(NK_Predictors[['DátumKód']] ,NK_Predictors[['Napi Középhőmérséklet']] )
        print("\nEzen a napon a napi középhőmérséklet a következő lesz: " + str(format(weatherForecastByDate(treeModel), '.2f')) + " °C " + "\n")
    elif(Input == '2'):
        DailyDatas=readHistoryDataExtra()
        FiveInputNK_Predictors = generateFiveInputNKPredictors(DailyDatas)
        print(FiveInputNK_Predictors)
    
    
    
main()
    