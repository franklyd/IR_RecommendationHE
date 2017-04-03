//var elasticsearch = require('elasticsearch');
//var elasticsearch = require('elasticsearch-js/elasticsearch.min.js');
//var client = elasticsearch.Client({ 'elasticsearch-js/elasticsearch.min.js' });
//var client = elasticsearch.Client({ ... });
var client = new $.es.Client({
    host: 'localhost:9200',
    log: 'trace'
});

var user_info;

function setUserInfo(value) {
    this.user_info = value;
}

function getUserInfo() {
    return this.user_info;
}

var user_index;

function setUserIndex(value) {
    this.user_index = value;
}

function getUserIndex() {
    return this.user_index;
}
var user_count;

function setUserCountValue(value) {
    this.user_count = value;
}

function getUserCountValue() {
    return this.user_count;
}

function showInfo(){
    var user_data = getUserInfo();
    document.getElementById('location').innerHTML = user_data["user_id"];// + " " + user_data["List of venue_id"];

}

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

GetCountofUsers();

function GetCountofUsers() {
    var temp;
    client.count({
        index: 'bm25_test',
        type: 'user'
    }, function(error, response) {
        console.log(response);
        temp = response['count'];
        if (temp != null) {
            setUserCountValue(temp);
            GenerateRandomUserId();
        }
    });
}

function GenerateRandomUserId() {
    var total = getUserCountValue();
    var rand = Math.floor(Math.random() * total);
    console.log(rand);
    setUserIndex(rand);
    getUserdata();

}


function getUserdata() {
    var user_index = getUserIndex();
    console.log(user_index);
    var temp_user;
    client.get({
        index: 'bm25_test',
        type: 'user',
        id: user_index
    }, function(error, response) {
        //temp = response.hits.hits[0];
        temp_user = response['_source'];
        if (temp_user != null) {
            setUserInfo(temp_user);
            console.log(temp_user);
            showInfo()
        }
            });

}

window.onload = function() {
    var elem = document.createElement("img");
    elem.setAttribute("src", "https://upload.wikimedia.org/wikipedia/commons/b/b4/London_Eye_Twilight_April_2006.jpg");
    elem.setAttribute("height", "250");
    elem.setAttribute("width", "200");
    elem.setAttribute("alt", "Flower");
    document.getElementById("placehere").appendChild(elem);
}