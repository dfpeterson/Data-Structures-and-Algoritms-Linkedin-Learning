# Data Structures and Algoritms Linkedin Learning
 Random files as I go through a DSA course to boost my Leetcode daily challenge completion

Notes:
## Stacks
 * Like a stack of plates
 * Insertions and deletions are made at one end only
 * __LIFO__ - Last-in First-out (like accounting)
 * Stack operations:
   * `push()` - add to the top
   * `pop()` - remove from the top and return value
   * `peek()` - see the last item without removing it
   * `is_empty()` - see if it's empty

## 2D Lists
 * Lists of lists
 * Can be a graph
 * 2D list can represent nodes & edges
 * Directed vs undirected
   * Does direction matter?
 * Weighted vs unweighted
   * Values of nodes have weighted relationships
 * Obstacles 
   * Inaccessible nodes or areas
 * _i_, _j_ notation (as opposed to _x_, _y_)
   * goes down and right

## Depth-first search
 * Best for situations where goal is to discover a particular path
 * Looks for goal or dead end and backtracks to last viable path and tries others
 * Doesn't guarantee shortest path
 * Good for:
   * Optimizing criteria (cost, speed, safety, fuel efficiency)
   * Pathfinding
   * Scheduling algorithms
   * Investment decision trees
   * Ordering formula cell evaluations in a spreadsheet
   * Determining order of completion for software builds
   * Data serialization
   * Resolving symbol dependencies
 * Insight: by using a LIFO stack, popping from the stack, adding surrounding nodes (more than one if available), the nature of it means that you automatically traverse down a path until you hit your goal or a dead end and then return to the last viable path if your goal is not reached without additional coding or tracking.

## Queues
 * Like a line IRL
 * Good for shared resources
 * __FIFO__ - Head/Tail
 * Queue operations
   * `enqueue()` - add to the back
   * `dequeue()` - remove from the front
   * `is_empty()`

## Breadth-first Search
 * Queue-based implementation
 * Radiates out from starting point
 * Shortest path (w/o any edge weights)
   * looks 1st edge away then increases
 * Uses:
   * GPS
   * Flight reservations
   * P2P neighbor nodes
   * Social networking connections
   * Web crawlers
   * Lots of AI applications
   * Electronics and communication
   * Scientific modelling
 * AKA "Flood fill"

## Priority Queue
 * Resources need to be prioritized
 * Like hospital triage
 * Uses:
   * AI, A* algorithm
   * Optimizing algorithms
   * OS System process scheduling
   * Bandwidth Management
   * Situational analysis
   * Spam filtering
 * Operations:
   * `get()` - gets highest priority
   * `put()` - adds an item
   * `is_empty()`
 * Can be added at any time, but only highest priority item can be grabbed

## The A* Algorithm
 * Shortest paths
 * Used in:
   * Traffic navigation
   * Social network analyses
   * Natural language processing
   * Machine learning
   * Puzzle solutions and puzzle-like problems
   * Algorithmic trading
   * Robotics
   * Video games
 * Uses a heuristic to determine best path:
   * Distance from path
   * Can use euclidean distance
 * Uses:
   * __G-value__ - best distance from start to current
   * __H-value__ - heuristic distance from current cell to destination
   * __F-value__ - sum of __G-value__ and __H-value__
 * Discovered vs Visited:
   * __Open set__ - discovered, but not necessarily visited
   * __Closed set__ - visited