function queryUser(id){
 var check
  client.search({
    index: 'bm25_test',
    type: 'user',
    q: id
}).then(function(body) {
    var hits = body.hits.hits[0];
    check=body.hits.hits[0];
    //console.log(body.hits.hits[0]);
}, function(error) {
    console.trace(error.message);
});
return check;
}