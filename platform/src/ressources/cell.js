/**
 * Cellule contenant les infos sur une salle, quand on clique dessus : affiche les salles occupées
 *
 * @param sallesOcc liste des salles occupées
 * @returns {JSX.Element} une cellule, avec une couleur en fonction du taux d'occupation à ce créneau
 */
export default function Cell({sallesOcc}){
    const color = {filter: `hue-rotate(${sallesOcc.length * -10}deg)` }

    return (
        <div className="cell" style={color}>{sallesOcc.length}</div>
    );
}