# Áttekintés

A rendszer célja, hogy statisztikai adatok alapján egy időjárás előrejelzést tudjon jósolni, ami elsősorban ingyenes és reklám mentes.
Ezen felül pedig rendelkezik minden olyan funkcióval ami ki tudja elégíteni a felhasználó igényeit is, viszont kellőképpen letisztult és felhasználóbarát a felülettel rendelkezik,
ahhoz, hogy intuitív legyen a használata.


# Jelenlegi helyzet
Bár rengeteg időjárás előrejelző alkalmazás található a piacon, viszont ezek nagyrésze általában rengeteg zavaró reklámot tartalmaz, vagy esetleg bizonyos funkciók csak fizetés ellenében használhatóak.

# Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felület | Tallózás | Az időjárási adatokat tartalmazó fájlok kiválasztása megnyitásra és beolvasásra |
| K2 | Felület | Mentés | Az előrejelzések lementése egy fájlba |
| K3 | Felület | Futtatás | Az adatok kielemzése, előrejelzések kiíratása |
| K4 | Funkció | Machine Learning | A program az elérhető adatok és a saját becslései felhasználásával "tanul", ezáltal képes egyre pontosabb erdemények megtippelésére |
| K5 | Funkció | Beolvasás | Egy nagyobb adathalmaz feldolgozása, majd a program számára kedvező adatkstruktúra létrehozása |
| K6 | Funkció | Előrejelzés | A rendelkezésre álló adatok tanulmányozásával, a program képes "megtippelni", hogy milyenek lesznek az időjárási viszonyok a jövőben |

A kívánt eredmény eléréséhez, több ilyen applikáció működési elvét és többféle "tanulásra" képes algoritmust fogunk tanulmányozni.
Manapság egyre többen igényelik a pontosan/megfelelően működő időjárás előrejelző szoftvereket, weboldalakat mivel a mai világban egyre kiszámíthatatlanabb időjárás, megnehezíti az emberek életét.
A csapat több tagja is szembesült már azzal a problémával, amikor hiretelen teljesen más időjárás volt mint amit az időjárás előrejelző szoftver kiszámolt.

# Jelenlegi üzleti folyamatok modellje

Bár a mai világban már rengeteg olyan program és applikáció létezik, ami időjárási előrejelzésekkel foglalkozik, a mi csapatunk mégis szeretné megpróbálni, egy olyan alkalmazással bővíteni eme programok palettáját, ami tudásával képes felvenni a versenyt társaival és még akár meg is haladja azt.
Ebben a gépi tanulás lesz a segítségünkre.
Célunk ezen technológia felhasználásával nem más mint egy olyan időjárási előrejelzéseket generáló program megírása, ami a lehető legpontosabban tudja "megjósolni" az időjárást.


# Igényelt üzleti folyamatok modellje

 - A felhasználónak semmilyen regisztráció nem szükséges a szoftver használatához
 - A felület mobilon lesz natív, de a reszponzív kialakítás miatt máson is használható lesz
 - A felhasználónak, amennyiben rendelkezik az "alkalmazással" nincs szükségre internetkapcsolatra a használathoz
 
# Használati esetek

A felhasználó legfőképpen egy vagy több időjárás előrejelzést lesz képes lefuttatni és ezalapján tudni, hogy milyen időjárás várható.


- Python: A Python egy általános célú, nagyon magas szintű programozási nyelv. A nyelv tervezési filozófiája az olvashatóságot és a programozói munka megkönnyítését helyezi előtérbe a futási sebességgel szemben.

# Forgatókönyvek

Az alkamazás célja különböző magyarországi időjárási adatok feldolgozása, ezen adatok tárolása későbbi elemzések céljából. A program a korábbi éghajlatai adatok felhasználásával megkísérli az időjárás alakulásának a "megjósolását", akár napi vagy éves szinten is, mindezt minnél pontosabb eredménnyel. A becslések pontosságát pedig a gépi tanulással próbálja majd a program folyamatosan pontosítani és javítani, ezáltal is elősegítve a megfelelő jóslási erdemények létrehozását. Az eredményeket eltárolva pedig lehetséges lesz a "tippek" és a valós adatok összehasonlítása is. Ehhez pedig egy egyszerű felhasználói felület lesz a segítségünkre.

# Fogalomszótár

- Machine learning: A gépi tanulás matematikai adatmodellekkel tanít be számítógépeket közvetlen felügyelet nélkül. Ez a mesterséges intelligencia (AI) egy részhalmaza. A gépi tanulás algoritmusokkal azonosít mintákat az adatokban, amelyekkel ezután adatmodellt készít, és előrejelzéseket végez. 