## Haunted Places: Building D3 Visuals and Using Applications for Fast Data Exploration
### Team Members:
Evan Hu, Chuqi (Angel) Jin, Aditya Venkat, Rohit Patil, Rahul Katinni, Quynh Tran

### Introduction

Building upon our previous work from the first two assignments, this project aims to show off the work we've done by creating D3 visualizations. We also deployed Apache Solr, MEMEX Image Space, and MEMEX GeoParser to further explore the dataset and its features. 

### Contributions:

D3 Visualizations (https://rahul-2422.github.io/550-homework-3/):

* Force Directed Graph: Quynh
* Heatmap: Angel
* Sankey Diagram: Rahul
* Geo Distribution (Choropleth and Bubble Map): Evan
* NER Word Cloud: Rohit
* Front End for D3 visuals: Aditya

Apache Solr
* Led by Angel, other members helped

Image Space
* Led by Aditya, other members helped

MEMEX GeoParser
* Led by Evan, other members helped

### Additional Submission Files

The following files are included in the root directory of this repository as part of the assignment submission requirements:

- **`Apache_Solr_Queries.pdf`**  
  Documents sample Solr queries used to explore the indexed Haunted Places data and validate ingestion. These include keyword-based searches and field-based filters relevant to the TSV dataset.

- **`MEMEX GeoParser Screenshots.pdf`**  
  Shows example outputs of running the MEMEX GeoParser on location-based fields from the Haunted Places dataset. Screenshots demonstrate extracted entities and geolocation visualizations, addressing Task 5.

- **`imagespace_submission.tar.gz`**  
  Contains the exported Solr and ImageCat index directories (`solr_index` and `imagecat_index`) from the deployed Image Space system. These were generated after successful ingestion and indexing of a subset of the Haunted Places dataset using SMQTK and the ImageCat pipeline, as initally requested by Task 4c.

