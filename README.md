# Women Who Code - CONNECT Conference Workshop

## What does this repo have?
1. Data - A list of (lat,lng) coordinates around San Francisco. Look under `gps-fun/data`.
2. A Frontend Page - To visualize the raw data and clustered results on the map.
3. Scripting entries - Run clustering algorithms to generate clusters and find the most representative center of a cluster. Centers can be visualized on the frontend page.

## Setup
The following steps will help you setup a development environment.

1. ### Install pip
```
$ sudo easy_install pip
```

2. ### Install virtualenv
```
$ sudo pip install virtualenv
```

3. ### Clone this repository
```
$ git clone git@github.com:salami162/gps-fun.git
$ cd gps-fun
```

4. ### Activate virtual environment
```
$ virtualenv venv
$ source venv/bin/activate
```

5. ### Install the required python packages
```
$ pip install -r requirements.txt
```

6. ### Find Help/Available options
```
$ python manage.py --help
```

7. ### Running the server
```
python manage.py runserver
```
This will launch a server on localhost at port 5000. Hit up the index page at ```http://localhost:5000/```
The Start/Stop toggle button on the top right corner is meant to start polling for changes in the trained clusters. Before you hit it the first time, make sure you've run atleast one round of clustering, so as to generate a `./data/trained_output.csv`. To run one, see the next step.

8. ### Running KMeans
```
python manage.py kmeans -c 4 -src './data/wwc_conf_dataset_tiny.csv' -dest './data/trained_output.csv'
```
Given a csv file of locations, generates clusters and outputs the cluster centers into another csv file. The above command will output 4 clusters, with the lat/lng of the centers in `./data/trained_output.csv`


## Recommended Reading
Here's some reading you can do to help familiarize yourself with [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis), [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) and [Hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering).

### Documentation
[sklearn clustering](http://scikit-learn.org/stable/modules/clustering.html) links to docs for the python package that implements various clustering algorithms.
