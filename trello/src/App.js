import React from "react";
import Board from "react-trello";

import {generator} from "./generateCustomers";
import "./App.css";

export function App() {
    console.log("ssss", generator());
    return (
        <div className="App">
            <h1>ОбЪединение закупщиков</h1>
            <Board data={generator()} draggable style={{backgroundColor: '#b4b1b1'}}/>
        </div>
    );
}
