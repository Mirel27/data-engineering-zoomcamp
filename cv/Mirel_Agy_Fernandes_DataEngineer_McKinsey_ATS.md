# MIREL AGY FERNANDES

mirelagy27@gmail.com | +44 7867093713 | linkedin.com/in/mirel-agy-fernandes | London, United Kingdom

---

## PROFESSIONAL SUMMARY

Data Engineer with 5+ years of experience designing scalable data platforms and building distributed ETL/ELT pipelines using Apache Spark, Snowflake, Azure, and dbt. Proven expertise processing large-scale healthcare, financial, and technology datasets across cloud-native architectures (Azure, AWS, GCP). Skilled in data modeling (dimensional, star schema), automated data quality frameworks, and CI/CD-driven deployments using Docker and Azure DevOps. Experienced collaborating with data scientists, ML engineers, and cross-functional stakeholders to deliver high-performance, GDPR-compliant data infrastructure for analytics and machine learning at scale.

---

## TECHNICAL SKILLS

Languages and Scripting: Python, SQL, Scala, PySpark, Snowpark, T-SQL

Big Data and Processing: Apache Spark, PySpark, Databricks

Data Warehousing and Lakes: Snowflake, Azure Synapse, Delta Lake, ADLS Gen2

ETL and Orchestration: Azure Data Factory, dbt, Apache Airflow, Kestra, SSIS

Cloud Platforms: Microsoft Azure (ADLS Gen2, Databricks, Synapse, Key Vault, Azure ML)

Data Modeling: Dimensional Modeling, Star Schema, Snowflake Schema, Data Vault

Data Quality and Observability: dbt tests, Great Expectations, automated validation frameworks, anomaly detection, PII/GDPR compliance

Infrastructure and DevOps: Docker, Kubernetes, Terraform, Git, CI/CD, Azure DevOps

Analytics and BI: Power BI, SSRS, SSAS, Qlik

Methodologies: Agile, Scrum, Technical Documentation, Stakeholder Management, Communication

---

## PROFESSIONAL EXPERIENCE

### Data Engineer | Imperial College Healthcare NHS Trust / Imperial College London
**March 2024 – Present | London, United Kingdom**

- Designed and deployed scalable ETL/ELT pipelines to extract Electronic Health Record (EHR) data from 4 source systems (Cerner, Arya Radiology, Somerset Cancer, Nautilus BLOB) into Snowflake via Azure Data Factory, using Parquet staging on ADLS Gen2 and WITH(NOLOCK) query optimization, reducing full load duration to 7 days.
- Engineered a high-performance clinical notes anonymization pipeline using Apache Spark DataFrames, Snowflake Modin, and a BERT-based transformer model (MMIC-4 deidentification standard), achieving 99% PII masking accuracy and improving throughput from 10K records in 4 days to 1M records in 1 hour.
- Built an automated data validation framework using Snowpark that validates 180M records (20 columns) in 1 minute, achieving 100% PII leakage prevention with near-zero human intervention across daily, weekly, and monthly pipeline triggers.
- Developed data models for 3 research projects including maternity and fetal linkage models (98% accuracy), reducing query times by 25% through strategic cluster key implementation in Snowflake.
- Authored dbt transformation logic, test cases, and macros supporting both full and incremental loads, applying data quality checks and automated regression testing as part of the CI/CD pipeline.
- Built fail-safe incremental loading framework with restart capability, handling Snowflake 16MB record-length limits via dynamic free-text splitting and fault-tolerant monitoring.
- Leveraged Azure Machine Learning with GPT-4.0 API to extract insights from Snowflake data for automated discharge summary generation, measuring completeness, accuracy, readability, and bias of clinical narratives.
- Developed end-to-end monitoring, logging, and alerting dashboards to provide transparency into pipeline health and ensure consistent, reliable pipeline execution.
- Collaborated effectively with a diverse cross-functional team including clinical researchers, clinicians, data scientists, data protection officers, ethics committees, and funders, ensuring development complied with GDPR, HIPAA, and legal guidelines.
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

- Led Legacy System-to-Cloud migration projects using Azure Data Factory, automating batch files, optimizing Scala jobs, and rewriting Python code for Azure Databricks, delivering a 40% reduction in ETL processing time for historical and incremental pipelines in Azure Synapse.
- Built Bronze layer ingestion pipelines in Azure Databricks to capture raw source data from legacy systems into ADLS Gen2 with schema enforcement and incremental loading strategies.
- Optimized 15 SQL stored procedures and functions and restructured 215+ database tables, reducing process time by an additional 20%.
- Designed data ingestion, transformation, and reporting frameworks using SSAS and SSIS, mapping source data to the Azure Synapse data warehouse.
- Developed interactive dashboards using Power BI and SSRS to analyze product performance and support business decision-making.
- Led an Agile team of 4 engineers, conducting sprint planning, stand-ups, and iterative development using Azure DevOps to ensure meticulous tracking of priorities and deliverables.
- Authored LEX Platform Documentation for Azure best practices and developed historical/incremental load framework documentation.
- Consistently rated 4.5/5 in appraisal cycles; earned High Performer Award for outstanding dedication and measurable improvements in data migration efficiency.

**Technologies used:** PySpark, Scala, Azure Databricks, Azure Data Factory, Azure Synapse, Azure Blob Storage Gen2, Azure DevOps, Azure Key Vault, Snowflake, MySQL, SSMS, SSRS, SSIS, SSAS, Python, SQL, Power BI

---

## PROJECTS

### Data Engineering Zoomcamp | Self-Directed Professional Development
**2025 – 2026 | GitHub: github.com/Mirel27/data-engineering-zoomcamp**

Completed hands-on modules covering the modern data engineering stack, directly applicable to QuantumBlack/McKinsey data infrastructure:

- **Containerization (Docker):** Built and deployed containerized data pipeline services using Docker and Docker Compose, enabling reproducible environments across development, staging, and production.
- **Workflow Orchestration (Kestra / Airflow):** Designed and scheduled batch and streaming data workflows using Kestra and Apache Airflow, applying DAG-based orchestration patterns for reliable pipeline execution.
- **Data Warehousing (BigQuery / GCP):** Implemented data warehouse solutions on Google BigQuery (GCP), applying partitioning, clustering, and cost optimization strategies for large-scale analytical queries.
- **Batch Processing (Apache Spark):** Developed distributed batch processing jobs using Apache Spark and PySpark, transforming and aggregating multi-million-record datasets.
- **Streaming (Apache Kafka):** Built real-time streaming data pipelines using Apache Kafka, implementing producer/consumer patterns for event-driven data ingestion.
- **Infrastructure as Code (Terraform / GCP):** Provisioned and managed cloud infrastructure on GCP using Terraform, automating resource creation and teardown for reproducible data environments.
- **Analytics Engineering (dbt):** Applied dbt for data transformation, testing, and documentation, implementing dimensional models and data quality checks on top of BigQuery.

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

## LANGUAGES

- English: Fluent / Professional
