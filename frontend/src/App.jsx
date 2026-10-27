import { useState } from 'react';
import { initialGames } from './data';
import { GameCard } from './components/GameCard';

function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [selectedGame, setSelectedGame] = useState(null);

  // Wyliczenie unikalnych kategorii z danych
  const categories = [...new Set(initialGames.map(g => g.category))];

  // Połączone filtrowanie (wyszukiwarka + kategoria)
  const filteredGames = initialGames.filter(game => {
    const matchesSearch = game.title.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === "" || game.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  // Widok szczegółów (Zadanie 8)
  if (selectedGame) {
    return (
      <div style={{ padding: '20px' }}>
        <h2>{selectedGame.title}</h2>
        <p><strong>Kategoria:</strong> {selectedGame.category}</p>
        <p><strong>Cena:</strong> {selectedGame.price.toFixed(2)} PLN</p>
        <p><strong>Data premiery:</strong> {selectedGame.release_date}</p>
        <p><strong>Liczba graczy:</strong> {selectedGame.players_count}</p>
        <button onClick={() => setSelectedGame(null)} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Powrót do listy
        </button>
      </div>
    );
  }

  // Główny widok listy z filtrami
  return (
    <div style={{ padding: '20px' }}>
      <h1>Katalog Gier Planszowych</h1>

      {/* Wyszukiwarka tekstowa (Zadanie 6) */}
      <div style={{ marginBottom: '15px' }}>
        <input 
          type="text" 
          placeholder="Szukaj gry..." 
          value={searchTerm} 
          onChange={(e) => setSearchTerm(e.target.value)} 
          style={{ padding: '8px', marginRight: '10px', width: '200px' }}
        />

        {/* Filtr rozwijany kategorii (Zadanie 7) */}
        <select 
          value={selectedCategory} 
          onChange={(e) => setSelectedCategory(e.target.value)}
          style={{ padding: '8px' }}
        >
          <option value="">Wszystkie kategorie</option>
          {categories.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>

      {/* Komunikat, gdy nic nie pasuje do filtrów */}
      {filteredGames.length === 0 && (
        <p style={{ color: 'red' }}>Brak gier spełniających kryteria wyszukiwania.</p>
      )}

      {/* Lista gier renderowana przez map() (Zadanie 4) */}
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {filteredGames.map(game => (
          <GameCard 
            key={game.id} 
            game={game} 
            onSelect={setSelectedGame} 
          />
        ))}
      </div>
    </div>
  );
}
import { useEffect } from 'react';

// wewnątrz komponentu App:
useEffect(() => {
  fetch('http://127.0.0.1:8000/api/games/')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error("Błąd fetch:", err));
}, []);



export default App;
