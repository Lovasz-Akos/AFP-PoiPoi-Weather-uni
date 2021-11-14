# Követelmény Specifikáció

## 1. Áttekintés

Az alkamazás célja különböző magyarországi időjárási adatok feldolgozása, ezen adatok tárolása későbbi elemzések céljából. A program a korábbi éghajlatai adatok felhasználásával megkísérli az időjárás alakulásának a "megjósolását", akár napi vagy éves szinten is, mindezt minnél pontosabb eredménnyel. A becslések pontosságát pedig a gépi tanulással próbálja majd a program folyamatosan pontosítani és javítani, ezáltal is elősegítve a megfelelő jóslási erdemények létrehozását. Az eredményeket eltárolva pedig lehetséges lesz a "tippek" és a valós adatok összehasonlítása is. Ehhez pedig egy egyszerű felhasználói felület lesz a segítségünkre.

## 2. Jelenlegi helyzet

A megrendelő egy olyan időjárási előrejelzéseket generáló alkalmazást szeretne, ami képes rendelkezésünkre álló éghajlati és időjárási adatok feldolgozásával, pontos és megbízható előrejelzéseket létrehozni a megrendelő számára. Majd ezen eredményeket a program "tanulással" képes legyen folyamatosan pontosítani, ezáltal még pontosabb becsléseket létrehozva.

## 3. Vágyálom rendszer

A projekt célja, egy olyan időjárási előrejelzéseket generáló program létrehozása, ami képes megbízható adatokat készíteni, a rendelkezésre álló adathalmaz feldolgozásával. Tehát a programnak képesnek kell lennie arra, hogy egy adatbázisba elmentett különböző időjárási és éghajlati adatok felhasznásával, elemzésével előrejelzési erdeményeket tudjon lérehozni, lehetőleg minnél pontosabban a felhasználó számára. Majd az eredményeket, és az valós adatokat összevetve, az alkalmazás képes legyen tanulni, ezáltal folyamatosan egyre pontosabb becsléseket megalkotni a felhasználónak. Továbba a program egy egszerűbb felhasználói felülettel is rendelkezni fog, ahol az előrejelzéseket lehet megtekinteni.

## 4. Funkcionális követelmények

- A program képes éghajlati és időjárási adatok felhasználásával előrejelzéseket generálni.
- A felhasználó képes lesz a www.met.hu-n található adatokkal bármely, az oldalon fellelhető város időjárás és éghajlati adatait felhasználni az előrejelzésekhez, így az adott városhoz készíthet előrejelzési adatokat
- A felhasználó képes lementeni az előrejelzéseket, későbbi felhasználás és összehasonlítás céljából
- A program az elérhető adatok és a saját előrejelzések felhasználásával és machine learning segítségével tanul, ezáltal képes egyre pontosabb erdemények lérehozására
- Az előrejlezések pontosságának javulását egy grafikonon követheti nyomon a felhasználó

## 5. Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felület | Tallózás | Az időjárási adatokat tartalmazó fájlok kiválasztása megnyitásra és beolvasásra |
| K2 | Felület | Mentés | Az előrejelzések lementése egy fájlba |
| K3 | Felület | Futtatás | Az adatok kielemzése, előrejelzések kiíratása |
| K4 | Funkció | Machine Learning | A program az elérhető adatok és a saját becslései felhasználásával "tanul", ezáltal képes egyre pontosabb erdemények megtippelésére |
| K5 | Funkció | Beolvasás | Egy nagyobb adathalmaz feldolgozása, majd a program számára kedvező adatkstruktúra létrehozása |
| K6 | Funkció | Előrejelzés | A rendelkezésre álló adatok tanulmányozásával, a program képes "megtippelni", hogy milyenek lesznek az időjárási viszonyok a jövőben |

## 6. Irányott és szabad szöveges riportok

A rendszer képes éghajlati és időjárási adatok felhasználásával előrejelzéseket generálni. Az egyik legfontosabb funkciója a machine learning amivel a program az elérhető adatok és a saját becslései felhasználásával "tanul", ezáltal képes egyre pontosabb erdemények megtippelésére.

## 7. Rendszerre vonatkozó törvények, szabványok, ajánlások

A programunk teljesen ingyenes, bárki használhatja.

## 8. Jelenlegi üzleti folyamatok modellje

Bár a mai világban már rengeteg olyan program és applikáció létezik, ami időjárási előrejelzésekkel foglalkozik, a mi csapatunk mégis szeretné megpróbálni, egy olyan alkalmazással bővíteni eme programok palettáját, ami tudásával képes megközelíteni a versenytársait. Általában ezek a programok a jelenlegi időjárást közlik, vagy csak pár napos előrejelzésekkel látnak el minket. A mi applikációnk célja viszont az, hogy akár 1 év távlatában is lehessen előrejelzéseket létrehozni. Ebben a gépi tanulás lesz a segítségünkre. Ezen technológia felhasználásával szeretnénk elérni, hogy olyan időjárási előrejelzéseket generáljon a program, amik a lehető legpontosabbak még ilyen nagyobb idősávok használata esetén is. A kívánt eredmény eléréséhez, több ilyen applikáció működési elvét és többféle machine learning modellt fogunk tanulmányozni.

## 9. Igényelt üzleti folyamatok modellje

Csapatunk célja egy olyan időjárási előrejelzéseket létrehozó applikáció létrehozása, ami elsősorban ingyenes, reklámmentes és bizonyos határértékeken belűl képes az imént említett előrejelzéseket létrehozni. Bár programunk nem veheti fel a meteorológiai szolgálatok pár napos előrejelzéseinek pontosságával a versenyt, az applikációnk errősége másból adódik. Ugyanis ez a program képes (jelen esetben) Budapest éghajlatának 119 évnyi adatát feldolgozni, elemezni és ebből hosszútávú, akár egy éves előrejelzéseket is generálni a felhasználó számára. Legyen szó egy adott nap időjárásáról vagy akár az év mindennapjáról is.

## 10. Fogalomszótár

- Machine learning: A gépi tanulás matematikai adatmodellekkel tanít be számítógépeket közvetlen felügyelet nélkül. Ez a mesterséges intelligencia (AI) egy részhalmaza. A gépi tanulás algoritmusokkal azonosít mintákat az adatokban, amelyekkel ezután adatmodellt készít, és előrejelzéseket végez.
- Python: A Python egy általános célú, nagyon magas szintű programozási nyelv. A nyelv tervezési filozófiája az olvashatóságot és a programozói munka megkönnyítését helyezi előtérbe a futási sebességgel szemben.
