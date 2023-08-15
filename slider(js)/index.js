var x = 0;
var per = document.getElementById("per");
var next = document.getElementById("next");
var img1 = document.getElementById("img1");
var img2 = document.getElementById("img2");
var img3 = document.getElementById("img3");
per.addEventListener("click", perf);
next.addEventListener("click", nextf);
var arr = [" rgb(255, 105, 180)", "rgb(203, 105, 255", "rgb(128, 255, 105)"];
function perf() {
  x += 1;

  handleimg();
}
function nextf() {
  x -= 1;
  if (x < 0) {
    x += 3;
  }
  handleimg();
}
function handleimg() {
  img1.style.backgroundColor = arr[x % 3];
  img2.style.backgroundColor = arr[(x + 1) % 3];
  img3.style.backgroundColor = arr[(x + 2) % 3];
}
