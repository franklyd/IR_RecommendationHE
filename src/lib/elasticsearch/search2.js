var elasticsearch = require('elasticsearch');
var util = require('util');
var HttpConnector = require('elasticsearch/src/lib/connectors/http');

function MyHttpConnector(host, config) {
  HttpConnector.call(this, host, config);
}
util.inherits(MyHttpConnector, HttpConnector);
MyHttpConnector.prototype.makeReqParams = function(params) {
  params = params || {};
  params.method = params.method || 'POST';
  return HttpConnector.prototype.makeReqParams.call(this, params);
};

var client = new elasticsearch.Client({
  connectionClass: MyHttpConnector
});
