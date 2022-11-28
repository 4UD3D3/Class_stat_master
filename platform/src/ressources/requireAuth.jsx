import React, {useContext} from 'react';
import Auth from "../contexts/auth";
import {Navigate} from "react-router-dom";

const RequireAuth = ({element}) => {
    const {isAuthenticated} = useContext(Auth);

    if (!isAuthenticated) {
        return <Navigate to="/portail"/>;
    }
    return element;
}

export default RequireAuth;