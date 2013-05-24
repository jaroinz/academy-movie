$('form').submit(function(){
	
	var postData = $(this).serialize();
	console.log(postData);
	
	$.ajax({
		data: postData,
		url: 'http://localhost:9980/votejsonp', 
		dataType: 'jsonp',
		type: 'GET',
	})
	.done(function(msg){
		console.log('result: ' + msg.result + ' msg: ' + msg.message +' ' + msg.votes);
		alert('result: ' + msg.result + ' msg: ' + msg.message +' ' + msg.votes );
	})
	.fail(function(msgjqXHR, textStatus, errorThrown){
		console.log(msgjqXHR);
		console.log(textStatus);
		console.log(errorThrown);
		alert('Error. msgjqXHR: ' +  msgjqXHR + ' textStatus: ' + textStatus + ' errorThrown: ' + errorThrown);
	})
	;
	
	return false;
});
