# Exon-Extractor
Python utility to search NCBI for NG records and extract exon-only-annotated GenBank files.

## Features
- **Interactive CLI:** Prompts for user email and gene symbol.
- **Specific Filtering:** Automatically removes introns, variations, and miscellaneous features, keeping only 'exon' and 'source' tags.
- **NG-RefSeq Validation:** Uses NCBI search filters to ensure genomic sequences are prioritized over mRNA transcripts.

## Prerequisites
- Python 3.x
- Biopython

- ## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/SworajSap/Exon-Extractor.git](https://github.com/SworajSap/Exon-Extractor.git)
   cd Exon-Extractor
