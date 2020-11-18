var opened = false;


$("#hamburgerImg").click(() => {
	
	if (opened) {
		
		opened = false;
		$("body").css("overflow-y", "scroll");
		console.log("Closed")

	} else {
		opened = true;
		$("body").css("overflow-y", "hidden");
		console.log("Open")
	}

	$("#menuDiv").slideToggle()
})

$("#button1").click(() => {
	window.location.href = "/"
})

$("#button2").click(() => {
	window.location.href = "/1"
})

$("#button3").click(() => {
	window.location.href = "/2"
})

$("#button4").click(() => {
	window.location.href = "/3"
})

$("#button5").click(() => {
	window.location.href = "/4"
})

$("#button6").click(() => {
	window.location.href = "/citations"
	console.log("HELLLO")
})

