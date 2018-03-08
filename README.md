## Welcome UitleggenAll - Team 7 - IN4325
# Recommendation System with Human Explanation

### Screencast  Youtube
- [Demo recommendation with human explanation Team 7-IN4325](https://youtu.be/WEFOHZnQ1Xk)


The project is divided in 4 folders. All the folders convey to the 'src' folder where the HTML index is located.

- DataSources: Crawling of twitter and foursquare. DBpedia annotation process of tweets.
- Elasticsearch: Indexing of the data
- Recommender System: Graphlab implementation of the recommendation system and text analysis for topic venues.
- src: Here you will find the main login for the recommendation with human explanation web app

## Requirements:
This web-app was tested with:
- Ubuntu 16.04 LTS
- Elasticsearch 5.2.1
- Elasticsearch JS lib (Already inside /src/lib)

## Start simple HTTP Server
```Mardown
 cd  /src
 sudo python -m SimplHTTPServer 80
```

## Start Elsaticsearch
Becasue we found some irregularities in the JS Elasticsearch lib is necesary to do the next changes in the configuration file of your eleastisearch server.  

```Mardown
 cd $ELASTICSEARCH_PATH/elasticsearch-5.2.1/config

 nano elasticsearch.yml
```
Add next lines of code at the end of elasticsearch.yml file. This will allow HTTP access from your browser to the elasticsearch local server

```Mardown
http.cors:
 enabled: true
 allow-origin: /https?:\/\/localhost(:[0-9]+)?/
```

## Twitter Anlysis Graphs
- [Tweet Analysis](http://nbviewer.jupyter.org/github/franklyd/Jupyter-Notebook-Demo/blob/master/twitter_analysis.ipynb#topic=0&lambda=1&term=)

- [Genrating topics for venue tips in London](https://nbviewer.jupyter.org/github/franklyd/Jupyter-Notebook-Demo/blob/master/Topic%20Modeling%20for%20Foursquare%20Tips%20in%20London.ipynb#topic=1&lambda=1&term=)

### Github repository
- [Team 7 code](https://github.com/broyson/IR_RecommendationHE.git)

## Code used from other authors

[Wordcloud generation in JS @jasondavies](https://github.com/jasondavies/d3-cloud)

## Code example libs
[Polar graph library](https://ecomfe.github.io/echarts-examples/public/)
