//import cal from './test/creneaux.json';
import Cell from './cell';
import '../styles/planning.css';
import { useState } from "react";
import {
    format,
    subMonths,
    addMonths,
    startOfWeek,
    addDays,
    getWeek,
    addWeeks,
    subWeeks
} from "date-fns"; // https://date-fns.org/

/**
 * Header:
 * icon for switching to the previous month,
 * formatted date showing current month and year,
 * another icon for switching to next month
 * icons should also handle onClick events to change a month
 */
const Planning = ({cal}) => {
    const [currentMonth, setCurrentMonth] = useState(new Date());
    const [currentWeek, setCurrentWeek] = useState(getWeek(currentMonth, {weekStartsOn: 1, firstWeekContainsDate: 7}));

    const dico ={"Mon":"D1_Lundi",
                "Tue":"D2_Mardi",
                "Wed":"D3_Mercredi",
                "Thu":"D4_Jeudi",
                "Fri":"D5_Vendredi",
                "Sat":"D6_Samedi",
                "Sun":"D7_Dimanche"}


    /* GESTION DES EVENEMENTS */

    const changeMonthHandle = (btnType) => {
        if (btnType === "prev") {
            let newMonth = subMonths(currentMonth, 1)
            setCurrentMonth(newMonth);
            setCurrentWeek(getWeek(newMonth, {weekStartsOn: 1, firstWeekContainsDate: 7}));
        }
        if (btnType === "next") {
            let newMonth = addMonths(currentMonth, 1)
            setCurrentMonth(newMonth);
            setCurrentWeek(getWeek(newMonth, {weekStartsOn: 1, firstWeekContainsDate: 7}));
        }
    };
    const changeWeekHandle = (btnType) => {
        //console.log("current week", currentWeek);
        if (btnType === "prev") {
            //console.log(subWeeks(currentMonth, 1));
            setCurrentMonth(subWeeks(currentMonth, 1));
            setCurrentWeek(getWeek(subWeeks(currentMonth, 1), {weekStartsOn: 1, firstWeekContainsDate: 7}));
        }
        if (btnType === "next") {
            //console.log(addWeeks(currentMonth, 1));
            setCurrentMonth(addWeeks(currentMonth, 1));
            setCurrentWeek(getWeek(addWeeks(currentMonth, 1), {weekStartsOn: 1, firstWeekContainsDate: 7}));
        }
    };
    /*const onDateClickHandle = (day, dayStr) => {
        setSelectedDate(day);
        showDetailsHandle(dayStr);
    };*/


    /* FONCTIONS UTILES */

    function getAnnee() {
        return cal[1][format(currentMonth, 'yyyy')];
    }
    function getSemaine() {
        return getAnnee()[currentWeek.toString()];
    }
    function getJour(day){
        return getSemaine()[day];
    }


    /**
     * Données des cellules mises en forme
     *
     * @returns {*} la liste de liste de créneaux d'une journée
     */
    function getListeCell() {
        /**
         * Liste contenant chaque 'liste de créneaux d'une journée'
         * @type {*[list]}
         */
        let listeJoursRendu = [];

        for(let jour in dico){
            if(Array.isArray(cal) && format(currentMonth, 'yyyy') in cal[0] && currentWeek.toString() in getAnnee()) { // vérifie si les données existent pour la semaine donnée
                let jourData = getJour(dico[jour]);

                /**
                 * Liste des créneaux d'une journée
                 * @type {*[]}
                 */
                let listeCellJour = [];

                if (typeof (jourData) !== "undefined") {
                    for (let cren in jourData) { // obtenir les créneaux
                        listeCellJour.push(<Cell key={cren} sallesOcc={jourData[cren]}/>);
                    }
                }

                listeJoursRendu.push(<div key={jour} className="jour-cell">{listeCellJour}</div>);
            }
        }

        return listeJoursRendu;
    }


    /* RENDUS */

    /**
     * Affiche les mois en en-tête du calendrier
     * @returns {JSX.Element} mois
     */
    const renderMois = () => {
        const dateFormat = "MMM yyyy";
        return (
            <div className="sel-mois">
                <span className="material-symbols-outlined" onClick={() => changeMonthHandle("prev")}>arrow_back_ios</span>
                <span>{format(currentMonth, dateFormat)}</span>
                <span className="material-symbols-outlined" onClick={() => changeMonthHandle("next")}>arrow_forward_ios</span>
            </div>
        );
    };
    /**
     * Affiche la semaine en en-tête du calendrier
     * @returns {JSX.Element} numéro de semaine
     */
    const renderSemaine = () => {
        return (
            <div className="sel-semaine">
                <span className="material-symbols-outlined" onClick={() => changeWeekHandle("prev")}>arrow_back</span>
                <span>Semaine {currentWeek}</span>
                <span className="material-symbols-outlined" onClick={() => changeWeekHandle("next")}>arrow_forward</span>
            </div>
        );
    };
    /**
     * Affiche les jours de la semaine en haut du calendrier
     * @returns {JSX.Element} liste des jours
     */
    const renderJours = () => {
        const dateFormat = "EEE";
        const dateNumFormat = "d";

        const days = [];
        let startDate = startOfWeek(currentMonth, { weekStartsOn: 1 });
        for (let i = 0; i < 7; i++) {
            days.push(<div className="jour" key={i}>{dico[format(addDays(startDate, i), dateFormat)].slice(3,6)} {format(addDays(startDate, i), dateNumFormat)}</div>);
        }
        return <div className="liste-jours">{days}</div>;
    };
    /**
     * Affiche les heures sur la gauche de la timetable
     * @returns {JSX.Element} liste des créneaux horaires
     */
    const renderCreneaux = () => {
        return (
            <div className="creneaux">
                <span>8h-9h30</span>
                <span>9h45-11h15</span>
                <span>11h30-13h</span>
                <span>13h-14h30</span>
                <span>14h45-16h15</span>
                <span>16h30-18h</span>
                <span>18h15-19h45</span>
            </div>
        );
    }
    /**
     * Affiche toutes les cellules de la timetable
     * @returns {JSX.Element}
     */
    function renderMoment() {
        let listeJoursRendu = getListeCell();

        return <div className="liste-jours-cell">{listeJoursRendu}</div>
    }


    return (
        <div className="calendar">
            {renderMois()}
            {renderSemaine()}
            <div className="semainier">
                {renderCreneaux()}
                <div className="timetable">
                    {renderJours()}
                    {renderMoment()}
                </div>
            </div>
        </div>
    );
};

export default Planning;