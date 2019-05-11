
var images = document.getElementsByTagName("img");
var text = document.getElementsByTagName("input");

images = Array.prototype.slice.call(images);
text = Array.prototype.slice.call(text);

function generateJson() {
    output = document.getElementById("output");

    output.value = "{\n";

    for (var i=0;i<text.length;i++) {
	output.value += '  "' + images[i].src + '": '
	    + '"' + text[i].value + '"\n';
    }

    output.value += "}";
}
