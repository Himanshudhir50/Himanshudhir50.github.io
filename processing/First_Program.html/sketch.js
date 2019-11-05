function setup() {
  createCanvas(1400, 800);
  background(240, 240, 240);
  }
  function draw() {
  if (mouseIsPressed) {
  fill(0);
  } else {
    fill(random(256),random(256),random(256));
  }
  ellipse(mouseX, mouseY, 80, 80);
  }