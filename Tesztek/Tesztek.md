# Tesztek

## Opció választás tesztjei

Amikor elindítjuk a programot, az egy opció választással indul, ami felkínálja a felhasználó számára a azon lehetőségeket amiből választhat

![Start](/Tesztek/Képek/Start.PNG)

A felhasználónak a 3 opció közül kell választania, tehát nem írhat be pl. 0-t vagy esetleg 4-et.

![Test-01](/Tesztek/Képek/Test01.PNG)

Ahogy a képen is látható az ellenörző elgoritmus nem engedi be a rossz értékeket.

## readSource függvény ellenörzése

Ez a függvény, az Adatforrás\Budapest\napi_adatok mappában találtható adathalmazt olvassa be.

![Test-02](/Tesztek/Képek/Test02.PNG)

Mint látható a függvény tökéletesen működik, minden adatot beolvas 1901-től 2020 végéig.

## readHistoryDataExtra függvény ellenörzése

Ez a függvény, az Adatforrás\Budapest\ mappában találtható history_data_extra.csv adathalmazt olvassa be. Erre az adathalmazra azért volt szükség mivel, a program második opciójához (a döntésifával való egynapos előrejelzéshez) mégtöbb paraméterre volt szükség amik a met.hu-n található adatbázisban nincsenek meg.
A forrásfájl így néz ki:

![historydataextra](/Tesztek/Képek/historydataextra.PNG)

Majd ha lefuttatjuk a függvény ezt az eredményt kapjuk:

![Test-03](/Tesztek/Képek/Test03.PNG)

A függvény tökéletesen működik, minden adatot beolvas.

## generateNKPredictors függvény

Ez a függvény a dátum alapú előrejelzéshez (1. opció) generál olyan adatokat amik a Napi Középhőmérséklet előrejelzéséhez szükségesek. A Dátum alapú előrejelzés egy DátumKód-ból számolja ki az adott nap hőmérsékletét. A program azokból az adatokból tanul amiket ez a függvény generál. Így a függvény által visszaadott adat struktúrának 2 adatot kell tartalmaznia, a DátumKódot (ez lesz az input) és a hozzá tartozó napi középhőmérsékletet (ez pedig az output).

![Test-04](/Tesztek/Képek/Test04.PNG)

A teszt képen látható, hogy minden adatot (input és output) tartalmaz a DataFrame.

## Dátum alapú előrejelzés tetszje

A dátum alapú előrejezésnek meg kell adni egy konkrét dátumot, és a program arra az adott napra fog generálni egy előrejelzést:
Ez volt a legelső előrejelzést generáló algoritmus és sajnos a legpontatlanabb is.
A tesztek során 2021.11.15.-ét adtam meg dátumnak

![DateTest01](/Tesztek/Képek/DateTest01.PNG)

Ha összevetjük a valós adatokkal:

![DateReal01](/Tesztek/Képek/DateReal01.PNG)

Láthatjuk egész pontos eredményt kapunk.
Megadok egy másik dátumot (2021.11.19):

![DateTest02](/Tesztek/Képek/DateTest02.PNG)

Valós adatok(3. a középhőmérséklet):

![DateReal02](/Tesztek/Képek/DateReal02.PNG)

Itt már viszont nem olyan pontos az előrejelzés sajnos, ami azért van mert a dátum alapú előrejelzés nem veszi figyelembe az elöző napok éghajlati adatait.
Ezért kerűlt be 2 másik opció is ami remélhetőleg pontosabb eredményt ad.