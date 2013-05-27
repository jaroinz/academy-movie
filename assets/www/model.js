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
		$.each(json.movies, function(i, obj) {
			  console.log('movie: ' + obj.movie_id + ' - ' + obj.title);
			  $('fieldset[data-role="controlgroup"]').append(
			        '<input name="movieId" id="radio-'+obj.movie_id+'" value="'+obj.movie_id+'" type="radio"/>'+
			        '<label for="radio-'+obj.movie_id+'">'+obj.title+'</label>'					  
			  );
		});
        $("input[type='radio']").checkboxradio().checkboxradio("refresh");

	})
	.fail(function(msgjqXHR, textStatus, errorThrown){
		console.log(msgjqXHR);
		console.log(textStatus);
		console.log(errorThrown);
		alert('Error. msgjqXHR: ' +  msgjqXHR + ' textStatus: ' + textStatus + ' errorThrown: ' + errorThrown);
	})
	;

});

