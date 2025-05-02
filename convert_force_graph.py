import json
import os

# Path to your original JSON
source_path = "dataset_subsets/json_files/rachel_viz.json"
output_path = "frontend/public/visualizations/haunted-force.json"

# Load your original data
with open(source_path) as f:
    raw = json.load(f)
    data = raw["rachel_viz"]

nodes = {}
links = []

def clean(val):
    if isinstance(val, str):
        return val.strip('"').strip()
    return val or "Unknown"

def add_node(value, group):
    if value and value not in nodes:
        nodes[value] = {
            "id": value,
            "group": group,
            "size": 1
        }
    elif value:
        nodes[value]["size"] += 1

for item in data:
    time = clean(item.get('"Time of Day"', 'Unknown'))
    event = clean(item.get('"Event type"', 'Unknown'))
    apparition = clean(item.get('"Apparition Type"', 'Unknown'))

    add_node(time, "Time")
    add_node(event, "Event")
    add_node(apparition, "Apparition")

    if time and event:
        links.append({"source": time, "target": event, "value": 1})
    if event and apparition:
        links.append({"source": event, "target": apparition, "value": 1})

# Final clean-up: remove links with missing nodes
valid_links = [link for link in links if link["source"] and link["target"]]

# Combine into final format
output = {
    "nodes": list(nodes.values()),
    "links": valid_links
}

# Write to frontend
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"Created {output_path} with {len(output['nodes'])} nodes and {len(output['links'])} links.")