$(function(){

	$('.trailerClass a').click(function(e){

		e.preventDefault();
		var current = $(this);
		var url = $(current).attr("id");

		$('#trailerModal').modal('open');
		var element = '<iframe src="'+url+'" width="100%" height="395" frameborder="0" allowfullscreen></iframe>'
		$('.modal-content').append(element);
	});

	$('.modal').modal({

		dismissible: true, 
		opacity: .5, 
		in_duration: 300, 
		out_duration: 300, 
		starting_top: '4%', 
		ending_top: '10%',
		complete: function() { 

			$('.modal-content').empty();
		}
	});

	$('.modal-close').click(function(e){

		$('#trailerModal').modal('close');
		$('.modal-content iframe').attr("src" , "");
		$('.modal-content p').text("");	
	});
});