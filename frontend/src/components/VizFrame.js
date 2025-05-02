import React from "react";

const VizFrame = ({ filename }) => {
  const isSankey = filename.includes("sankey");

  return (
    <iframe
      title={filename}
      src={`/visualizations/${filename}`}
      width="100%"
      height={isSankey ? "800px" : "900px"}
      style={{
        border: "1px solid #ddd",
        borderRadius: "8px",
        backgroundColor: "#fff",
        boxShadow: "0 2px 8px rgba(0,0,0,0.05)",
        overflow: "hidden",
      }}
    />
  );
};

export default VizFrame;
