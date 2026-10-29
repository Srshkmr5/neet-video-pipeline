const canvas = document.getElementById("scene");
const ctx = canvas.getContext("2d");

const forceInput = document.getElementById("force");
const thetaInput = document.getElementById("theta");
const distanceInput = document.getElementById("distance");

const forceValue = document.getElementById("forceValue");
const thetaValue = document.getElementById("thetaValue");
const distanceValue = document.getElementById("distanceValue");

function updateLabels() {
  forceValue.textContent = `${forceInput.value} N`;
  thetaValue.textContent = `${thetaInput.value}°`;
  distanceValue.textContent = `${distanceInput.value} m`;
}

forceInput.addEventListener("input", updateLabels);
thetaInput.addEventListener("input", updateLabels);
distanceInput.addEventListener("input", updateLabels);

function resizeCanvas() {
  const ratio = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = rect.width * ratio;
  canvas.height = rect.height * ratio;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
}

window.addEventListener("resize", resizeCanvas);
resizeCanvas();

function draw() {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;

  ctx.clearRect(0, 0, w, h);

  // Background
  ctx.fillStyle = "#081521";
  ctx.fillRect(0, 0, w, h);

  // Ground
  ctx.strokeStyle = "#475569";
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(40, h * 0.72);
  ctx.lineTo(w - 40, h * 0.72);
  ctx.stroke();

  const force = Number(forceInput.value);
  const angleDeg = Number(thetaInput.value);
  const distance = Number(distanceInput.value);
  const theta = angleDeg * Math.PI / 180;
  const component = force * Math.cos(theta);

  const blockX = 90;
  const blockY = h * 0.72 - 48;
  const blockW = 110;
  const blockH = 56;

  // block
  ctx.fillStyle = "#1e293b";
  ctx.strokeStyle = "#7dd3fc";
  ctx.lineWidth = 2;
  ctx.fillRect(blockX, blockY, blockW, blockH);
  ctx.strokeRect(blockX, blockY, blockW, blockH);

  ctx.fillStyle = "#e2e8f0";
  ctx.font = "bold 16px Arial";
  ctx.textAlign = "center";
  ctx.fillText("m", blockX + blockW / 2, blockY + blockH / 2 + 6);

  // displacement vector
  const dispX = blockX + blockW + 30;
  const dispY = blockY + blockH / 2;
  const dispLen = distance * 16;
  drawArrow(ctx, blockX + blockW, dispY, blockX + blockW + dispLen, dispY, "#fbbf24", "d");

  // force angle
  const fx = blockX + blockW / 2;
  const fy = blockY + blockH / 2;
  const forceLen = Math.min(160, force * 0.9);
  const forceX = fx + Math.cos(-theta) * forceLen;
  const forceY = fy + Math.sin(-theta) * forceLen;

  drawArrow(ctx, fx, fy, forceX, forceY, "#34d399", "F");

  // component along displacement
  const compX = fx + Math.cos(theta) * Math.min(140, component * 1.5);
  const compY = fy;
  drawDashedLine(ctx, fx, fy, compX, compY, "#7dd3fc", "F cos θ");

  // angle arc
  ctx.strokeStyle = "#fbbf24";
  ctx.beginPath();
  ctx.arc(fx, fy, 36, 0, theta);
  ctx.stroke();

  ctx.fillStyle = "#fbbf24";
  ctx.font = "bold 12px Arial";
  ctx.fillText("θ", fx + 45, fy - 12);

  // work value
  const work = component * distance;
  ctx.fillStyle = "#e2e8f0";
  ctx.font = "bold 14px Arial";
  ctx.textAlign = "left";
  ctx.fillText(`W = F d cos θ = ${work.toFixed(1)} J`, 40, 40);

  ctx.fillStyle = "#94a3b8";
  ctx.font = "12px Arial";
  ctx.fillText("positive if θ < 90°, zero if θ = 90°, negative if θ > 90°", 40, 64);

  requestAnimationFrame(draw);
}

function drawArrow(ctx, x1, y1, x2, y2, color, label) {
  const angle = Math.atan2(y2 - y1, x2 - x1);
  const headlen = 12;

  ctx.strokeStyle = color;
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();

  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - headlen * Math.cos(angle - Math.PI / 6), y2 - headlen * Math.sin(angle - Math.PI / 6));
  ctx.lineTo(x2 - headlen * Math.cos(angle + Math.PI / 6), y2 - headlen * Math.sin(angle + Math.PI / 6));
  ctx.closePath();
  ctx.fillStyle = color;
  ctx.fill();

  ctx.fillStyle = color;
  ctx.font = "bold 12px Arial";
  ctx.fillText(label, (x1 + x2) / 2, (y1 + y2) / 2 - 14);
}

function drawDashedLine(ctx, x1, y1, x2, y2, color, label) {
  ctx.setLineDash([8, 6]);
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.fillStyle = color;
  ctx.font = "bold 11px Arial";
  ctx.fillText(label, (x1 + x2) / 2, (y1 + y2) / 2 - 10);
}

updateLabels();
requestAnimationFrame(draw);
