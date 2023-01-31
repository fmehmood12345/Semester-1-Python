# <u>Optimisation Report</u>

---
### Stochastic PageRank
```
def stochastic_page_rank(graph, args):
    hit_count = {} 
    
    for x in graph_dictionary.keys():
        hit_count[x] = 0.0
        for node in range(args.repeats):
            current_node = random.choice(list(graph_dictionary.keys()))
            for x in range(args.steps):
                current_node = random.choice(graph_dictionary[current_node])
            hit_count[current_node] += 1/args.repeats
    
    return hit_count
```
This is my code before any optimisation, and it took 54.23 seconds to run.

I found out that there are certain part of the code which get unnecessarily repeated multiple times. This 
means that it takes up processing time so in order to reduce this, I decided to make a variable outside the function
which does the calculation just once. This took 48.46 seconds to process.

```
def stochastic_page_rank(graph, args):
    hit_count = {}
    repeat_count = 1 / args.repeats
    
    for x in graph.keys():
        hit_count[x] = 0.0
    for node in range(args.repeats):
        current_node = random.choice(list(graph.keys()))
        for x in range(args.steps):
            current_node = random.choice(graph[current_node])
        hit_count[current_node] += repeat_count
        
    return hit_count
```
As a result of this, `1/args.repeats` is not repeated 100 times which saves processing time. I also found
that `list(graph.key)` also makes the keys of the dictionary into a list 1,000,000 times therefore, I made a seperate
variable outside the loop so that the list is make just once. This took 46.44 seconds to run.
```
def stochastic_page_rank(graph, args):
    hit_count = {}
    repeat_count = 1 / args.repeats
    key_list = list(graph.keys())
    
    for x in graph.keys():
        hit_count[x] = 0.0
    for node in range(args.repeats):
        current_node = random.choice(key_list)
        for x in range(args.steps):
            current_node = random.choice(graph[current_node])
        hit_count[current_node] += repeat_count
        
    return hit_count
```
I then decided to optimise this by removing the random module. The reason I decided to 
remove the `random` module was because in order for the `choice()` function to be called, the program will 
go through all different functions in the random module until the `choice()` function is found. This will lose 
alot of unnecessary time. Therefore, in order to fix this I did the following:
```
def stochastic_page_rank(graph, args):
    hit_count = {}
    repeat_count = 1 / args.repeats
    key_list = list(graph.keys())
    
    for x in graph.keys():
        hit_count[x] = 0.0
    for node in range(args.repeats):
        current_node = choice(key_list)
        for x in range(args.steps):
            current_node = choice(graph[current_node])
        hit_count[current_node] += repeat_count
        
    return hit_count
```
I also assigned graph.keys() to a variable so that the processor does not have to go through all the keys of the graph 
and find the length of the graph for every loop, it can simply find the length of the graph through this variable. This 
resulted in 41.19 seconds taken in total.
```
def stochastic_page_rank(graph, args):
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
```
---
### Distribution PageRank
```
def distribution_page_rank(graph, args):
    node_prob ={}
    next_prob = {}
    
    for keys in graph.keys():
        node_prob[keys] = 1/len(graph)
        
    for x in range(args.steps):
       for node in graph.keys():
            next_prob[node] = 0.0
       for each_key in graph.keys():
            p = node_prob[each_key]/len(graph[each_key])
            for target in graph[each_key]:
                next_prob[target] += p
       node_prob = next_prob
       
    return node_prob
```

There wasn't much I could optimise for this function mainly because even if optimisation was done, the change in
processing time is negligible. The main change I made was to have `.get()` to retrieve the values of a specific key. 
This is the optimised code:
```
def distribution_page_rank(graph, args):
    node_prob = {}
    
    for keys in graph.keys():
        node_prob[keys] = 1 / len(graph)
    
    for x in range(args.steps):
        next_prob = {}
        for node in graph.keys():
            next_prob[node] = 0.0
        for each_key in graph.keys():
            p = node_prob[each_key] / (len(graph.get(each_key)))
            for target in graph.get(each_key):
                next_prob[target] += p
        node_prob = next_prob
        
    return node_prob
```
Another way I optimised the code was by having variables which compute certain things outside the loops. For example,
I changed `graph.keys()` into `list_of_nodes` which is a variable made that contains `graph.keys()`:
```
def distribution_page_rank(graph, args):
    node_prob = {}
    list_of_nodes = graph.keys()
    
    for keys in list_of_nodes:
        node_prob[keys] = 1 / len(graph)
    
    for x in range(args.steps):
        next_prob = {}
        for node in graph.keys():
            next_prob[node] = 0.0
        for each_key in graph.keys():
            p = node_prob[each_key] / (len(graph.get(each_key)))
            for target in graph.get(each_key):
                next_prob[target] += p
        node_prob = next_prob
        
    return node_prob
```

Also, I assigned `1 / len(graph)` to a variable which means that this computation wouldn't take place 555 times 
therefore reducing time.
```
def distribution_page_rank(graph, args):
    node_prob = {}
    list_of_nodes = graph.keys()
    prob = 1 / len(graph)
    
    for keys in list_of_nodes:
        node_prob[keys] = prob
    
    for x in range(args.steps):
        next_prob = {}
        for node in graph.keys():
            next_prob[node] = 0.0
        for each_key in graph.keys():
            p = node_prob[each_key] / (len(graph.get(each_key)))
            for target in graph.get(each_key):
                next_prob[target] += p
        node_prob = next_prob
        
    return node_prob
```
The timings for the distribution pagerank did not change and stayed constant at 0.13 seconds.