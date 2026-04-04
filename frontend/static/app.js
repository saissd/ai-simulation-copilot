const API_BASE = "http://127.0.0.1:8000";

// ---------------- LOAD DATA ----------------
async function loadData() {
  const res = await fetch(`${API_BASE}/api/summary`);
  const data = await res.json();

  document.getElementById("summaryBox").innerText = data.summary;
  document.getElementById("insightBox").innerText = data.insight;

  document.getElementById("scalarBox").innerText =
    data.scalar_names.join(", ");
}

// ---------------- CHAT ----------------
async function askQuestion() {
  const question = document.getElementById("questionInput").value;

  const res = await fetch(`${API_BASE}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();

  document.getElementById("chatAnswer").innerText = data.answer;
}

// ---------------- 3D VIEW ----------------
async function load3D() {
  const res = await fetch(`${API_BASE}/api/mesh`);
  const data = await res.json();

  const points = data.points;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, 600/400, 0.1, 1000);

  const renderer = new THREE.WebGLRenderer({
    canvas: document.getElementById("vtkCanvas")
  });

  renderer.setSize(600, 400);

  const geometry = new THREE.BufferGeometry();
  const vertices = new Float32Array(points.flat());

  geometry.setAttribute("position", new THREE.BufferAttribute(vertices, 3));

  const material = new THREE.PointsMaterial({
    size: 0.1,
    color: 0x00ffcc
  });

  const cloud = new THREE.Points(geometry, material);
  scene.add(cloud);

  camera.position.z = 5;

  function animate() {
    requestAnimationFrame(animate);
    cloud.rotation.y += 0.01;
    renderer.render(scene, camera);
  }

  animate();
}

// ---------------- INIT ----------------
document.addEventListener("DOMContentLoaded", () => {
  loadData();
  load3D();

  document.getElementById("askBtn").addEventListener("click", askQuestion);
  document.getElementById("refreshBtn").addEventListener("click", loadData);
});