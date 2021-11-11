# Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felület | Tallózás | Az időjárási adatokat tartalmazó fájlok kiválasztása megnyitásra és beolvasásra |
| K2 | Felület | Mentés | Az előrejelzések lementése egy fájlba |
| K3 | Felület | Futtatás | Az adatok kielemzése, előrejelzések kiíratása |

# Jelenlegi üzleti folyamatok modellje

Bár a mai világban már rengeteg olyan program és applikáció létezik, ami időjárási előrejelzésekkel foglalkozik, a mi csapatunk mégis szeretné megpróbálni, egy olyan alkalmazással bővíteni eme programok palettáját, ami tudásával képes felvenni a versenyt társaival és még akár meg is haladja azt.
Ebben a gépi tanulás lesz a segítségünkre.
Célunk ezen technológia felhasználásával nem más mint egy olyan időjárási előrejelzéseket generáló program megírása, ami a lehető legpontosabban tudja "megjósolni" az időjárást.

# Forgatókönyvek

Az alkamazás célja különböző magyarországi időjárási adatok feldolgozása, ezen adatok tárolása későbbi elemzések céljából. A program a korábbi éghajlatai adatok felhasználásával megkísérli az időjárás alakulásának a "megjósolását", akár napi vagy éves szinten is, mindezt minnél pontosabb eredménnyel. A becslések pontosságát pedig a gépi tanulással próbálja majd a program folyamatosan pontosítani és javítani, ezáltal is elősegítve a megfelelő jóslási erdemények létrehozását. Az eredményeket eltárolva pedig lehetséges lesz a "tippek" és a valós adatok összehasonlítása is. Ehhez pedig egy egyszerű felhasználói felület lesz a segítségünkre.