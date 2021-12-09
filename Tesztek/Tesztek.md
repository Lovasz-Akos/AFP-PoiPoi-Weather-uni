# Tesztek

## Opció választás tesztjei

Amikor elindítjuk a programot, az egy opció választással indul, ami felkínálja a felhasználó számára a azon lehetőségeket amiből választhat
![Start](/Tesztek/Képek/Start.PNG)
A felhasználónak a 3 opció közül kell választania, tehát nem írhat be pl. 0-t vagy esetleg 4-et.
![Test-01](/Tesztek/Képek/Test01.PNG)
Ahogy a képen is látható az ellenörző elgoritmus nem engedi be a rossz értékeket.

## readSource függvény ellenörzése

Ez a függvény, az Adatforrás\Budapest\napi_adatok mappában találtható adathalmazt olvassa be.
![Test-02](/Tesztek/Képek/Test01.PNG)
Mint látható az függvény tökéletesen működik, minden adatot beolvas 1901-től 2020 végéig.
