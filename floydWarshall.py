# User function Template for Python

class Solution:
    # Function to implement the Floyd–Warshall algorithm
    def floydWarshall(self, dist):
        V = len(dist)
        
        # Triple nested loops to consider every possible intermediate vertex
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    # Relax the edge if a shorter path exists via vertex k
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist
