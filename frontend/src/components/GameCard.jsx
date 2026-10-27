// frontend/src/components/GameCard.jsx
export function GameCard({ game, onSelect }) {
  return (
    <div className="game-card" onClick={() => onSelect(game)} style={{ border: '1px solid #ccc', padding: '15px', margin: '10px', borderRadius: '8px', cursor: 'pointer' }}>
      <h3>{game.title}</h3>
      <p><strong>Kategoria:</strong> {game.category}</p>
      <p><strong>Cena:</strong> {game.price.toFixed(2)} PLN</p> {/* Sformatowane pole liczbowe */}
      <p><strong>Max graczy:</strong> {game.players_count} osób</p>
    </div>
  );
}
<p>{game.price > 200 ? "🔥 Droga gra" : "✅ Przystępna cena"}</p>
{game.players_count > 4 && <span style={{ color: "red" }}>W sam raz na imprezę!</span>}