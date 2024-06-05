# main.py

import argparse
from gc_content import parse_sequences, calculate_gc_content, gc_content_sliding_window
from visualization import plot_gc_content, plot_gc_content_sliding_window

def main():
    parser = argparse.ArgumentParser(description="GCgenie - A GC Content Calculation and Visualization Tool")
    parser.add_argument("-i", "--input", required=True, help="Path to the input FASTA or FASTQ file")
    parser.add_argument("-w", "--window", type=int, default=None, help="Size of the sliding window")
    parser.add_argument("-o", "--output", default="gc_content_plot.png", help="Output file name for the plot")

    args = parser.parse_args()

    sequences = parse_sequences(args.input)
    if args.window:
        gc_contents = [gc_content_sliding_window(seq, args.window) for seq in sequences]
        plot_gc_content_sliding_window(gc_contents, args.window, output_file=args.output)
    else:
        gc_contents = [calculate_gc_content(seq) for seq in sequences]
        plot_gc_content(gc_contents, output_file=args.output)

if __name__ == "__main__":
    main()
