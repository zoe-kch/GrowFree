window.onscroll = function() {scrollFunction()};

document.getElementById("dropdown").style.display = "none";
document.getElementById("filterType").style.height = "40px";

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("logo").style.maxBlockSize = "8vw";
        document.getElementById("navBar").style.borderBottomStyle = "none";
        document.getElementById("navBar").style.width = "100%";
    } else {
        document.getElementById("logo").style.maxBlockSize = "10vw";
        document.getElementById("navBar").style.borderBottomColor = "#f6dc1d"
        document.getElementById("navBar").style.borderBottomStyle = "solid";
        document.getElementById("navBar").style.borderBottomWidth = "2px";
    }
  }

function dropdown() {
    document.getElementById("dropdown").style.display = "block";
    document.getElementById("interestsBox").style.display = "none";
}
function highlight(x) {
    document.getElementById(x).style.backgroundColor = "#f6dc1d";
}
function oppDropdown() {
    document.getElementById("filterType").style.height = "max-content";
}