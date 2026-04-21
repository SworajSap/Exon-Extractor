from Bio import Entrez, SeqIO
import os

def download_and_clean_ng_record():
    # --- INTERACTIVE INPUTS ---
    print("--- NCBI NG Exon Downloader ---")
    email = input("Enter your email (required by NCBI): ").strip()
    gene_name = input("Enter the Gene Symbol (e.g., MECP2, HTT): ").strip().upper()
    save_path = input("Enter save directory (press Enter for current folder): ").strip()

    if not save_path:
        save_path = "."
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    Entrez.email = email
    
    # 1. Search for the NG record
    search_term = f"{gene_name}[Gene Name] AND RefSeqGene[Filter]"
    print(f"\nSearching NCBI for the Genomic (NG) record of {gene_name}...")
    
    try:
        search_handle = Entrez.esearch(db="nucleotide", term=search_term)
        search_results = Entrez.read(search_handle)
        search_handle.close()
        
        id_list = search_results.get("IdList")
        if not id_list:
            print(f"Error: No NG records found for '{gene_name}'.")
            return

        target_id = id_list[0]
        
        # 2. Fetch the record
        print(f"Found ID {target_id}. Fetching GenBank data...")
        fetch_handle = Entrez.efetch(db="nucleotide", id=target_id, rettype="gb", retmode="text")
        
        # 3. Parse and Filter
        record = SeqIO.read(fetch_handle, "genbank")
        fetch_handle.close()

        # Keep only 'exon' and 'source' features
        original_feature_count = len(record.features)
        record.features = [f for f in record.features if f.type in ["exon", "source"]]
        
        # 4. Save
        filename = f"{gene_name}_NG_Exons.gb"
        full_path = os.path.join(save_path, filename)
        
        with open(full_path, "w") as output_file:
            SeqIO.write(record, output_file, "genbank")
            
        print("-" * 30)
        print(f"SUCCESS!")
        print(f"Gene: {gene_name}")
        print(f"Features removed: {original_feature_count - len(record.features)}")
        print(f"File saved to: {os.path.abspath(full_path)}")
        print("-" * 30)

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    download_and_clean_ng_record()