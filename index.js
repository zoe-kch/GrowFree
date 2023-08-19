window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
      document.getElementById("logo").style.height = "10vh";
    } else {
      document.getElementById("logo").style.height = "20vh";
    }
  }