# Dokumentacja Bazy Danych

## Tabela pól i uzasadnienie typów

| Nazwa pola | Typ Django | Typ SQL (SQLite) | Uzasadnienie |
| :--- | :--- | :--- | :--- |
| `id` | `AutoField` | `INTEGER` | Unikalny identyfikator klucza głównego genrowany automatycznie. |
| `title` | `CharField` | `varchar(200)` | Przechowuje krótkie teksty o ograniczonej długości. |
| `category` | `ForeignKey` | `integer` | Tworzy relację jeden-do-wielu wskazującą na ID z tabeli kategorii. |
| `price` | `DecimalField` | `decimal` | Gwarantuje dokładność obliczeń finansowych bez błędów zaokrągleń float. |
| `release_date` | `DateField` | `date` | Umożliwia operowanie na dokładnych datach i ich filtrowanie w bazie. |
| `players_count`| `IntegerField` | `integer` | Przechowuje całościowe wartości liczbowe. |

## Dowód sqlmigrate
```sql
-- Wynik komendy: python manage.py sqlmigrate boardgames 0001
CREATE TABLE "boardgames_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "description" text NOT NULL);
CREATE TABLE "boardgames_game" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "price" decimal NOT NULL, "release_date" date NOT NULL, "players_count" integer NOT NULL, "description" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "boardgames_category" ("id") DEFERRABLE INITIALLY DEFERRED);