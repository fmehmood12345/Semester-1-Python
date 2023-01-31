from random import choice
import sys
import os
import time
import argparse
from progress import Progress
from collections import defaultdict


# Returns some python object that contains the graph data
def load_graph(args):
    """Load graph from text file
    Parameters:
    args -- arguments named tuple
    Returns:
    A dict mapling a URL (str) to a list of target URLs (str).
    """
    graph = defaultdict(list)
    # Iterate through the file line by line
    for line in args.datafile:
        # And split each line into two URLs
        (node, target) = line.split()
        graph[node].append(target)
    return graph


def print_stats(graph):
    """Print number of nodes and edges in the given graph"""
    number_of_edges = 0
    print(f"The number of nodes in the graph are: {len(graph)}")
    for node, target in graph.items():
        number_of_edges += len([item for item in target if target])
    print(f"The number of edges in the graph are: {number_of_edges}")


# Estimate PageRanks via random walkers
# Estimate PageRanks via random walkers
def stochastic_page_rank(graph, args):
    """Stochastic PageRank estimation
    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple
    Returns:
    A dict that assigns each page its hit frequency
    This function estimates the Page Rank by counting how frequently
    a random walk that starts on a random node will after n_steps end
    on each node of the given graph.
    """
    hit_count = {}
    repeat_count = 1 / args.repeats
    key_list = list(graph.keys())
    graphs_keys = graph.keys()

    for x in graphs_keys:
        hit_count[x] = 0.0
    for node in range(args.repeats):
        current_node = choice(key_list)
        for x in range(args.steps):
            current_node = choice(graph[current_node])
        hit_count[current_node] += repeat_count

    return hit_count


# Estimate PageRanks via probability distributions
def distribution_page_rank(graph, args):
    """Probabilistic PageRank estimation
    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple
    Returns:
    A dict that assigns each page its probability to be reached
    This function estimates the Page Rank by iteratively calculating
    the probability that a random walker is currently on any node.
    """
    node_prob = {}
    list_of_nodes = graph.keys()
    prob = 1 / len(graph)
    # Loops through all the keys in the graph
    for keys in list_of_nodes:
        # Makes each value of the key equal to 1/the length of the graph in other words 1/555
        node_prob[keys] = prob

    # Loops through 100 times to randomly go through 100 websites
    for x in range(args.steps):
        next_prob = {}
        # Loops through 555 time to make sure that you go through each key
        for node in graph.keys():
            # Make it equal to 0.0
            next_prob[node] = 0.0
        # Goes through each key in dictionary graph
        for each_key in graph.keys():
            # Makes the probability of landing on that node equal to p with this formula
            p = node_prob[each_key] / (len(graph.get(each_key)))
            # Gets each connecting node
            for target in graph.get(each_key):
                # Increases probability
                next_prob[target] += p
        node_prob = next_prob
    return node_prob


parser = argparse.ArgumentParser(description="Estimates page ranks from link information")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Textfile of links among web pages as URL tuples")
parser.add_argument('-m', '--method', choices=('stochastic', 'distribution'), default='stochastic',
                    help="selected page rank algorithm")
parser.add_argument('-r', '--repeats', type=int, default=1_000_000, help="number of repetitions")
parser.add_argument('-s', '--steps', type=int, default=100, help="number of steps a walker takes")
parser.add_argument('-n', '--number', type=int, default=20, help="number of results shown")

if __name__ == '__main__':
    args = parser.parse_args()
    algorithm = distribution_page_rank if args.method == 'distribution' else stochastic_page_rank
    graph = load_graph(args)
    print_stats(graph)
    start = time.time()
    ranking = algorithm(graph, args)
    stop = time.time()
    time = stop - start
    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100 * v:.2f}\t{k}' for k, v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")
