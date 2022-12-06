Part 2
In Part 2 of the lab, we implemented a K-Means algorithm using PySpark to find the probability of a black vehicle getting a ticket that has parked illegally at 34510, 10030, and 34050 (street codes). (Very rough prediction)
1.	Initializing spark session
2.	We loaded the CSV file as DataFrame and filtered it according to the color black. We selected the columns of Street code and then transformed the filtered dataframe into RDD.
3.	After the previous step, we implemented the K-Means algorithm by randomly selecting 4 rows as preliminary centroids.
Then iteratively run the K-Means algorithm. We determine the separations between each data point and the four original centroids, then place each one in the cluster to which its closest centroid belongs. The new centroid is then calculated for each cluster by taking the mean of each column. We then compute the distance between each data point and the new centroids, giving us 4 new centroids. Until the new centroids are equal to the old centroids or until the maximum number of iterations has been achieved, this process is iterated.
First, we calculate the distance of each data to the centroid and then assign each data to its closest centroid. Then we find the mean iteration for each cluster to determine the new centroid: the distance between each data point and the NEW centroid. Finally, we stop the iteration when the original and new centroids are equal, or when the maximum number of iterations has been reached.
4.	Finally, we calculate the probability of a black vehicle getting a ticket.
