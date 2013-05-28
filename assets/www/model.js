$( document ).ready(function() {

	$.ajax({
		url: 'http://localhost:9980/modeljsonp', 
		dataType: 'jsonp',
		type: 'GET',
	})
	.done(function(json){
		$.each(json.users, function(i, obj) {
			  console.log('user: ' + obj.user_id + ' - ' + obj.name);
			  $("select#userId").append('<option value="'+obj.user_id+'">'+obj.name+'</option>');			  
		});
		$("select#userId").selectmenu("refresh");
		
		var radioList = "<fieldset data-role=\"controlgroup\"><legend>Choose your favourite movie</legend>";
		$.each(json.movies, function(i, obj) {
			radioList += '<input name="movieId" id="radio-'+obj.movie_id+'" value="'+obj.movie_id+'" type="radio"/>'+
	        			 '<label for="radio-'+obj.movie_id+'">'+obj.title+'</label>';
			
            console.log('movie: ' + obj.movie_id + ' - ' + obj.title);
		});
		radioList += "</fieldset>";
		
        $('form').append(radioList);
        $('form').append("<input value=\"My vote!\" type=\"submit\">").trigger("create");

	})
	.fail(function(msgjqXHR, textStatus, errorThrown){
		console.log(msgjqXHR);
		console.log(textStatus);
		console.log(errorThrown);
		alert('Error. msgjqXHR: ' +  msgjqXHR + ' textStatus: ' + textStatus + ' errorThrown: ' + errorThrown);
	})
	;

});

