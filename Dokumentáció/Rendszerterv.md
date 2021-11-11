# A rendszer célja

A rendszer célja, hogy statisztikai adatok alapján egy időjárás előrejelzést tudjon jósolni, ami elsősorban ingyenes és reklám mentes.
Ezen felül pedig rendelkezik minden olyan funkcióval ami ki tudja elégíteni a felhasználó igényeit is, viszont kellőképpen letisztult és felhasználóbarát a felülettel rendelkezik,
ahhoz, hogy intuitív legyen a használata.
Fontos, hogy a felhasználó el tudjon igazodni a szoftverünkön.
A rendszert a felhasználók majd webes felületen is tudják használni, tehát valamelyik böngésző szükséges lesz a használatához (Google Crome, Firefox, Opera, Safari, stb.).

# Projektterv 

Tag|Felelősség
-|-
Farkas Erik|Logika fejlesztő, Dokumentáció
Zöldi Tóth István|Design fejlesztő, Dokumentáció
Karsai Petra|Design tervező, Dokumentáció
Maka Bettina|Rendszerszervező, Dokumentáció

# Üzleti folyamatok modellje

Felhasználók:

- Alapvetően csak a program felületéhez és a használatához férnek hozzá.

# Követelmények

A program legfőbb feladata, hogy statisztikai adatok alapján egy időjárás előrejelzést tudjon jósolni.
Mindemellett szeretnénk hogy a gépi tanulás legyen a program alapja és működési elve.

- Admin:
    - Teljes hozzáférése van a rendszerhez, és  bármilyen rendszerszereplőként beléphet a rendszerbe
	
- Nincsenek megvásárolt komponenseink
	- Fejlesztői eszközök:
		- Notepad++
		- Python

# Teszt terv

A tesztelések célja, hogy a tesztelések során esetleges hibák feltűnése esetén, azokat ki tudjuk javítani.

Tesztelési eljárások:

- Unit teszt:

	- Ahol csak lehetséges, szükséges már a fejlesztési idő alatt is tesztelni, hogy a
metódusok megfelelően működnek-e.
Ezért a metódusok megfelelő működésének biztosítására mindegyikhez írni
kell Unit teszteket, a minél nagyobb kódlefedettséget szem előtt tartva. A
metódusok akkor vannak kész, ha a tesztesetek hiba nélkül lefutnak az egyes
metódusokon.

# Telepítési terv

- Androidos alkalmazás esetén: Töltse le az alkalmazást a Google Play áruházból, adja meg a szükséges engedélyeket és telepítse a programot!

# Karbantartási terv

- Corrective Maintenance: A felhasználók által felfedezett és "user reportben" elküldött hibák javítása.
- Adaptive Maintenance: A program naprakészen tartása és finomhangolása.