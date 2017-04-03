//var elasticsearch = require('elasticsearch');
//var elasticsearch = require('elasticsearch-js/elasticsearch.min.js');
//var client = elasticsearch.Client({ 'elasticsearch-js/elasticsearch.min.js' });
//var client = elasticsearch.Client({ ... });
var client = new $.es.Client({
    host: 'localhost:9200',
    log: 'trace'
});

var user_rec_ids;

function setUserValue(value) {
    this.user_rec_ids = value;
}

function getUserValue() {
    return this.user_rec_ids;
}

function showUserInfo() {
    var rec_ids = getUserValue();
    rec_ids = rec_ids['_source']['List of venue_id'];
    alert("This is the object" + rec_ids)
}

var rec_venues;

function setVenueValue(value) {
    this.rec_venues = value;
}

function getVenueValue() {
    return this.rec_venues;
}

function showImg() {
    var rec_ids = getVenueValue();
    var elem = document.createElement("img");
    elem.setAttribute("src", rec_ids[0]["_source"]["photo"][0]);
    elem.setAttribute("height", "300");
    elem.setAttribute("width", "200");
    elem.setAttribute("alt", "Flower");
    document.getElementById("img1").appendChild(elem);

    document.getElementById('location1').innerHTML = rec_ids[0]["_source"]["name"];
    document.getElementById('Explanation1').innerHTML = rec_ids[0]["_source"]["description"];

    var elem = document.createElement("img");
    elem.setAttribute("src", rec_ids[1]["_source"]["photo"][0]);
    elem.setAttribute("height", "300");
    elem.setAttribute("width", "200");
    elem.setAttribute("alt", "Flower");
    document.getElementById("img2").appendChild(elem);

    document.getElementById('location2').innerHTML = rec_ids[1]["_source"]["name"];
    document.getElementById('Explanation2').innerHTML = rec_ids[1]["_source"]["description"];

    var elem = document.createElement("img");
    elem.setAttribute("src", rec_ids[2]["_source"]["photo"][0]);
    elem.setAttribute("height", "300");
    elem.setAttribute("width", "200");
    elem.setAttribute("alt", "Flower");
    document.getElementById("img3").appendChild(elem);

    document.getElementById('location3').innerHTML = rec_ids[2]["_source"]["name"];
    document.getElementById('Explanation3').innerHTML = rec_ids[2]["_source"]["description"];
}
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
    }, function(error) {
        if (error) {
            console.trace('elasticsearch cluster is down!');
        } else {
            console.log('All is well');
        }
    });

window.onload=function(){document.getElementById('Tue').innerHTML=xyz("userid")}
id=xyz("userid");
getUserRecommendations(id);

function getUserRecommendations(id) {
    var user_info;
    client.search({
        index: 'bm25_test',
        type: 'user',
        q: id
    }).then(function(body) {
        user_info = body.hits.hits[0];
        if (user_info != null) {
            setUserValue(user_info);
            retriveVenueInfo()
        }
    }, function(error) {
        console.trace(error.message);
    });

}

function retriveVenueInfo() {
    var rec_venue_info = [];
    var venue;
    var rec_ids = getUserValue();
    var venueIds = rec_ids["_source"]["List of venue_id"]
    for (var i = 0; i < venueIds.length; i++) {
        console.log(venueIds[i])
        client.search({
            index: 'bm25_test',
            type: 'london_instagram',
            q: venueIds[i]
        }).then(function(body) {
            venue = body.hits.hits[0];
            rec_venue_info.push(venue);
            if (rec_venue_info.length == 3) {
                setVenueValue(rec_venue_info);
                showImg()
            }

        }, function(error) {
            console.trace(error.message);
        });
    }

}

function xyz(param) {
    var found;
    window.location.search.substr(1).split("&").forEach(function(item) {
        if (param ==  item.split("=")[0]) {
            found = item.split("=")[1];
        }
    });
    return found;
}


//client.response(){}
client.count({
  index: 'bm25_test',
  type: 'table'
}, function (error, response) {
  console.log(response);
});

client.update({
  index: 'bm25_test',
  type: 'table',
  id: '300',
  body: {
    // put the partial document under the `doc` key
    doc: {
      country: 'NL'
    }
  }
}, function (error, response) {
  // ...
  console.log(response);
});

/*client.update({
  index: 'bm25_test',
  type: 'table',
  id: '300',
  body: {
    script: 'ctx._source.tags.contains(tag) ? ctx.op = "delete" : ctx.op = "none"',
    params: {
      tag: 'to-delete'
    }
  }
}, function (error, response) {
  // ...
});*/