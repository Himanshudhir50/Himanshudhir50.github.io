var x1 = -20;
var x2 = 20;

function setup() {
  createCanvas(1400, 800);
  noStroke(); 
}

function draw() {
  background(0);
  x1 += 0.5;
  x2 += 0.5;
  arc(x1, 30, 40, 400, 200, 5.76, 40);
  arc(x2, 90, 40, 200, 200, 5.76, 40);
}