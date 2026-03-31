# CV Review & Analysis
## Mirel Agy Fernandes — Data Engineering, QuantumBlack, AI by McKinsey

---

## Overall ATS Score: **68 / 100**

### Recruiter Reach Likelihood: **BORDERLINE — ~60–70% chance of passing ATS**

You have a genuinely strong tech stack and real quantified achievements. The main risks are:
- Missing high-priority keywords that QuantumBlack's ATS specifically scans for (`Docker`, `Airflow`, `Kafka`, `feature engineering`, `data lakehouse`)
- A typo that signals lack of attention to detail — a critical soft skill listed in the JD
- A poorly aligned Professional Summary that doesn't mirror the JD language
- The GTA role consumes space without adding value for this application

After the recommended fixes, the estimated ATS pass rate rises to **~80–85%**.

---

## Keyword Gap Analysis

### Keywords Present ✅
| Keyword | Found In |
|---------|----------|
| Python | Skills section, Infosys role |
| SQL / T-SQL | Skills section |
| Spark / PySpark / Snowpark | Skills section, NHS role |
| Snowflake | Skills section, NHS role |
| Azure (ADLS Gen2, Synapse, Databricks) | Skills, both roles |
| dbt | Skills section, NHS role |
| Azure Data Factory | Skills, NHS role, Infosys role |
| CI/CD | Skills section |
| Git / Azure DevOps | Skills section |
| Agile | Skills section, Infosys role |
| Databricks | Skills section, Infosys role |
| ETL / ELT | Summary, NHS role |
| Data Quality / Anomaly Detection | Skills section, NHS role |
| GDPR | Summary, NHS role |
| ML / LLM / BERT / GPT-4 | NHS role |
| Scala | Skills section, Infosys role |
| Dimensional Modeling / Star Schema | Skills section |

### Keywords Missing or Under-Represented ❌
| Missing Keyword | Priority | Recommended Action |
|-----------------|----------|--------------------|
| `Docker` | 🔴 Critical | Add to Skills; mention containerised deployment in at least one bullet |
| `Kubernetes` | 🟡 High | Add if any exposure exists |
| `Apache Airflow` | 🔴 Critical | Map ADF orchestration experience to Airflow concepts or mention as equivalent |
| `Kafka` / streaming / event-driven | 🟡 High | Add if any exposure exists; or mention familiarity |
| `data lakehouse` | 🟡 High | You use ADLS Gen2 — explicitly call this a "lakehouse architecture" |
| `feature engineering` / `feature pipeline` | 🟡 High | Your GPT-4/BERT work qualifies — use this language |
| `ML pipeline` / `ML-ready data infrastructure` | 🔴 Critical | QuantumBlack is AI-first; this phrase must appear |
| `reproducible pipelines` / `modular pipelines` | 🟡 High | McKinsey-specific language |
| `GCP` (Google Cloud Platform) | 🟡 High | If any exposure exists, add it |
| `Terraform` / `Infrastructure as Code` | 🟢 Medium | Add if applicable |
| `data governance` | 🟢 Medium | You have GDPR compliance work — use this term explicitly |
| `client-facing` / `client impact` | 🟡 High | Infosys work was Fortune 500 client delivery — highlight this |

---

## Section-by-Section Grading

### 1. Professional Summary — **C+ (65/100)**

**Strengths:** Mentions core stack (Spark, Snowflake, Azure, dbt), quantifies years of experience, references healthcare/finance domain.

**Weaknesses:**
- Does not mirror QuantumBlack JD language at all
- No mention of ML-ready data infrastructure, client impact, or cross-functional collaboration
- Misses opportunity to mention Docker, which the candidate does know
- "Passionate about building reliable, high-performance data infrastructure" is generic

**Fix:** Rewrite to explicitly reference ML pipeline support, client impact, and cross-functional Agile delivery.

---

### 2. Technical Skills Section — **B (78/100)**

**Strengths:** Well-structured, comprehensive, covers most of the required stack.

**Weaknesses:**
- Docker is completely absent (candidate confirmed they are familiar)
- Airflow, Kafka, GCP missing
- No mention of data lakehouse architectures
- AWS is listed but no specific services mentioned (S3, Glue, Redshift, etc.)

**Fix:** Add Docker under Containers. Add Airflow/Kafka under ETL/Orchestration. Expand AWS entry.

---

### 3. Work Experience — Imperial College Healthcare NHS Trust — **A- (88/100)**

**Strengths:** Excellent quantified achievements (99% PII masking, 1M records/1 hour, 180M records/1 min, 25% query reduction). Demonstrates enterprise-scale, ML adjacency (BERT, GPT-4, Snowflake Cortex), GDPR compliance, cross-functional collaboration.

**Weaknesses:**
- **Typo: "spark DataFrames DataFrames"** — duplicate word, must be fixed immediately
- **Broken phrase: "Snowflake modin. pandas"** — sentence structure is broken
- ML work is described in engineering terms but never uses "ML pipeline", "feature engineering", or "ML-ready infrastructure" — critical for QuantumBlack
- "Build" instead of "Built" (tense error) in one bullet
- Does not use the word "lakehouse" despite using lakehouse architecture

