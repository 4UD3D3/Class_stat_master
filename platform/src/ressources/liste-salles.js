import dataSalle from './test/test_icsFile-Salles.json';

const ListeSalles = ({batiment, handleClick}) => {
    return filtreBat(batiment).map((salle) =>
        <li key={salle}>
            <input type="button" id={salle} value={salle} onClick={(event) => handleClick(salle)} />
        </li>
    );
}
export default ListeSalles;


function filtreBat(batiment){
    /**
     *  • Parcours des clés [A104, D010...]
     *  • Liaison avec entrée de map, ex : si bat == "ENSIBS" alors on ajoute à la liste
     */
    let liFiltree = [];
    dataSalle.map( salle => {
        if(salle.bat === batiment){
            liFiltree.push(salle.nom);
        }
        return null;
    })

    return liFiltree.sort();
}