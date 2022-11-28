import logoENSIBS from './styles/images/ENSIBS-LOGO-blanc.png';
import illustrationData from './styles/images/Data_report-pana.svg';
import './styles/portail.css';
import {Link} from "react-router-dom";

export default function Portail() {
    return (
        <section id="haut" className="portail">
            <article id="item-portail">
                <h2>Bienvenue sur Classtat</h2>
                <hr/>
                {/* illustration : https://storyset.com/data - Data illustrations by Storyset */}

                <p>Visualisez et analysez les statistiques d'occupation des salles de l'UBS en temps réel.</p>
                <p>Afin d'accéder à la plateforme, veuillez vous authentifier.</p>

                <div className="illustration">
                    <img src={illustrationData} alt="Des gens qui discutent de ronds et bâtons" />
                </div>

                <Link to='/connexion'><div className="connexion"><button className="submit">Connexion</button></div></Link>
            </article>

            <article id="item-footer">
                <p>Site réalisé par<br/> Grégoire Truhé, Andréa Gainche, Mehdi Le Floch et Nassim Hmamouche</p>
                <img id="logo" src={logoENSIBS} alt="Logo de l'ENSIBS" />
            </article>
        </section>
    );
}