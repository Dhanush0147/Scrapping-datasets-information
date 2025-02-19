# 📊 Data Scraping  for Public Datasets to extract their information for analysis 

This project scrapes and analyzes public datasets from various platforms to provide insights into **available resources, descriptions, and popularity metrics**. The goal is to facilitate **data-driven decision-making** for researchers and professionals looking for curated datasets.

## 🌐 Websites Scraped
1. **[Data.gov](https://www.data.gov/)** - A comprehensive platform hosting datasets from U.S. government agencies across domains like healthcare, education, and environment.
2. **[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)** - A repository offering machine learning datasets frequently used in **academic research** and practical applications.

---

## 📌 Purpose of the Data
The goal of this project is to create a **centralized and structured collection** of metadata about publicly available datasets. By extracting key details such as **dataset names, organizations, descriptions, and popularity metrics**, users can quickly identify relevant datasets for their projects.

This data serves as a foundational resource for:
✅ **Researchers** exploring datasets for analysis.  
✅ **Educators** seeking real-world examples for teaching **data science** or **machine learning**.  
✅ **Policymakers & professionals** looking for insights from publicly available datasets.  

---

## 🎯 Relevance
- **Data.gov** datasets highlight key resources released by government agencies, ensuring **transparency and accessibility**.  
- **UCI Machine Learning Repository** datasets are widely used for benchmarking **machine learning models**, making them essential for **academic and industrial research**.

---

## 🔍 Key Findings
### **1️⃣ Data.gov**
- ✅ Extracted **dataset names, descriptions, associated organizations, and recent views** (for 2 pages).
- ✅ Identified datasets across **diverse topics** such as **public health** and **environmental studies**.

### **2️⃣ UCI Machine Learning Repository**
- ✅ Extracted **dataset titles, subject areas, descriptions, feature counts, and views** (for 2 pages).
- ✅ Focused on datasets with **well-defined attributes** for machine learning research.

---

## ⚙️ Technologies & Libraries Used
- **🦊 Selenium** – Automates browser navigation for dynamic content.  
- **🌐 BeautifulSoup** – Extracts structured data from web pages.  
- **📊 Pandas** – Handles data manipulation.  
- **🔥 JSON** – Saves structured dataset information.  

### Install dependencies:
```bash
pip install selenium beautifulsoup4 requests
