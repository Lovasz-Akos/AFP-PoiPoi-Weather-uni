# A rendszer célja

A rendszer célja, hogy statisztikai adatok alapján egy időjárás előrejelzést tudjon jósolni, ami elsősorban ingyenes és reklám mentes.
Ezen felül pedig rendelkezik minden olyan funkcióval ami ki tudja elégíteni a felhasználó igényeit is, viszont kellőképpen letisztult és felhasználóbarát a felülettel rendelkezik,
ahhoz, hogy intuitív legyen a használata.
Természetesen nem csak számítógépen lesz elérhető, hanem minél több platformon, tehát tableten és telefonon is.
Használatához semmilyen regisztráció nem szükséges, bárki hozzáférhet.

# Üzleti folyamatok modellje

Felhasználók:

- Alapvetően csak a program felületéhez és a használatához férnek hozzá.

Fejlesztők:

- Szintén hozzá tudnak férni a program felületéhez és használatához, viszont a karbantartást és a fejlesztést is ők végzik.

# Követelmények

A program legfőbb feladata, hogy statisztikai adatok alapján egy időjárás előrejelzést tudjon jósolni.
Mindemellett szeretnénk hogy a gépi tanulás legyen a program alapja és működési elve.

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

- Alfa teszt:

	- A teszt elsődleges célja: az eddig meglévő funkcióknak a különböző
böngészőkkel, és androidokkal való kompatibilitásának tesztelése. A tesztet a
fejlesztők végzik.
Az eljárás sikeres, ha különböző böngészőkben és különböző androidokon is
megfelelően működnek a különböző funkciók. A teszt időtartama egy hét.

# Telepítési terv

- Androidos alkalmazás esetén: Töltse le az alkalmazást a Google Play áruházból, adja meg a szükséges engedélyeket és telepítse a programot!
- Webes alkalmazás esetén: A szoftver webes felületéhez csak egy ajánlott böngésző telepítése szükséges
	(Például: Google Chrome, Firefox, Opera, Safari), külön szoftver nem kell hozzá.
	
# Karbantartási terv

- Corrective Maintenance: A felhasználók által felfedezett és "user reportben" elküldött hibák javítása.
- Adaptive Maintenance: A program naprakészen tartása és finomhangolása.
- Perfective Maintenance: A szoftver hosszútávú használata érdekében végzett módosítások, új funkciók, a szoftver teljesítményének és működési megbízhatóságának javítása.
