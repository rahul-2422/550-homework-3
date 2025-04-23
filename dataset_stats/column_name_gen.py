import pandas as pd
import os


def extract_column_names(input_tsv_path, output_csv_path):
    """
    Reads a TSV file and writes all column names into a CSV file,
    with each column name in a separate row.

    Parameters:
    - input_tsv_path (str): Path to the input TSV file.
    - output_csv_path (str): Path to save the output CSV file.
    """
    try:
        # Read only the header of the TSV
        df = pd.read_csv(input_tsv_path, sep="\t", nrows=0)

        # Get column names as a DataFrame
        columns_df = pd.DataFrame(df.columns, columns=["Column Names"])

        # Save to CSV
        columns_df.to_csv(output_csv_path, index=False)
        print(f"Column names saved to {output_csv_path}")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
original_tsv_path: os.path = os.path.abspath(
    "orginal_dataset/haunted_places_final_all_features.tsv"
)
dataset_subset_path: os.path = os.path.abspath(
    "dataset_subsets/filtered_dataset.tsv"
)
dataset_stats_path: os.path = os.path.abspath(
    "dataset_stats/filtered_dataset_columns.csv"
)
extract_column_names(dataset_subset_path, dataset_stats_path)
