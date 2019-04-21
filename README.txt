Udit Das
CS455 Dr.S
Final Project
******************************************************
Files edited: search.py
	     functions edited: 	breadthFirstSearch
				depthFirstSearch
				aStarSearch
				iterativeDeepeningSearch 
******************************************************

References:
http://ai.berkeley.edu/search.html
https://github.com/richss/CS455-search-python/blob/master/uninformed.ipynb


Depth-First Search:
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
python pacman.py -l openMaze -z .5 -p SearchAgent
Breadth-First Search :
python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs
python pacman.py -l openMaze -p SearchAgent -a fn=bfs
Iterative Deepening Search:
python pacman.py -l tinyMaze -p SearchAgent -a fn=ids
python pacman.py -l mediumMaze -p SearchAgent -a fn=ids -z .5
python pacman.py -l bigMaze -p SearchAgent -a fn=ids -z .5
python pacman.py -l openMaze -p SearchAgent -a fn=ids -z .5
A* Search:
python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
