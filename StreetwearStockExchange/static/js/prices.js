$(document).ready(function() {
	console.log("ready");

	var csrftoken = $.cookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
});

function lookupSaleHistory() {
	search = "supreme arc logo crewneck";

	$.ajax({
		url: "/prices/get_history/",
		type: "POST",
		content_type: 'application/json',
		data_type: "json",
		data: {data: JSON.stringify({'search': search})},
		success: function (data) {
			data = JSON.parse(data);
			console.log(data["searchResult"]["item"]);
		}
	});

}