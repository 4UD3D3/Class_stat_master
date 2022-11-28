import jwtDecode from "jwt-decode";
import {getItem, addItem, removeItem} from "./localStorage";

export function hasAuthenticated(){
    const token = getItem('classtatToken');
    const tokenValide = token ? tokenIsValid(token) : false;

    if(!tokenValide){
        removeItem('classtatToken');
    }
    return tokenValide;
}

export function login(cred){
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify(cred);

    const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    return fetch("http://127.0.0.1:5000/login", requestOptions)
        .then(response => {
            if (response.ok){
                return response.text()
            }
            return Promise.reject(response);
        })
        .then(result => {
            let dataRes = JSON.parse(result);
            addItem('classtatToken', dataRes['token']);
            return true;
        })
        .catch((response) => {return response.status()});
    /*axios.post('https://localhost:5000/login', cred)
                .then(response => response.data.token)
                .then(token => {
                    addItem('classtatToken', token);
                    return true;
                });*/
}

export function logout(){
    removeItem('classtatToken');
}

function tokenIsValid(token){
    const {exp} = jwtDecode(token);
    return exp * 1000 > new Date().getTime();
}