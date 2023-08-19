window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("logo").style.maxBlockSize = "8vw";
    } else {
        document.getElementById("logo").style.maxBlockSize = "10vw";
    }
  }