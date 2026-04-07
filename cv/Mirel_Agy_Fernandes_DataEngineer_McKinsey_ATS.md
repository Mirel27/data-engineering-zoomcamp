# MIREL AGY FERNANDES

mirelagy27@gmail.com | +44 7867093713 | linkedin.com/in/mirel-agy-fernandes | github.com/Mirel27 | London, United Kingdom

---

## PROFESSIONAL SUMMARY

Data Engineer with 5+ years of experience designing scalable data platforms and building distributed ETL/ELT pipelines using Apache Spark, Snowflake, Azure, and dbt. Proven expertise processing large-scale datasets, building analytical models, and delivering data solutions for research, enterprise, and public sector environments.

---

## TECHNICAL SKILLS

Languages and Scripting: Python, SQL, Scala, PySpark, Snowpark, T-SQL, R

Big Data and Processing: Apache Spark, PySpark, Databricks, MapReduce

Data Warehousing and Lakes: Snowflake, Azure Synapse, Delta Lake, ADLS Gen2

ETL and Orchestration: Azure Data Factory, dbt, Apache Airflow, Kestra, SSIS

Cloud Platforms: Microsoft Azure (ADLS Gen2, Databricks, Synapse, Key Vault, Azure ML)

Data Modeling: Dimensional Modeling, Star Schema, Snowflake Schema, Data Vault

Data Quality and Observability: dbt tests, Great Expectations, automated validation frameworks, anomaly detection, PII/GDPR compliance

Infrastructure and DevOps: Docker, Kubernetes, Terraform, Git, CI/CD, Azure DevOps

Analytics and BI: Power BI, SSRS, SSAS, Qlik, Matplotlib

NLP and Data Science Libraries: pandas, spaCy, NLTK, NumPy, TensorFlow, BERT, SHAP

Machine Learning: Binary Classification, Feature Engineering, Multivariate Regression, Model Interpretability

Methodologies: Agile, Scrum, Technical Documentation, Stakeholder Management, Communication

---

## PROFESSIONAL EXPERIENCE

### Data Engineer | Imperial College Healthcare NHS Trust / Imperial College London
**March 2024 – Present | London, United Kingdom**

- Designed and deployed scalable ETL/ELT pipelines to extract Electronic Health Record (EHR) data from 4 source systems (Cerner, Arya Radiology, Somerset Cancer, Nautilus BLOB) into Snowflake via Azure Data Factory, processing 180M+ records with full audit logging and GDPR compliance.
- Engineered a high-performance clinical notes anonymization pipeline using Apache Spark DataFrames, Snowflake Modin, and a BERT-based transformer model (MMIC-4 deidentification standard), achieving industry-leading PII detection and redaction at scale.
- Built an automated data validation framework using Snowpark that validates 180M records (20 columns) in 1 minute, achieving 100% PII leakage prevention with near-zero human intervention across data processing workflows.
- Developed data models for 3 research projects including maternity and fetal linkage models (98% accuracy), reducing query times by 25% through strategic cluster key implementation in Snowflake.
- Authored dbt transformation logic, test cases, and macros supporting both full and incremental loads, applying data quality checks and automated regression testing as part of the CI/CD pipeline.
- Built fail-safe incremental loading framework with restart capability, handling Snowflake 16MB record-length limits via dynamic free-text splitting and fault-tolerant monitoring.
- Leveraged Azure Machine Learning with GPT-4.0 API to extract insights from Snowflake data for automated discharge summary generation, measuring completeness, accuracy, readability, and bias of clinical content.
- Developed analytical models using pandas, spaCy, NLTK, and NumPy, including incremental models that serve as the basis for Qlik and Matplotlib visualisations delivered to clients for data verification and validation.
- Developed end-to-end monitoring, logging, and alerting dashboards to provide transparency into pipeline health and ensure consistent, reliable pipeline execution.
- Collaborated effectively with a diverse cross-functional team including clinical researchers, clinicians, data scientists, data protection officers, ethics committees, and funders, ensuring delivery of trusted, research-ready datasets.
- Managed code deployments and project priorities using Azure DevOps with CI/CD pipelines, applying Agile sprint methodology throughout.

**Key Project Highlights:**
- Enriched structured fields by extracting data points from free-text using Snowflake Cortex, increasing structured field population from 60% to 90%.
- Implemented rule-based and ML-based data quality automation, enabling researchers to access validated, de-identified clinical datasets in a safe data environment.

---

### Graduate Teaching Assistant (GTA) — Management Research (Quantitative Analysis)
**The University of Sheffield | March 2023 – September 2023 | Sheffield, United Kingdom**

- Provided expertise in statistical analysis (SPSS) to support 154 postgraduate students across MSc Management and MSc Management (International Business) programs.
- Conducted data cleaning, manipulation, and analysis to enhance accuracy and derive meaningful insights from research datasets.
- Led lab sessions on data analysis and delivered personal tutoring to 20 students, ensuring clarity on technical statistical concepts.
- Collaborated with the module coordinator to plan sessions, track student progress, and provide structured feedback on performance.

---

### Senior System Developer / Azure Data Engineer | Infosys Limited
**November 2019 – April 2022 | Bangalore, India**

Delivered developer support across multiple projects for international clients in Insurance (MetLife Inc.), Finance (Citi), and Technology (Apple Inc.) sectors.

