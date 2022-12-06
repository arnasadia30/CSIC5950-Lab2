**Part 3**

In part 3 of the lab, we figured out when tickets are most likely to be issued by trying out different levels of
parallelism, 2, 3, 4, 5. In order to do so,we set the configuration of spark-submit to the parallelism levels by 
adding the following line of code after spark-submit in the test.sh file: 

–conf spark.default.parallelism=2
