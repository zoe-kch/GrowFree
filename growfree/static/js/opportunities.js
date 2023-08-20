window.onscroll = function() {scrollFunction()};

document.getElementById("dropdown").style.display = "none";

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("logo").style.maxBlockSize = "8vw";
        document.getElementById("navBar").style.borderBottomStyle = "none";
    } else {
        document.getElementById("logo").style.maxBlockSize = "10vw";
        document.getElementById("navBar").style.borderBottomStyle = "solid";
    }
  }

function dropdown() {
    document.getElementById("dropdown").style.display = "block";
    document.getElementById("interestsBox").style.display = "none";
}
function highlight(x) {
    document.getElementById(x).style.backgroundColor = "#f6dc1d";
}