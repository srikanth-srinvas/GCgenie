# visualization.py

import matplotlib.pyplot as plt

def plot_gc_content(gc_contents, title="GC Content Across Sequences", output_file="gc_content_plot.png"):
    """
    Plot GC content as a bar chart.
    Args:
        gc_contents (list of float): List of GC content percentages
        title (str): Title of the plot
        output_file (str): Path to save the plot image
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(gc_contents)), gc_contents)
    plt.xlabel('Sequence Index')
    plt.ylabel('GC Content (%)')
    plt.title(title)
    plt.savefig(output_file)
    plt.show()

def plot_gc_content_sliding_window(gc_contents, window_size, title="GC Content Sliding Window", output_file="gc_content_window_plot.png"):
    """
    Plot GC content as a line plot for sliding windows.
    Args:
        gc_contents (list of list of float): List of GC content percentages for each window per sequence
        window_size (int): Size of the sliding window
        title (str): Title of the plot
        output_file (str): Path to save the plot image
    """
    plt.figure(figsize=(10, 6))
    for i, window_gc in enumerate(gc_contents):
        plt.plot(range(len(window_gc)), window_gc, label=f'Sequence {i+1}')
    plt.xlabel(f'Window Position (Window Size = {window_size})')
    plt.ylabel('GC Content (%)')
    plt.title(title)
    plt.legend()
    plt.savefig(output_file)
    plt.show()
