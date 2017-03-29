//var elasticsearch = require('elasticsearch');
//var elasticsearch = require('elasticsearch-js/elasticsearch.min.js');
//var client = elasticsearch.Client({ 'elasticsearch-js/elasticsearch.min.js' });
//var client = elasticsearch.Client({ ... });


var client = new $.es.Client({
  host: 'localhost:9200',
  log: 'trace'
});

/*
var client = new elasticsearch.Client({
  host: 'localhost:9200',
  log: 'trace'
});
*/
var table =

client.ping({
  // ping usually has a 3000ms timeout
  requestTimeout: 1000
}, function (error) {
  if (error) {
    console.trace('elasticsearch cluster is down!');
  } else {
    console.log('All is well');
  }
});





client.search({
    index: 'bm25_test',
    type: 'table',
    q: 'Movies'
}).then(function(body) {
    var hits = body.hits.hits;
    console.log(body);
}, function(error) {
    console.trace(error.message);
});


/*
client.response(){

}
*/
