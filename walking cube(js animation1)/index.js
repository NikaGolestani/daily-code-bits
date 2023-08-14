var x = 0;
var v = 1;
var w = 0;
var y = 200;
var l = 50;
var z = 200;
var box = document.getElementById("small");
var t = setInterval(move, 10);
function move() {
  x += v;
  box.style.left = x + "px";
  if (x === y) {
    if (w === z) {
      l *= -1;
      if (z === 200) {
        z = 0;
      } else {
        z = 200;
      }
    }

    w += l;
    box.style.top = w + "px";
    v *= -1;

    if (y === 200) {
      y = 0;
    } else {
      y = 200;
    }
  }
}
