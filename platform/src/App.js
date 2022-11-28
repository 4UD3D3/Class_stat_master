import React, {useState} from "react";
import {BrowserRouter, Routes, Route} from 'react-router-dom';

import './styles/header.css';
import './styles/main.css';
// import './styles/footer.css';

import Header from "./header";
// import Footer from "./ressources_jsx/footer";
import Portail from "./portail";
import Accueil from "./accueil";
import Config from "./config";
import Auth from './contexts/auth'
import RequireAuth from "./ressources/requireAuth";
import {hasAuthenticated} from "./services/authAPI";
import Connexion from "./users/connexion";

function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(hasAuthenticated());

    return (
        <Auth.Provider value={{isAuthenticated, setIsAuthenticated}}>
            <BrowserRouter>
                <Header/>
                <Routes>
                    <Route path="/portail" element={<Portail/>}/>
                    <Route path="/connexion" element={<Connexion/>}/>
                    <Route path="/" element={
                        <RequireAuth element={<Accueil/>}></RequireAuth>
                    }/>
                    <Route path="/config" element={
                        <RequireAuth element={<Config/>}></RequireAuth>
                    }/>
                </Routes>
            </BrowserRouter>
        </Auth.Provider>
    );
}

export default App;
