# Boardgames DB API

Projekt katalogu gier planszowych z bazą danych SQLite i Django ORM.

## Instrukcja uruchomienia

Komenda instalacji: npm install

Komenda uruchomienia dev: npm run dev

http://127.0.0.1:8000/api/games/

dane początkowe są ładowane statycznie z pliku src/data.js odwzorowującego strukturę bazy danych.

# Boardgames DB

Projekt aplikacji webowej do zarządzania bazą danych gier planszowych, składający się z backendu opartego na frameworku Django oraz frontendu przygotowanego w React (Vite).

---

## 📦 Architektura i Moduły Projektu

| Moduł | Technologia | Ścieżka / Opis |
| :--- | :--- | :--- |
| **Backend** | Python, Django, Django REST Framework | Główny katalog projektu (`/`) – obsługa API, bazy danych oraz polityki CORS. |
| **Frontend** | React, Vite, JavaScript | Katalog `/frontend` – interfejs użytkownika, wyszukiwarka, filtry i widok szczegółów. |
| **Dokumentacja**| Markdown | Katalog `/docs/cors.md` – opis testów bezpieczeństwa, nagłówków i zmiennych środowiskowych. |

---

## 🚀 Instrukcja Uruchomienia (Krok po kroku)

### 1. Sklonowanie repozytorium
```bash
git clone [https://github.com/TwojLogin/boardgames-db.git](https://github.com/TwojLogin/boardgames-db.git)
cd boardgames-db

### 2. Konfiguracja i uruchomienie Backendu (Django)
```bash
W pierwszym oknie terminala wykonaj polecenia:

# Utworzenie i aktywacja środowiska wirtualnego
python -m venv venv
source venv/Scripts/activate  # (lub source venv/bin/activate na systemach Linux/macOS)

# Instalacja zależności
pip install -r requirements.txt

# Skopiowanie pliku konfiguracyjnego środowiska
cp .env.example .env

(Upewnij się, że plik .env zawiera wymagane zmienne, takie jak SECRET_KEY).
Uruchom serwer deweloperski Pythona:

python manage.py runserver

3. Konfiguracja i uruchomienie Frontend (React / Vite)
W drugim oknie terminala przejdź do katalogu frontendu:

cd frontend

# Instalacja zależności Node.js
npm install

# Skopiowanie pliku konfiguracyjnego środowiska
cp .env.example .env

Uruchom serwer deweloperski frontendu:
npm run dev