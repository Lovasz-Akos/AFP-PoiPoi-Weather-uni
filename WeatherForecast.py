import pandas as pd
import numpy as np

def readSource():
    DailyDatas_columns=['Dátum','Napi Középhőmérséklet','Napi Maximumhőmérséklet','Napi Minimumhőmérséklet','Napi Csapadékösszeg','Napi Csapadékösszeg Fajtája','Napfénytartam Napi Összege','Globálsugárzás Napi Összege']
    DailyDatas = pd.read_csv('Adatforrás/Budapest/napi_adatok/BP_d.txt', sep=';', skiprows=1, names=DailyDatas_columns)
    print("A fájl beolvasás sikeres")
    DailyDatas['Dátum']=pd.to_datetime(DailyDatas['Dátum'])
    DailyDatas=DailyDatas.drop(['Globálsugárzás Napi Összege'], axis=1)
    return DailyDatas

def generateDateCodes(DataFrame):
    DateCodes=[0]*DataFrame.index.stop
    i=0
    for date in DataFrame['Dátum']:
        DateCodes[i]= date.month*100 + date.day
        i=i+1
    return DateCodes
        
    
def main():
    DailyDatas = readSource()
    DateCodes=pd.DataFrame(generateDateCodes(DailyDatas),columns=['DátumKód'])
    DailyDatas['DátumKód']=DateCodes
    print(DailyDatas)
    
main()
    