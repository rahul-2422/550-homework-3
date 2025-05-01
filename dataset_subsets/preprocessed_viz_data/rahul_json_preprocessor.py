import json
from collections import defaultdict
from pathlib import Path
import os

# ---- Config ----
INPUT_PATH = os.path.abspath("dataset_subsets/json_files/rahul_viz.json")
OUTPUT_PATH = os.path.abspath(
    "dataset_subsets/preprocessed_viz_data/sankey_data.json"
)
# OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# ---- Step 1: Load original JSON ----
with open(INPUT_PATH, "r") as f:
    raw_data: json = json.load(f)["rahul_viz"]

# ---- Step 2: Count edges across stages ----
edge_counter = defaultdict(int)

for entry in raw_data:
    # Clean keys (remove quotes)
    event_type = entry.get('"Event type"', "").strip()
    time_of_day = entry.get('"Time of Day"', "").strip()
    evidence = entry.get('"Combined_Evidence"', "").strip()
    state = entry.get('"state"', "").strip()
    witness_group = entry.get('"Witness_Count_Group"', "").strip()

    # Skip incomplete rows
    if not all([event_type, time_of_day, evidence, state, witness_group]):
        continue

    if "Unknown" in [event_type, time_of_day, evidence, state, witness_group]:
        continue

    # Build edges
    path = [
        (event_type, time_of_day),
        (time_of_day, evidence),
        (evidence, state),
        (state, witness_group),
    ]

    for source, target in path:
        edge_counter[(source, target)] += 1

# ---- Step 3: Convert to D3 Sankey format ----
sankey_links = [
    {"source": src, "target": tgt, "value": count}
    for (src, tgt), count in edge_counter.items()
]

# ---- Step 4: Save formatted JSON ----
with open(OUTPUT_PATH, "w") as f:
    json.dump(sankey_links, f, indent=2)

print(f"✅ Sankey data saved to: {OUTPUT_PATH}")
