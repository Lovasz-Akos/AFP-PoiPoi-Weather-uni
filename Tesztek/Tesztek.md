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
