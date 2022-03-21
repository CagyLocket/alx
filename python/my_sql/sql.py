SELECT * FROM mojatestowa.znajomi;
UPDATE znajomi SET imie="Python", nazwisko="Snake" WHERE idznajomi=4;

DELETE FROM znajomi WHERE idznajomi=2;


SELECT * FROM zawodnicy WHERE kraj="POL" OR kraj="GER" OR kraj="NOR";
SELECT * FROM zawodnicy WHERE kraj IN ("POL", "GER", "NOR");

SELECT * FROM zawodnicy WHERE wzrost >= 173 AND wzrost <=180;
SELECT * FROM zawodnicy WHERE wzrost BETWEEN 173 AND 180;


# znajdz wszsytkich trenerów, którzy nie mają daty urodzenia (data == Null)
# w przypadku Null nie ma znaku "=" jest "is null"
SELECT * FROM trenerzy WHERE data_ur_t is null;

# wypisz zawodników różnych niż kraj POL
SELECT * FROM zawodnicy WHERE kraj != "POL";


#szukanie po frazie
# % - dowlna ilość dowolnych znaków lub zero
# _ - 1 dowolny znak
# __ - dowolne 2 znaki

SELECT * FROM zawodnicy WHERE nazwisko LIKE "H%";

SELECT * FROM zawodnicy WHERE (nazwisko LIKE "%o%") AND (wzrost BETWEEN 177 AND 185) AND (kraj="GER" OR kraj="USA") AND (waga BETWEEN 59 and 60);

SELECT imie, nazwisko, ROUND(wzrost/100,2) FROM zawodnicy;

SELECT imie, nazwisko, wzrost, wzrost*1.46 as "Max. dł. nart" FROM zawodnicy;

SELECT imie, nazwisko, ROUND((waga/(wzrost/100*wzrost/100)), 2) as "BMI" FROM zawodnicy;

# wypisz zawodników wraz z ich trenerami (łączenie tabel przez kraj)
SELECT zawodnicy.imie, zawodnicy.nazwisko, trenerzy.imie_t, trenerzy.nazwisko_t FROM zawodnicy INNER JOIN trenerzy ON zawodnicy.kraj = trenerzy.kraj;

# wypisz trenerów, którzy nie treneują zawodników
SELECT * FROM trenerzy LEFT JOIN zawodnicy ON zawodnicy.kraj = trenerzy.kraj WHERE zawodnicy.imie is null;