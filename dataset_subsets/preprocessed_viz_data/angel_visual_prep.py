import pandas as pd

# Load dataset
tsv_file = "../orginal_dataset/haunted_places_final_all_features.tsv"  
df = pd.read_csv(tsv_file, sep="\t")

# Make a copy before data processing
visual_data = df[['Time of Day', 'Event type']].copy()

# Fill all na values in event type as Unknown event
visual_data['Event type'] = visual_data['Event type'].fillna('Unknown')

# Edit the event name to make it shorter
edit_name = {
    "Object and Environmental Manipulation": "Object/Enviromental Manipulation",
    "Mysterious Occurrences": "Mysterious Occurrences",
    "Ghostly Sightings": "Ghostly Sightings",
    "Sounds and Noises": "Sounds/Noises",
    "Violent or Tragic Deaths": "Violent/Tragic Deaths",
    "Unexplained Movements and Physical Manifestations": "Unexplained Physical Manifestations",
    "Fire and Destruction": "Fire/Destruction",
    "Murder": "Murder",
    "Unknown": "Unknown"
}
visual_data['Event type'] = visual_data['Event type'].map(edit_name)

# Edit the time name to make it follow the same format
time_edit = {
    "night": "Night",
    "morning": "Morning",
    "afternoon": "Afternoon",
    "evening": "Evening",
    "Unknown": "Unknown"
}
visual_data['Time of Day'] = visual_data['Time of Day'].map(time_edit)

# Find all unique time and events
all_time = visual_data['Time of Day'].unique()
all_event = visual_data['Event type'].unique()

# Got all paired combinations
full_combo = pd.MultiIndex.from_product([all_time, all_event], names=["Time of Day", "Event type"]).to_frame(index=False)

# Group by 'Time of Day' and 'Event type', then count occurrences
stats = visual_data.groupby(['Time of Day', 'Event type']).size().reset_index(name='count')

# Merge the group by results with all possible paired combinations
final_df = pd.merge(full_combo, stats, on=["Time of Day", "Event type"], how="left")

# Fill missing counts with 0 and ensure integer type
final_df['count'] = final_df['count'].fillna(0).astype(int)

# Change the column title
final_df.columns = ['timeofday', 'typesofevent', 'count']

# Final dataset to tsv 
final_df.to_csv("../dataset_subsets/tsv_subsets/angel_viz.tsv", sep='\t', index=False)

print("Processing completed.")
