import '../styles/affichage-salles.css';
import ListeSalles from "./liste-salles";

export default function AffichageSalles({handleClick}) {
    return (
        <div className="item" id="salles">
            <h3>Salles</h3>

            <details id="ENSIBS">
                <summary>ENSIBS</summary>
                <ul><ListeSalles batiment={"ENSIBS"} handleClick={handleClick} /></ul>
            </details>

            <details id="DSEG">
                <summary>DSEG</summary>
                <ul><ListeSalles batiment={"DSEG"} handleClick={handleClick} /></ul>
            </details>

            <details id="YC">
                <summary>Yves Coppens</summary>
                <ul><ListeSalles batiment={"YC"} handleClick={handleClick} /></ul>
            </details>

            <details id="Autres">
                <summary>Autres</summary>
                <ul><ListeSalles batiment={"Autres"} handleClick={handleClick} /></ul>
            </details>
        </div>
    );
}