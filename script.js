<script>
var images = document.getElementsByTagName("img");
var text = document.getElementsByTagName("input");

// HTML collection -> array
images = Array.prototype.slice.call(images);
text = Array.prototype.slice.call(text);

function generateJson() {
    output = document.getElementsByTagName("textarea")[0];
    let res = "{\n";

    for (var i=0;i<text.length;i++) {
	res += '  "' + images[i].getAttribute("src") + '": [';
	let words = text[i].value.split(",");

	words.forEach(elem => {
	    if(elem[0] == " ") {
		elem = elem.substr(1);
	    }
	    res += '"' + elem + '", ';
	});

	// also remove the extra ", " at the end of each list
	res = res.slice(0, -2) +  '],\n';
    }

    output.value = res.slice(0,-2) + "\n}";
}
</script>
