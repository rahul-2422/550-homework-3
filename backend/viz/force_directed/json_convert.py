# tsv_to_forcejson.py
import csv
import json
from collections import defaultdict
from pathlib import Path

# Use relative paths for portability
input_file = Path('rachel_viz.tsv')
output_file = Path('haunted-force.json')

# Create containers for nodes and links
node_types = ['Time of Day', 'Event type', 'Apparition Type', 'Image/Video/Visual Evidence', 'Audio Evidence']
node_groups = {
    'Time of Day': 'Time',
    'Event type': 'Event',
    'Apparition Type': 'Apparition',
    'Image/Video/Visual Evidence': 'Evidence',
    'Audio Evidence': 'Evidence'
}

node_map = {}  # Maps (type, value) -> node index
nodes = []
links = []
node_counts = defaultdict(int)

# Helper to add/get node index
def get_node_index(node_type, value):
    key = (node_type, value)
    if key not in node_map:
        node_map[key] = len(nodes)
        nodes.append({
            'id': value,
            'group': node_groups[node_type],
            'type': node_type,
            'size': 1
        })
    else:
        nodes[node_map[key]]['size'] += 1
    return node_map[key]

# Read TSV and build nodes/links
with input_file.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        # Clean and extract values
        time_val = row['Time of Day'] or 'Unknown'
        event_val = row['Event type'] or 'Unknown'
        app_val = row['Apparition Type'] or 'Unknown'
        vis_val = 'Visual Evidence' if row['Image/Video/Visual Evidence'].strip().lower() == 'true' else None
        aud_val = 'Audio Evidence' if row['Audio Evidence'].strip().lower() == 'true' else None

        # Build list of present entities for this row
        entities = [
            ('Time of Day', time_val),
            ('Event type', event_val),
            ('Apparition Type', app_val)
        ]
        if vis_val:
            entities.append(('Image/Video/Visual Evidence', vis_val))
        if aud_val:
            entities.append(('Audio Evidence', aud_val))

        # Add nodes and links for all pairs in this row
        indices = [get_node_index(t, v) for t, v in entities]
        for i in range(len(indices)):
            for j in range(i+1, len(indices)):
                links.append({
                    'source': indices[i],
                    'target': indices[j],
                    'value': 1
                })

# Save as JSON
with output_file.open('w', encoding='utf-8') as f:
    json.dump({'nodes': nodes, 'links': links}, f, indent=2)

print(f"Converted {input_file} to {output_file} for D3 force-directed graph.")
