# project2.py

1. Opis projektu
   Temat projektu
   Gra w stylu "pamięć", w której gracz musi odnaleźć takie same pary kart.

Określenie celu projektu i oczekiwanych rezultatów
Celem projektu jest stworzenie gry, która pozwoli użytkownikowi trenować swoją pamięć poprzez odnajdywanie par kart. Oczekiwane rezultaty to działająca aplikacja konsolowa, która umożliwi grę w "pamięć".

Opis funkcjonalności projektu
Gra losowo rozmieszcza pary kart na planszy.
Gracz wybiera dwie karty do odsłonięcia w każdej turze.
Jeśli karty są takie same, pozostają odkryte.
Jeśli karty są różne, zostają ponownie zakryte.
Gra kończy się, gdy wszystkie pary kart zostaną odkryte.
Wynik gracza (ilość ruchów) jest wyświetlany na końcu gry.
Krótka instrukcja uruchomienia projektu
Uruchom plik memory_game.py w terminalu za pomocą komendy python memory_game.py.

2. Analiza wymagań
   Spis wymagań funkcjonalnych i niefunkcjonalnych projektu

   Funkcjonalne:
   Gra losowo rozmieszcza karty na planszy.
   Gracz może wybrać dwie karty do odsłonięcia w każdej turze.
   Gra sprawdza, czy karty są takie same i odpowiednio je odsłania lub zakrywa.
   Gra kończy się, gdy wszystkie pary kart są odkryte.
   Gra wyświetla wynik gracza na końcu.

Niefunkcjonalne:
Gra powinna być intuicyjna i łatwa w obsłudze.
Kod powinien być modularny i czytelny.
Aplikacja powinna działać płynnie i bez błędów.
Określenie interfejsu użytkownika i funkcjonalności systemu
Interfejs użytkownika: tekstowy, konsolowy
Funkcjonalności systemu:
Inicjalizacja gry
Wyświetlanie planszy
Odczytanie ruchów gracza
Sprawdzenie par kart
Wyświetlenie wyniku na końcu gry

3.  Użycie wybranej struktury danych
    Struktura danych: Lista dwuwymiarowa do reprezentacji planszy gry
    Organizacja kodu w modułach
    Plik główny: memory_game.py
    Moduł testowy: test_memory_game.py

Zastosowanie wybranego elementu biblioteki standardowej
Użycie random.shuffle do losowego rozmieszczania kart.
Wykorzystanie jednego z frameworków służących do wykorzystania sztucznej inteligencji
W tym projekcie zastosowanie AI jest opcjonalne i nie jest głównym celem, więc nie zostanie użyte.

4. Testowanie
   Implementacja testu jednostkowego
   Opis wyników testów i ewentualne poprawki

5. Projekt został zrealizowany zgodnie z założeniami, a gra działa poprawnie. Możliwe usprawnienia obejmują:
   -Dodanie interfejsu graficznego zamiast konsolowego.
   -Implementacja różnych poziomów trudności.
   -Dodanie licznika czasu gry.
   -Ulepszenie testów jednostkowych o więcej przypadków testowych.
