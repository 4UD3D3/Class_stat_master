import {Link} from 'react-router-dom';
import {useContext} from "react";
import Auth from "./contexts/auth";
import {logout} from "./services/authAPI";

export default function Header() {
    const {isAuthenticated, setIsAuthenticated} = useContext(Auth);

    const handleLogout = () => {
        logout();
        setIsAuthenticated(false);
    }

    const handleLinkClick = () => { // pour refermer le menu, sur téléphone
        document.getElementById("mobile-menu").checked = false;
    };

    function displayUser() {
        if(!isAuthenticated){
            return (
                <ul>
                    <li className="identify" id="identify">
                        <Link to="/connexion" className="title-menu">Connexion <span className="material-symbols-outlined">bolt</span></Link>
                    </li>
                </ul>
            );
        }
        return (
            <ul>
                <li><Link to="/config" onClick={handleLinkClick}>Configuration</Link></li>
                <li><Link to="/" onClick={handleLinkClick}>Statistiques Utilisateur</Link></li>
                <li><a href="https://ent.univ-ubs.fr/" target="_blank" rel="noreferrer">ENT UBS</a></li>

                <li className="identify" id="identify">
                    <label htmlFor="title-menu-tel3">Maxence Jung <span className="material-symbols-outlined">expand_more</span></label>
                    <input type="checkbox" className="title-menu-tel" id="title-menu-tel3" />

                    <div className="sous-menu">
                        <Link to="/">Profil</Link>
                        <a onClick={handleLogout}>Déconnexion</a> {/* TODO : à transformer */}
                    </div>
                    <span className="title-menu">Maxence Jung <span className="material-symbols-outlined">expand_more</span></span>
                </li>
            </ul>
        );
    }

    return (
        <header id="header">
            <Link to="/"><h1>classtat</h1></Link>

            <input type="checkbox" id="mobile-menu"/>
            <label htmlFor="mobile-menu"><span className="material-symbols-outlined">menu</span></label>

            <nav id="menu">
                {displayUser()}
            </nav>
        </header>
    );
}