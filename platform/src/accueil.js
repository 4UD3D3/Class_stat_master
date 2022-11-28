import {useState} from "react";
import './styles/accueil.css';
import Params from "./ressources/params";
import AffichageSalles from "./ressources/affichage-salles";
import Planning from "./ressources/planning";

function Accueil() {
    const [li, setSalle] = useState([]);
    const handleClick = (salle) => { // ajoute une salle à la liste des salles
        if(!li.includes(salle)){
            setSalle(li => [...li, salle]);
        }else{
            setSalle(li.filter(s => s !== salle));
        }
    };

    const [data, setData] = useState("");

    return (
        <section id="haut" className="accueil">
            <article>
                <h2>Disponibilité des salles</h2>
                <hr/>

                <div id="salles-planning">
                    <AffichageSalles handleClick={handleClick} />

                    <Params salles={li} setDataFunc={setData} />
                </div>
            </article>

            <article id="item2">
                <h2>Planning</h2>
                <hr/>
                <Planning cal={data} />
                <br />
            </article>
        </section>
    );
}

export default Accueil;