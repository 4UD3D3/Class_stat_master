import {useState} from "react";

export default function Params({salles, setDataFunc}){
    const [dateDebut, setDateDebut] = useState(getDateAjd()); // par défaut, date d'ajd
    const handleDateDebut = (event) => {
        setDateDebut(event.target.value);
    };

    const [dateFin, setDateFin] = useState(getDateDem());
    const handleDateFin = (event) => {
        setDateFin(event.target.value);
    };

    function handleSubmit() {
        if(salles.length > 0) { // vérifie si une salle a été spécifiée
            if (dateDebut < dateFin) {

                let myHeaders = new Headers();
                myHeaders.append("Authorization", "Basic ZTE5MDA5MDE6R3JlZ29pcmU1NjI0MA==");
                myHeaders.append("Content-Type", "application/json");

                const raw = JSON.stringify({
                    "start_date": dateDebut.toString().replace('-', '').replace('-', ''),
                    "end_date": dateFin.toString().replace('-', '').replace('-', ''),
                    "rooms_list": salles
                });

                const requestOptions = {
                    method: 'POST',
                    headers: myHeaders,
                    body: raw,
                    redirect: 'follow'
                };

                fetch("http://127.0.0.1:5000/data", requestOptions)
                    .then(function(response) {
                        return response.text();
                    })
                    .then(function(result) {
                        setDataFunc(JSON.parse(result));
                    })
                    .catch(error => console.log('error', error));
                    /*.then(response => response.text())
                    .then(result => console.log(result))
                    .catch(error => console.log('error', error));*/
            } else alert("Vérifiez les dates entrées : une date de début ne peut être après une date de fin !");
        }  else alert("Sélectionnez une salle !");
    }

    return(
        <div className="item" id="params">
            <h3>Paramètres</h3>

            <label>
                du
                <input type="date" id="debut" onChange={event => handleDateDebut(event)} defaultValue={getDateAjd()} />
            </label>

            <label>
                au
                <input type="date" id="fin" onChange={event => handleDateFin(event)} defaultValue={getDateDem()} />
            </label>

            {afficheSalle(salles)}
            <button className="submit" onClick={handleSubmit}>Exporter</button>
        </div>
    );
}

function afficheSalle(salles){
    if(salles.length > 0){ // vérifie s'il s'agit d'un tableau de string
        return (
            <div>
                Salles sélectionnées
                <ul style={{paddingLeft: 0, marginTop: "0.5em", fontSize: "0.9em"}}>
                    {salles.map(s =>
                        <li className="item-salle" key={s}>{s}</li>
                    )}
                </ul>
            </div>
        );
    }
    return <p>Sélectionner une salle</p>;
}

/** Renvoie la date d'aujourd'hui */
function getDateAjd(){
    return (new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().substring(0,10));
}
/** Renvoie la date de demain */
function getDateDem(){
    return (new Date(Date.now()+86400000 - new Date().getTimezoneOffset() * 60000).toISOString().substring(0,10)); // 86400000 est le nb de milisecondes
}