import argparse
import csv
import os
from datetime import datetime
from Bio import Entrez, SeqIO

# Configure Entrez email
Entrez.email = "agershkoviz@gmail.com"

# Search the NCBI database and return the result count and IDs
def search_ncbi(database, term, number):
    handle = Entrez.esearch(db=database, term=term, idtype="acc", retmax=number)
    record = Entrez.read(handle)
    handle.close()
    return int(record["Count"]), record["IdList"]

# Download a record from NCBI and save it to a file
def download_ncbi_record(database, doc_id, output_dir):
    handle = Entrez.efetch(db=database, id=doc_id, rettype="gb", retmode="text")
    data = handle.read()
    handle.close()
    
    filename = os.path.join(output_dir, f"{doc_id}.gb")
    with open(filename, 'w') as file:
        file.write(data)
    return filename

# Log metadata to a CSV file
def log_to_csv(log_file, date, term, database, max_records, total_found):
    """Log metadata to a CSV file."""
    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, term, max_records, total_found])

def main():
    try:
        parser = argparse.ArgumentParser(description="Download data from NCBI.")
        parser.add_argument("--database", type=str, default="nucleotide", help="NCBI database to query (default: nucleotide)")
        parser.add_argument("--term", type=str, required=True, help="Search term")
        parser.add_argument("--number", type=int, default=10, help="Number of records to download (default: 10)")
        args = parser.parse_args()

        # Create output directory
        output_dir = "ncbi files & log"
        os.makedirs(output_dir, exist_ok=True)

        # Perform search
        total_found, id_list = search_ncbi(args.database, args.term, args.number)
        
        # Download records
        for doc_id in id_list:
            filename = download_ncbi_record(args.database, doc_id, output_dir)

        # Log metadata
        log_file = os.path.join(output_dir, "log.csv")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_to_csv(log_file, timestamp, args.term, args.database, args.number, total_found)

        # Print CSV-style output to command line
        print("date,database,term,max,total")  
        print(f"{timestamp},{args.database},{args.term},{args.number},{total_found}")

if __name__ == "__main__":
    main()