**Fix:** Fix typos and tense. Reframe GPT-4/BERT work using ML pipeline language. Add "lakehouse architecture" to ADLS Gen2 description.

---

### 4. Work Experience — GTA, University of Sheffield — **D (35/100)**

**Strengths:** Shows communication and teaching ability.

**Weaknesses:**
- Entirely irrelevant to a senior Data Engineering role
- SPSS is not a recognised tool in the QuantumBlack stack
- 6-month role with no engineering output takes space that could be used for technical achievements
- ATS may penalise the appearance of a "gap" or "career pivot" signal

**Fix:** Compress to 1–2 lines maximum or remove entirely. Use the freed space for a Projects section or more detail on the Infosys role.

---

### 5. Work Experience — Infosys Limited — **B (77/100)**

**Strengths:** Fortune 500 clients (MetLife, Citi, Apple), quantified impact (40% ETL reduction, 20% process time decrease, 15 optimised stored procedures), tech stack overlap is strong.

**Weaknesses:**
- The Fortune 500 client angle is buried in the middle of the role description — McKinsey is a consulting firm and values this heavily
- "Build" instead of "Built" (tense error) in two bullets
- Does not use "lakehouse" or "data lakehouse" language despite Medallion architecture (Bronze layer ingestion)
- Power BI and SSRS are listed but weak signals for this role — deprioritise
- "Consistently rated 4.5/5" is valuable but phrased passively — make it an achievement

**Fix:** Open the role with a client-impact sentence leading with MetLife, Citi, Apple. Fix tense. Reframe Bronze layer as Medallion/lakehouse architecture.

---

### 6. Education — **B+ (80/100)**

**Strengths:** MSc Data Science from University of Sheffield is well-regarded and directly relevant. BE in Electronic and Telecommunication provides a technical foundation.

**Weaknesses:**
- Education is placed at the bottom of the CV — McKinsey is pedigree-conscious, the MSc should be more prominent
- No dissertation or relevant modules mentioned — an opportunity to add relevant keywords (ML, big data, distributed systems)

**Fix:** Move Education above Work Experience, or at minimum ensure the MSc title is clearly prominent.

---

### 7. Certifications — **A (92/100)**

**Strengths:** Excellent and directly relevant. Snowflake Data Engineer + dbt Fundamentals + Azure Data Engineer Associate is exactly the stack QuantumBlack uses. HPC Driving Licence is a unique differentiator.

**Weaknesses:** No AWS or GCP certification despite listing AWS in skills.

**Fix:** No major changes needed. Consider adding an AWS or GCP cert if pursuing one.

---

## Formatting Issues

| Issue | Severity | Impact |
|-------|----------|--------|
| Multi-font PDF (Times New Roman, Symbol, Arial, Calibri) | Medium | ATS parsers may misread sections |
| Multi-column or table layout (suspected) | High | Workday ATS (used by McKinsey) fails on column layouts |
| Duplicate word: "DataFrames DataFrames" | Critical | Signals poor attention to detail |
| Broken sentence: "modin. pandas" | High | Signals poor proofreading |
| "Build" instead of "Built" (x3 occurrences) | Medium | Tense inconsistency signals carelessness |
| LinkedIn URL rendering issue in PDF | Low | May break hyperlink parsing |

---

## Top 5 Critical Changes Needed

### 1. 🔴 Fix the Typos Immediately
- `"spark DataFrames DataFrames"` → `"Spark DataFrames"`
- `"Snowflake modin. pandas"` → remove or rewrite clearly
- `"Build a historical"` → `"Built a historical"` (and all similar instances)

These errors appear in your **best role** and are the first thing a McKinsey recruiter will notice. Attention to detail is explicitly listed in the JD.

### 2. 🔴 Add Docker to Skills + One Experience Bullet
QuantumBlack explicitly requires container knowledge. The candidate confirmed Docker familiarity. Add:
- `Docker` under a new "Containers" line in Technical Skills
- One bullet in the NHS or Infosys role: *"Containerised data pipeline services using Docker for reproducible deployment across environments"*

### 3. 🔴 Rewrite the Professional Summary to Mirror QuantumBlack JD
Current summary is generic. New summary must include: `ML-ready data infrastructure`, `cross-functional Agile teams`, `client impact`, `scalable pipelines`, and mirror QuantumBlack's own language.

### 4. 🔴 Add Missing Critical Keywords
Add to Skills or experience bullets: `Airflow` (or `Apache Airflow`), `data lakehouse`, `ML pipeline`, `feature engineering`. These are either present in the candidate's experience or directly mappable.

### 5. 🟡 Restructure for Maximum Impact
- Remove or condense the GTA role to 1 line
- Lead the Infosys role with the Fortune 500 client angle
- Move Education higher (after Summary, before Experience) or make the MSc more prominent
- Ensure single-column, ATS-safe PDF format before submission

---

## Revised Estimated Scores After Fixes

| Category | Before | After Fixes |
|----------|--------|-------------|
| ATS Compatibility | 55/100 | 82/100 |
| Keyword Alignment | 60/100 | 85/100 |
| Formatting & Readability | 65/100 | 88/100 |
| Quantified Impact | 82/100 | 88/100 |
| Tailoring to Role | 45/100 | 80/100 |
| **Overall** | **68/100** | **85/100** |
