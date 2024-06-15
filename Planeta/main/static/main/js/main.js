


  window.addEventListener('scroll', e =>{
    document.body.style.cssText = `--scrollTop:  ${this.scrollY}px`
})

var modal = document.getElementById("myModal");
var btn = document.querySelector(".main-header a");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
