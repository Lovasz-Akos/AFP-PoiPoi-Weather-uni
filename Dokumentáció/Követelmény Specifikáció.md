# Követelmény Specifikáció

## 1. Áttekintés

Az alkamazás célja különböző magyarországi időjárási adatok feldolgozása, ezen adatok tárolása későbbi elemzések céljából. A program a korábbi éghajlatai adatok felhasználásával megkísérli az időjárás alakulásának a "megjósolását", akár napi vagy éves szinten is, mindezt minnél pontosabb eredménnyel. A becslések pontosságát pedig a gépi tanulással próbálja majd a program folyamatosan pontosítani és javítani, ezáltal is elősegítve a megfelelő jóslási erdemények létrehozását. Az eredményeket eltárolva pedig lehetséges lesz a "tippek" és a valós adatok összehasonlítása is. Ehhez pedig egy egyszerű felhasználói felület lesz a segítségünkre.

## 2. Jelenlegi helyzet

A megrendelő egy olyan időjárási előrejelzéseket generáló alkalmazást szeretne, ami képes rendelkezésünkre álló éghajlati és időjárási adatok feldolgozásával, pontos és megbízható előrejelzéseket létrehozni a megrendelő számára. Majd ezen eredményeket a program "tanulással" képes legyen folyamatosan pontosítani, ezáltal még pontosabb becsléseket létrehozva.

## 3. Vágyálom rendszer

A projekt célja, egy olyan időjárási előrejelzéseket generáló program létrehozása, ami képes megbízható adatokat készíteni, a rendelkezésre álló adathalmaz feldolgozásával. Tehát a programnak képesnek kell lennie arra, hogy egy adatbázisba elmentett különböző időjárási és éghajlati adatok felhasznásával, elemzésével előrejelzési erdeményeket tudjon lérehozni, lehetőleg minnél pontosabban a felhasználó számára. Majd az eredményeket, és az valós adatokat összevetve, az alkalmazás képes legyen tanulni, ezáltal folyamatosan egyre pontosabb becsléseket megalkotni a felhasználónak. Továbba a program egy egszerűbb felhasználói felülettel is rendelkezni fog, ahol az előrejelzéseket lehet megtekinteni.

## 4. Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felület | Tallózás | Az időjárási adatokat tartalmazó fájlok kiválasztása megnyitásra és beolvasásra |
| K2 | Felület | Mentés | Az előrejelzések lementése egy fájlba |
| K3 | Felület | Futtatás | Az adatok kielemzése, előrejelzések kiíratása |
| K4 | Funkció | Machine Learning | A program az elérhető adatok és a saját becslései felhasználásával "tanul", ezáltal képes egyre pontosabb erdemények megtippelésére |
| K5 | Funkció | Beolvasás | Egy nagyobb adathalmaz feldolgozása, majd a program számára kedvező adatkstruktúra létrehozása |
| K6 | Funkció | Előrejelzés | A rendelkezésre álló adatok tanulmányozásával, a program képes "megtippelni", hogy milyenek lesznek az időjárási viszonyok a jövőben |

## 6. Jelenlegi üzleti folyamatok modellje

Bár a mai világban már rengeteg olyan program és applikáció létezik, ami időjárási előrejelzésekkel foglalkozik, a mi csapatunk mégis szeretné megpróbálni, egy olyan alkalmazással bővíteni eme programok palettáját, ami tudásával képes felvenni a versenyt társaival és még akár meg is haladja azt. Ebben a gépi tanulás lesz a segítségünkre. Célunk ezen technológia felhasználásával nem más mint egy olyan időjárási előrejelzéseket generáló program megírása, ami a lehető legpontosabban tudja "megjósolni" az időjárást. A kívánt eredmény eléréséhez, több ilyen applikáció működési elvét és többféle "tanulásra" képes algoritmust fogunk tanulmányozni.