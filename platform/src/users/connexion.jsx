import React, {useContext, useEffect, useState} from 'react';
import Auth from "../contexts/auth";
import {login} from "../services/authAPI";

const Connexion = ({history}) => {
    const {isAuthenticated, setIsAuthenticated} = useContext(Auth);

    const [user, setUser] = useState({
        user: "",
        password: ""
    });

    const [status, setStatus] = useState('');

    useEffect(() => {
        if(isAuthenticated){
            window.location.replace('/');
        }
    }, [history, isAuthenticated])


    const handleChange = ({currentTarget}) => {
        const {name, value} = currentTarget;

        setUser({...user, [name]: value});
    }

    const handleSubmit = async event => {
        event.preventDefault();

        try {
            const response = await login(user);
            setIsAuthenticated(response);
        } catch({response}) {
            setStatus('Identifiant ou mot de passe incorrects');
        }
    }

    function displayError() {
        if(status!==""){
            return (
                <div style={{padding: "0.5em 1.5em", border: "1px solid transparent", marginTop: "1.5em", borderRadius: "4px", color: "#a94442", backgroundColor: "#f2dede", borderColor: "#ebccd1"}}>
                    <p>{status}</p>
                </div>
            );
        }
        return null;
    }

    return (
        <section id="haut" className="connexion">
            <article>
                <h2>Connexion</h2>
                <hr/>

                <form className="item" onSubmit={handleSubmit}>
                    <label>
                        Nom d'utilisateur
                        <div className="input-mail">
                            <input name="user" type="text" onChange={handleChange} placeholder="Maxence" />
                        </div>
                    </label>

                    <label>
                        Mot de passe
                        <div className="input-mail">
                            <input name="password" type="password" onChange={handleChange} placeholder="********" />
                        </div>
                    </label>

                    <button className="submit" type="submit">Connexion</button>

                    {displayError()}
                </form>
            </article>
        </section>
    )
}

export default Connexion;