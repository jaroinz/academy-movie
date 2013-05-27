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
		console.log('result: ' + msg.result + ' msg: ' + msg.message + ' ' + msg.votes);
		var votesList = 'Votes: <br>';
		$.each($('input[type="radio"]'), function(i, obj) {
			var counter = 0;
			$.each(msg.votes, function(j, vobj){
				if(vobj.movie_id==obj.value){
					counter += 1;
				}
			});			
			votesList += counter + ' for ' + $('label[for="'+ obj.id +'"] span[class="ui-btn-text"]').html() + '<br>';	  
		});
		$( "#votingResultsPopUp" ).html(msg.result + ', ' + msg.message + '<br>' + votesList);
				
		$( "#votingResultsPopUp" ).popup( "open" );		
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
