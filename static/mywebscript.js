let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
        if (this.status == 200) {
            document.getElementById("system_response").innerHTML = this.responseText;
        } else {
            document.getElementById("system_response").innerHTML =
                "Error: " + this.responseText;
        }
    }
};

    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
