import pandas as pd
import os


def combine_evidence(row):
    audio = row["Audio Evidence"]
    visual = row["Image/Video/Visual Evidence"]
    if audio and visual:
        return "Both"
    elif audio:
        return "Audio Only"
    elif visual:
        return "Visual Only"
    else:
        return "None"


def bucket_witnesses(count):
    try:
        count = int(count)
    except:
        return "Unknown"  # Handle missing or invalid data
    if count == 0:
        return "0"
    elif count == 1:
        return "1"
    elif 2 <= count <= 5:
        return "2-5"
    elif 6 <= count <= 10:
        return "6-10"
    else:
        return "10+"


def filter_tsv_columns(input_tsv_path, output_tsv_path, required_columns):
    """
    Reads a TSV file, filters only the required columns, and saves the result as a new TSV.

    Parameters:
    - input_tsv_path (str): Path to the input TSV file.
    - output_tsv_path (str): Path to save the filtered TSV file.
    - required_columns (list): List of column names to keep.
    """
    try:
        # Read the TSV file
        df = pd.read_csv(input_tsv_path, sep="\t", low_memory=False)

        df["Combined_Evidence"] = df.apply(combine_evidence, axis=1)
        df["Witness_Count_Group"] = df["Haunted Places Witness Count"].apply(
            bucket_witnesses
        )

        # Check if all required columns exist
        missing_cols = [
            col for col in required_columns if col not in df.columns
        ]
        if missing_cols:
            print(
                f"Warning: These columns were not found in the TSV: {missing_cols}"
            )

        # Filter the columns
        filtered_df: pd.DataFrame = df[required_columns]

        # Save to new TSV
        filtered_df.to_csv(output_tsv_path, sep="\t", index=False)
        print(f"Filtered TSV saved to {output_tsv_path}")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
required_columns = [
    "Time of Day",
    "Event type",
    "Apparition Type",
    "Image/Video/Visual Evidence",
    "Audio Evidence",
    "state",
    "State% of High School Diploma",
    "State% of Bachelor's Degree",
    "State% of Advanced Degree",
    "Haunted Places Witness Count",
    "Combined_Evidence",
    "Witness_Count_Group",
    "QUANTITY",
    "TIME",
    "FAC",
    "ORG",
    "LOC",
    "EVENT",
]

original_tsv_path: os.path = os.path.abspath(
    "orginal_dataset/haunted_places_final_all_features.tsv"
)
dataset_subset_path: os.path = os.path.abspath(
    "dataset_subsets/filtered_dataset.tsv"
)

filter_tsv_columns(original_tsv_path, dataset_subset_path, required_columns)
