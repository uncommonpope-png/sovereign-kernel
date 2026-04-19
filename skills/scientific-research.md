# scientific-research

Access scientific literature, run bioinformatics tools, and reason over research data.

## What this skill does
Fetches papers from PubMed/arXiv, parses abstracts, runs bioinformatics pipelines, and provides evidence-based synthesis on scientific topics.

## PubMed search
```python
import httpx
def pubmed_search(query, max_results=5):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    search = httpx.get(f"{base}/esearch.fcgi?db=pubmed&term={query}&retmax={max_results}&retmode=json").json()
    ids = search["esearchresult"]["idlist"]
    summary = httpx.get(f"{base}/esummary.fcgi?db=pubmed&id={','.join(ids)}&retmode=json").json()
    return [(summary["result"][i]["title"], summary["result"][i]["pubdate"]) for i in ids]
```

## arXiv search
```python
import httpx, xml.etree.ElementTree as ET
def arxiv_search(query, max_results=5):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results={max_results}"
    r = httpx.get(url, timeout=15)
    root = ET.fromstring(r.text)
    ns = "{http://www.w3.org/2005/Atom}"
    return [(e.find(f"{ns}title").text.strip(), e.find(f"{ns}summary").text[:200].strip())
            for e in root.findall(f"{ns}entry")]
```

## Bioinformatics (BLAST query)
```bash
curl "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Put&PROGRAM=blastn&DATABASE=nt&QUERY=ATCGATCG&FORMAT_TYPE=JSON2"
```

## Statistical analysis
```python
import scipy.stats as stats
# t-test
t, p = stats.ttest_ind(group_a, group_b)
print(f"t={t:.3f}, p={p:.4f}, significant={'yes' if p<0.05 else 'no'}")
```

## Evidence synthesis
Rank sources by: peer-reviewed > preprint > review > blog. Store findings with importance 0.85.

## Example commands
```
ACTION: Search PubMed for "autonomous AI agents" and summarize the top 5 papers
ACTION: Find recent arXiv papers on PLT reinforcement learning and store abstracts in memory
```
