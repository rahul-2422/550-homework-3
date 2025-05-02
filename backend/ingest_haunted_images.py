import os
from imagecat import ingest
from imagecat.extractors.colorhistogram import ColorHistogramExtractor

image_folder = '/Users/adityavenkat/homework-2/data/generated_images'

extractor = ColorHistogramExtractor()
es_url = 'http://localhost:9200'
index_name = 'haunted_places_index'

ingestor = ingest.ImageIngestor(
    extractor=extractor,
    es_url=es_url,
    index_name=index_name
)

for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(image_folder, filename)
        try:
            ingestor.ingest(file_path)
            print(f"[+] Ingested {filename}")
        except Exception as e:
            print(f"[!] Error with {filename}: {e}")
