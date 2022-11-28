import {useState} from "react";
import './styles/config.css';

export default function Config() {
    const [mail, setMail] = useState([]);

    function handleInputMail(event) {
        setMail(event.target.value);
    }

    /**
     * Vérifie qu'une adresse mail a une syntaxe correcte
     * @param address adresse mail à vérifier
     * @returns {*} true si l'adresse est correcte
     */
    function isEmail(address) {
        let regexMail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        return address.match(regexMail);
    }

    /**
     * Constitue un header pour une requête POST
     * @param raw données à inclure pour la requête
     * @returns {{redirect: string, headers: Headers, method: string, body}} le header formulé pour une requête POST
     */
    function header(raw) {
        let myHeaders = new Headers();
        myHeaders.append("Authorization", "Basic ZTE5MDA5MDE6R3JlZ29pcmU1NjI0MA==");
        myHeaders.append("Content-Type", "application/json");

        return {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };
    }

    function handleAddMail() {
        if(isEmail(mail)) {
            let myHeaders = new Headers();
            myHeaders.append("Authorization", "Basic ZTE5MDA5MDE6R3JlZ29pcmU1NjI0MA==");
            myHeaders.append("Content-Type", "application/json");

            const raw = JSON.stringify({"email": mail});

            fetch("http://127.0.0.1:5000/add_email", header(raw))
                .then(response => response.text())
                .then(result => {
                    console.log(result);
                    alert("Adresse email correctement ajoutée");
                })
                .catch(error => alert("Erreur - "+ error));
        }else{
            alert("Adresse email invalide !");
        }
    }

    function handleDelMail() {
        if(isEmail(mail)) {
            let myHeaders = new Headers();
            myHeaders.append("Authorization", "Basic ZTE5MDA5MDE6R3JlZ29pcmU1NjI0MA==");
            myHeaders.append("Content-Type", "application/json");

            const raw = JSON.stringify({"email": mail});

            fetch("http://127.0.0.1:5000/del_email", header(raw))
                .then(response => response.text())
                .then(result => {
                    console.log(result);
                    alert("Adresse email correctement supprimée");
                })
                .catch(error => alert("Erreur - "+ error));
        }else{
            alert("Adresse email invalide !");
        }
    }

    function handleSubmit() {
        let myHeaders = new Headers();
        myHeaders.append("Authorization", "Basic ZTE5MDA5MDE6R3JlZ29pcmU1NjI0MA==");
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/send_alert", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
    }

    return (
        <section id="haut" className="config">
            <article>
                <h2>Configuration</h2>
                <hr/>

                <div className="item">
                    <h3>Paramétrage d'alertes mail</h3>
                    <label>
                        Ajouter une adresse mail
                        <div className="input-mail">
                            <input placeholder="maxence.jung@univ-ubs.fr" type="email" onChange={handleInputMail} />
                            <button name="add" onClick={handleAddMail}><span className="material-symbols-outlined">add</span></button>
                            <button name="del" onClick={handleDelMail}><span className="material-symbols-outlined">delete</span></button>
                        </div>
                    </label>

                    <button className="submit" onClick={handleSubmit}><span className="material-symbols-outlined">notification_important</span> Envoyer une alerte</button>
                </div>
            </article>
        </section>
    );
}