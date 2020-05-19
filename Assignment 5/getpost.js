var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout: 'main'});

var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 6615);

app.get(‘/getCheck’, function(req, res){
  var parameters = [];
  for (var x in req.query) {
    parameters.push({'name': x, 'value': req.query[x]})
  }

	var context = {};
	context.dataList = parameters;
	res.render('getChecker', context);
});

app.post(‘/postCheck’,function(req,res){
    var parameters = [];
    for (var x in req.query){
        parameters({‘name’:x, ‘value’:req.query[x]})
    }
    for (var x in req.body){
        parameters.push({"name":i, "value":req.body[i]})
    }

  var context = {};
  context.dataList = parameters;
  res.render(‘postChecker’, context);
}

app.use(function(req, res) {
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function() {
  console.log('Express started on http://flip3.engr.oregonstate.edu:' + app.get('port') + '; press Ctrl-C to terminate.');
});
