function myFunction() {
    var x = document.getElementById("navBarID");
    if (x.className === "navBar") {
      x.className += " responsive";
    } else {
      x.className = "navBar";
    }
  }