- Led Legacy System-to-Cloud migration projects using Azure Data Factory, automating batch files, optimizing Scala jobs, and rewriting Python code for Azure Databricks, delivering a 40% reduction in processing time.
- Built Bronze layer ingestion pipelines in Azure Databricks to capture raw source data from legacy systems into ADLS Gen2 with schema enforcement and incremental loading strategies.
- Optimized 15 SQL stored procedures and functions and restructured 215+ database tables, reducing process time by an additional 20%.
- Designed data ingestion, transformation, and reporting frameworks using SSAS and SSIS, mapping source data to the Azure Synapse data warehouse.
- Developed interactive dashboards using Power BI and SSRS to analyze product performance and support business decision-making.
- Led an Agile team of 4 engineers, conducting sprint planning, stand-ups, and iterative development using Azure DevOps to ensure meticulous tracking of priorities and deliverables.
- Authored LEX Platform Documentation for Azure best practices and developed historical/incremental load framework documentation.
- Consistently rated 4.5/5 in appraisal cycles; earned High Performer Award for outstanding dedication and measurable improvements in data migration efficiency.

**Technologies used:** PySpark, Scala, Azure Databricks, Azure Data Factory, Azure Synapse, Azure Blob Storage Gen2, Azure DevOps, Azure Key Vault, Snowflake, MySQL, SSMS, SSRS, SSIS, SSAS, Python, Power BI

---

## PROJECTS

### End-to-End Data Engineering Portfolio | Self-Directed Professional Development
**2025 – 2026 | GitHub: github.com/Mirel27/data-engineering-zoomcamp**

Architected and delivered end-to-end data pipeline solutions spanning containerization (Docker), workflow orchestration (Kestra/Airflow), cloud data warehousing (BigQuery/GCP), batch processing (Apache Spark/dbt), and streaming (Kafka/Flink), demonstrating production-grade data engineering capabilities.

---

### NLP Classification Pipeline: Mining Text vs Speech for Depression Diagnosis | MSc Research Project
**May 2023 – Sep 2023 | University of Sheffield | GitHub: github.com/Mirel27/Mining-Text-Versus-Speech-Exploring-Classification-Models-for-Depression-Diagnosis**

- Designed and implemented a scalable data pipeline integrating YouTube Data API, Selenium, and BeautifulSoup for automated retrieval of mental health vlogs using keyword filters, with ephemeral storage and automatic data deletion to ensure GDPR and ethics compliance.
- Developed automated scraping scripts with robust logging and error handling; applied rule-based text cleaning algorithms to preprocess highly unstructured YouTube vlog transcripts.
- Utilised Python in Databricks to fine-tune pretrained transformer models (BERT, MentalBERT, MentalRoBERTa, ClimateBERT) on multimodal datasets from Reddit and YouTube using TensorFlow.
- Achieved F1 score of 0.967 on Reddit data (MentalRoBERTa); conducted SHAP interpretability analysis to identify domain-specific vocabulary shifts between written and spoken language datasets.

**Technologies:** Python, Databricks, TensorFlow, BERT, SHAP, YouTube Data API, Selenium, BeautifulSoup, NLP

---

### Big Data: Exploring Job-Technology Skill Relationships | MSc Academic Project
**Feb 2023 – Jun 2023 | University of Sheffield | GitHub: github.com/Mirel27/Big-Data-Exploring-Job-Technology-Skill-Relationships**

- Integrated data from multiple sources (CSV and O*NET) using Databricks to analyse relationships between job descriptions and in-demand technological skills.
- Utilised DataFrames, RDD, SQL, and MapReduce in Databricks for scalable data processing and analysis.
- Performed data manipulation and skill pattern analysis to identify trends and correlations across job market datasets.

**Technologies:** Python, Databricks, Spark DataFrames, RDD, SQL, MapReduce

---

### COVID-19 Lockdown Impact on Insomnia and Anxiety Levels in the UK | MSc Academic Project
**Sep 2022 – Jan 2023 | University of Sheffield | GitHub: github.com/Mirel27/COVID19-UK-Insomnia-Anxiety-Impact-Analysis**

- Extracted and cleaned data from multiple sources (Our World in Data COVID-19 dataset, Mental Health Search Terms dataset) using R, handling missing values, type conversion, and normalisation.
- Applied feature selection techniques (correlation and variance analysis) and performed multivariate regression to explore the relationship between COVID-19 lockdown measures and insomnia/anxiety levels.

**Technologies:** R, Feature Engineering, Data Wrangling, Multivariate Regression

---

## EDUCATION

**Master of Science (MSc) — Data Science**
The University of Sheffield | Sheffield, United Kingdom | 2022 – 2023

**Bachelor of Engineering (B.E.) — Electronic and Telecommunication Engineering**
Goa University | Goa, India | 2015 – 2019

---

## CERTIFICATIONS

- Snowflake Data Engineer — Snowflake | 2025
- dbt Fundamentals — dbt Labs (Data Build Tool) | 2025
- Azure Data Engineer Associate (DP-203) — Microsoft | 2023
- Azure AI Fundamentals (AI-900) — Microsoft | 2023
- High-Performance Computing (HPC) Driving License — University of Sheffield | 2023

---

## ACHIEVEMENTS

- Secured 2nd place at the GitHub Copilot Hack Tour, collaborating with a cross-functional team to design and build an impactful data profiling proof-of-concept using GitHub Copilot.

---

## LANGUAGES

- English: Fluent / Professional