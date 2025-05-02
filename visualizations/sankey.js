// d3_vis/sankey/sankey.js

const sankeyDataUrl = "./sankey_data.json";

const svg = d3.select("#sankey"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

const sankey = d3.sankey()
    .nodeWidth(20)
    .nodePadding(10)
    .extent([[1, 1], [width - 1, height - 6]]);

const color = d3.scaleOrdinal(d3.schemeCategory10);

d3.json(sankeyDataUrl).then(rawLinks => {
    // extract all unique nodes
    const nodesSet = new Set();
    rawLinks.forEach(l => {
        nodesSet.add(l.source);
        nodesSet.add(l.target);
    });

    const nodes = Array.from(nodesSet).map(name => ({ name }));
    const nameToIndex = Object.fromEntries(nodes.map((d, i) => [d.name, i]));

    const links = rawLinks.map(d => ({
        source: nameToIndex[d.source],
        target: nameToIndex[d.target],
        value: d.value
    }));

    const graph = sankey({
        nodes: nodes.map(d => Object.assign({}, d)),
        links: links
    });

    // Draw links
    svg.append("g")
        .selectAll("path")
        .data(graph.links)
        .join("path")
        .attr("d", d3.sankeyLinkHorizontal())
        .attr("class", "link")
        .attr("stroke-width", d => Math.max(1, d.width))
        .attr("stroke", "#999")
        .attr("fill", "none")
        .attr("opacity", 0.4);

    // Draw nodes
    const node = svg.append("g")
        .selectAll("g")
        .data(graph.nodes)
        .join("g")
        .attr("class", "node")
        .attr("transform", d => `translate(${d.x0},${d.y0})`);

    node.append("rect")
        .attr("height", d => d.y1 - d.y0)
        .attr("width", sankey.nodeWidth())
        .attr("fill", d => color(d.name));

    node.append("text")
        .attr("x", -6)
        .attr("y", d => (d.y1 - d.y0) / 2)
        .attr("dy", "0.35em")
        .attr("text-anchor", "end")
        .text(d => d.name)
        .filter(d => d.x0 < width / 2)
        .attr("x", 6 + sankey.nodeWidth())
        .attr("text-anchor", "start");
});
