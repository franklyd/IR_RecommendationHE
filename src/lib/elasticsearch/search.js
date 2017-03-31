//var elasticsearch = require('elasticsearch');
//var elasticsearch = require('elasticsearch-js/elasticsearch.min.js');
//var client = elasticsearch.Client({ 'elasticsearch-js/elasticsearch.min.js' });
//var client = elasticsearch.Client({ ... });

var temp;
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


var venue;
var c=[];
 client.search({
    index: 'bm25_test',
    type: 'user',
    q: '225059732'
}).then(function(body) {
    var hits = body.hits.hits[0];
    console.log(body.hits.hits[0]);
    temp=body.hits.hits[0];
    //console.log(body.hits.hits[0]);
}, function(error) {
    console.trace(error.message);
});



function Display() {
  console.log(temp);
  console.log(temp["_source"]["List of venue_id"]);
  var venueIds=temp["_source"]["List of venue_id"]
  for (var i = 0; i < venueIds.length; i++) {
    console.log(venueIds[i])
     client.search({
    index: 'bm25_test',
    type: 'london_instagram',
    q: venueIds[i]
}).then(function(body) {
    var hits = body.hits.hits[0];
    console.log(body.hits.hits[0]);
    venue=body.hits.hits[0];
    c.push(venue);
    //console.log(body.hits.hits[0]);
}, function(error) {
    console.trace(error.message);
});
  }
}
function venue(){
  console.log("tes");
}
/*

client.response(){

}

function queryVenue(id){
 
  client.search({
    index: 'bm25_test',
    type: 'london_instagram',
    q: id
}).then(function(body) {
    var hits = body.hits.hits[0];
    check=body.hits.hits[0];
    //console.log(body.hits.hits[0]);
}, function(error) {
    console.trace(error.message);
});
console.log(check)
return check
}
*/