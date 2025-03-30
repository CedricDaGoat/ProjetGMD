🔬 GMD Project 2025 – Biomedical Data Integration System

This project was developed as part of the GMD (Data Management and Modeling) course. It consists of building a biomedical data integration system using Python and the Flask web framework.

The main objective is to allow a user to input one or more signs or symptoms in order to:

    retrieve diseases that could be causing them,

    identify drugs that may be used to treat them,

    or discover drugs that might cause them as side effects.

The system follows a mediator-based architecture, meaning the data remains in its original format and location. When a query is made, it is translated and sent to the various data sources. Results are then aggregated and presented to the user in a structured and readable format.

The application integrates multiple heterogeneous data sources (XML, CSV, SQLite, MySQL, OBO...), such as DrugBank, OMIM, SIDER, HPO, and STITCH/ATC, in order to cross-reference and unify information across symptoms, diseases, and medications.
🔧 Processing HPO and DrugBank Sources
🧬 HPO: Symptom Extraction

The HPO Annotations database, provided as a SQLite file, contained a single main table. To improve readability and integration, this table was exported as a CSV file named main_phenotype_annotation.csv.

A Python script was then developed to link these annotations with terms and synonyms found in the hpo.obo file. This file contains standardized symptom names as well as their synonyms. The script extracts and matches HPO IDs with readable labels, resulting in clean Python lists like: ["Nausea", "Cough", "Headache"].

This step ensures that users can query symptoms using different lexical variations, greatly improving both accuracy and coverage of search results.
💊 DrugBank: Indexing Drugs Related to Symptoms

The DrugBank data, provided in XML format, originally included indication and side effect information inside the Indication and Toxicity fields as free-text paragraphs. This made it difficult to directly access or search for symptoms, since one had to parse and interpret long unstructured strings.

To address this, a custom Python script (index_drugbank.py) was created to automatically parse and extract relevant data from the XML and store it in a simplified CSV file: drug_symptoms_relations.csv.

This file contains the following columns:

    drug_id

    drug_name

    treats: a list of symptoms or diseases the drug is intended to treat

    causes: a list of symptoms the drug may cause as side effects

This transformation enables the system to quickly and efficiently retrieve all drugs related to a given symptom, whether as a treatment or a possible cause.

Additionally, thanks to the integration of HPO synonyms, the new structured database drastically improves performance and response time, compared to direct XML parsing which was significantly slower for even small queries.