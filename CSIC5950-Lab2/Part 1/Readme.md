Part 1
For each player, we define the comfortable zone of shooting as a matrix of,
{SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
In part 1 of the lab, we implemented a K-Means algorithm to classify each player’s records into 4 comfortable zones. Considering the hit rate, we also figured out which zone is the best for James Harden, Chris Paul, Stephen Curry, and Lebron James.
1.	Initializing spark session
2.	Loading the csv file into the spark context and filter based on player names and the given column names. Converting the DataFrame into RDD through map to prepare for the iteration.
3.	After the previous step, we implemented the K-Means algorithm by randomly selecting 4 rows as preliminary centroids.

Then iteratively run the K-Means algorithm. We determine the separations between each data point and the four original centroids, then place each one in the cluster to which its closest centroid belongs. The new centroid is then calculated for each cluster by taking the mean of each column. We then compute the distance between each data point and the new centroids, giving us 4 new centroids. Until the new centroids are equal to the old centroids or until the maximum number of iterations has been achieved, this process is iterated.
First, we calculate the distance of each data to the centroid and then assign each data to its closest centroid. Then we find the mean iteration for each cluster to determine the new centroid: the distance between each data point and the NEW centroid. Finally, we stop the iteration when the original and new centroids are equal, or when the maximum number of iterations has been reached.
