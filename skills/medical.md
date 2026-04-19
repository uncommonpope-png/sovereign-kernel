# medical

Clinical reasoning, diagnosis support, drug interaction checking, and evidence-based medicine.

## What this skill does
Provides medical AI capabilities: symptom analysis, drug interaction lookup, clinical guidelines retrieval, ICD-10 coding, and evidence synthesis from PubMed.

## ⚠️ Disclaimer
This skill is for information and research only. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

## Drug interaction check (OpenFDA)
```python
import httpx
def check_drug_interaction(drug1, drug2):
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{drug1}+AND+patient.drug.medicinalproduct:{drug2}&limit=3"
    r = httpx.get(url, timeout=10)
    if r.status_code == 200:
        results = r.json().get("results", [])
        return [r.get("patient",{}).get("reaction",[]) for r in results[:3]]
    return []
```

## ICD-10 code lookup
```python
def icd10_search(term):
    url = f"https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms={term}&maxList=5"
    r = httpx.get(url, timeout=10)
    codes = r.json()
    return list(zip(codes[1], codes[3])) if len(codes) > 3 else []
```

## Clinical reasoning template
```
Patient: [age, sex, chief complaint]
Symptoms: [list]
Vital signs: [if known]
Differential diagnosis (top 3):
1. [Most likely] — reasoning
2. [Less likely] — reasoning  
3. [Rule out] — reasoning
Recommended workup: [labs, imaging]
Red flags to watch: [list]
```

## PubMed clinical search
```python
# Search for clinical guidelines
results = pubmed_search("clinical guidelines " + condition, max_results=3)
```

## Example commands
```
ACTION: Look up drug interactions between metformin and ibuprofen using OpenFDA
ACTION: Search PubMed for clinical guidelines on hypertension management and summarize
```
