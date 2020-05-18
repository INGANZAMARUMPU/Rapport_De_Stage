jQuery(document).ready(function($) {
//==================== drag code ======================
	let $dragging = null;
	let draggable = null;
	let local_x = null;
	let local_y = null;
	let global_x = null;
	let global_y = null;
	$(".client-table").on("mousedown touchstart", function (event) {
		if( $('#edit_mode').is(':checked') ){
	    	event.preventDefault();
			$dragging = true;
			$(".client-table").css("z-index", 0);
			$draggable = $(this);
		    let offset = $(this).offset();
		    local_x = event.pageX-offset.left;
		    local_y = event.pageY-offset.top;
		    $(this).css("z-index", 1);
		}
	});

	$(".client-table").parent().on("mouseup touchend", function (e) {
	    if ($dragging & $('#edit_mode').is(':checked')) {
	    	event.preventDefault();
		    $dragging = null;
		    let data={
		    	x: $draggable.position().left,
		    	y: $draggable.position().top,
		    };
		    console.log(data);
		    $.ajax({
		        	url: '/api/table/'+$draggable.attr('data-id')+"/",
		        	type: 'PUT',
		        	headers:{ "X-CSRFToken": $.cookie("csrftoken") },
		        	data: data,
		        })
		        .done(function() {
		        	$("#log").text("change table position success");

		        })
		        .fail(function() {
		        	$("#log").text("change element position error");
		        });
	    }

	});

	$(".client-table").parent().on("mousemove touchmove", function (event) {
	    if ($dragging & $('#edit_mode').is(':checked')) {
	    	event.preventDefault();
	    	let offset = $(this).offset();
	    	let max_w = $(this).width()-$draggable.width();
	    	let max_h = $(this).height()-$draggable.height();
	    	global_x = event.pageX-offset.left-local_x;
			global_y = event.pageY-offset.top-local_y;
			// console.log(global_x, max_w, global_y, max_h);
			if(global_x<max_w && global_x>=0 && global_y<max_h && global_y>=0){
				$draggable.css("left", global_x+"px");
				$draggable.css("top", global_y+"px");
			}
	    }
	});
});