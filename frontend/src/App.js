import React, { useState } from "react";
import VizFrame from "./components/VizFrame";
import "./App.css";

const FILES = {
  "Force Directed Graph": "force_graph.html",
  Heatmap: "heatmap.html",
  "Sankey Diagram": "sankey.html",
  "Evan's Viz": "sankey.html",
  "NER Word Cloud": "rohit.html",
};

function App() {
  const [selected, setSelected] = useState("Force Directed Graph");

  return (
    <div className="App">
      <header>
        <h1>Team 3: Haunted Places Visualizations</h1>
        <p className="subheader">
          Created by Rachel, Angel, Evan, Rahul, Rohit, and Aditya
        </p>
      </header>

      <nav>
        {Object.keys(FILES).map((label) => (
          <button
            key={label}
            className={selected === label ? "tab active" : "tab"}
            onClick={() => setSelected(label)}
          >
            {label}
          </button>
        ))}
      </nav>

      <main>
        <h2 className="viz-title">{selected}</h2>
        <VizFrame filename={FILES[selected]} />
      </main>
    </div>
  );
}

export default App;
