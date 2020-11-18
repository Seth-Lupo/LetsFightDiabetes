console.log("Hello :D")

$("#nextButton").click(() => {

	console.log("IM CLICKED")

	var lastChar = window.location.href.slice(-1);

	switch(lastChar) {

		case "1":

			window.location.href = "/2"
			break;

		case "2":

			window.location.href = "/3"
			break;

		case "3":

			window.location.href = "/4"
			break;

		case "4":

			window.location.href = "/citations"
			break;

		case "/":

			window.location.href = "/1"

			break;

	}
})

$(".postButton").click(() => {

		
	if($('.nameField').val() == "" || $('.nameField').val() == "") {

		$(".alertLabel").text("Please enter your name and response.")



	} else {

		$.ajax({
			type: "POST",
		  	url: window.location.origin = "/responses/" +  window.location.href.slice(-1),
	  		data: {

	  			csrfmiddlewaretoken: TOKEN,
	  			name: $('.nameField').val(),
	  			responses: $('.responseField').val(),


	  		}
		}).done(function() {
	  		
			window.location.href = "responses/" +  window.location.href.slice(-1)
			console.log("IM CLICKED")

		});


		var lastChar = window.location.href.slice(-1)
		(".alertLabel").text("")

	}

})

$(".viewButton").click(() => {

	console.log("IM CLICKED")

	window.location.href = "responses/" +  window.location.href.slice(-1)

})


setTimeout(function () {
    var viewheight = $(window).height();
    var viewwidth = $(window).width();
    var viewport = $("meta[name=viewport]");
    viewport.attr("content", "height=" + viewheight + "px, width=" + 
    viewwidth + "px, initial-scale=1.0");
}, 300);

$("#citationButton").click(() => {
	window.location.href =  "/citations"
})