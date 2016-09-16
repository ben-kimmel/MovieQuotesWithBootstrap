var rh = rh || {};
rh.mq = rh.mq || {};
rh.mq.editing = false;

rh.mq.enableButtons = function() {
	$("#toggle-edit").click(function() {
		if (rh.mq.editing) {
			rh.mq.editing = false;
			$(".edit-actions").addClass("hidden");
			$(this).html("Edit");
		} else {
			rh.mq.editing = true;
			$(".edit-actions").removeClass("hidden");
			$(this).html("Done");
		}
	});

	$("#add-quote").click(function() {
		$("#add-quote-modal .modal-title").html("Add a MovieQuote");
		$("#add-quote-modal button[type=submit]").html("Add Quote");
		$("#add-quote-modal input[name=quote]").val("");
		$("#add-quote-modal input[name=movie]").val("");
		$("#add-quote-modal input[name=entity_key]").val("").prop("disabled", true);
	});

	$(".edit-movie-quote").click(function() {
		$("#add-quote-modal .modal-title").html("Edit this MovieQuote");
		$("#add-quote-modal button[type=submit]").html("Edit Quote");

		var quote = $(this).find(".quote").html().trim();
		var movie = $(this).find(".movie").html().trim();
		var entityKey = $(this).find(".entity-key").html().trim();

		$("#add-quote-modal input[name=quote]").val(quote);
		$("#add-quote-modal input[name=movie]").val(movie);
		$("#add-quote-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
	});
	
	$(".delete-movie-quote").click(function() {
		entityKey = $(this).find(".entity-key").html().trim();
		$("#delete-quote-modal input[name=entity_key]").val(entityKey);
	});
};

rh.mq.attachEventHandlers = function() {
	$('#add-quote-modal').on('shown.bs.modal', function() {
		$("input[name='quote']").focus();
	});
};

$(document).ready(function() {
	rh.mq.enableButtons();
	rh.mq.attachEventHandlers();
});
