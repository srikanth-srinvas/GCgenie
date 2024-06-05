# GC Content Calculation and Visualization Tool

## Description
This Python tool calculates the GC content of DNA sequences from FASTA or FASTQ files and visualizes the results. It supports calculating GC content for each sequence or using a sliding window approach.

## Prerequisites
- Python 3.x
- Biopython
- Matplotlib

Install the necessary libraries using pip:
```bash
pip install biopython matplotlib
```

## Usage 
- Clone or download the project from GitHub.
- Navigate to the project directory.
- Install the required libraries using pip install -r requirements.txt.
- Run the tool using Python:

```bash
python main.py -i <path_to_fasta_or_fastq_file> [-w <window_size>] [-o <output_file>]
```
<path_to_fasta_or_fastq_file>: Path to the input FASTA or FASTQ file.
<window_size> (optional): Size of the sliding window for GC content calculation.
<output_file> (optional): Name of the output file for the plot (default: gc_content_plot.png).

## Examples
- Calculate GC content for each sequence in a FASTA file:

```bash
python main.py -i test_data/sample.fasta
```

- Calculate GC content using a sliding window of size 50:

```bash
python main.py -i test_data/sample.fasta -w 50
```

## Credits

- Biopython (https://biopython.org/)
- Matplotlib (https://matplotlib.org/)
