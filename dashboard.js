// ====== ENHANCED MATRIX RAIN ======
(function() {
  var c = document.getElementById("matrix-canvas");
  if (!c) return;
  var ctx = c.getContext("2d");
  c.width = window.innerWidth;
  c.height = window.innerHeight;
  
  // Multiple streams with different colors
  var streams = [];
  var streamCount = Math.floor(c.width / 12);
  
  for (var i = 0; i < streamCount; i++) {
    streams.push({
      x: i * 12 + Math.random() * 6,
      y: Math.random() * c.height,
      speed: 1 + Math.random() * 3,
      chars: [],
      maxChars: 8 + Math.floor(Math.random() * 12),
      color: Math.random() > 0.7 ? "#ff77aa" : (Math.random() > 0.5 ? "#aa55ff" : "#ff55aa"),
      glow: Math.random() > 0.8
    });
  }
  
  // Katakana + symbols + numbers
  var chars = [];
  for (var i = 0; i < 48; i++) chars.push(String.fromCharCode(0x30A0 + i));
  for (var i = 0; i < 10; i++) chars.push(String(i));
  chars.push("Ω", "Ψ", "Σ", "Π", "Φ", "∞", "∴", "∵", "∈", "∉", "⊕", "⊖", "★", "☆", "♦", "♠", "♣", "♥", "※", "¶", "§", "©", "®", "™");
  
  setInterval(function() {
    // Fade with trail effect
    ctx.fillStyle = "rgba(10,10,15,0.06)";
    ctx.fillRect(0, 0, c.width, c.height);
    
    for (var i = 0; i < streams.length; i++) {
      var s = streams[i];
      
      // Add new character occasionally
      if (Math.random() > 0.92 && s.chars.length < s.maxChars) {
        s.chars.push({
          char: chars[Math.floor(Math.random() * chars.length)],
          alpha: 1,
          y: s.y
        });
      }
      
      // Draw all chars in stream
      for (var j = 0; j < s.chars.length; j++) {
        var ch = s.chars[j];
        
        // Glow effect for some chars
        if (s.glow && j === s.chars.length - 1) {
          ctx.shadowBlur = 15;
          ctx.shadowColor = s.color;
        } else {
          ctx.shadowBlur = 0;
        }
        
        ctx.fillStyle = s.color;
        ctx.globalAlpha = ch.alpha;
        ctx.font = "13px monospace";
        ctx.fillText(ch.char, s.x, ch.y);
        
        // Fade and move
        ch.y -= s.speed;
        ch.alpha -= 0.015;
        
        // Remove faded chars
        if (ch.alpha <= 0) {
          s.chars.splice(j, 1);
          j--;
        }
      }
      
      // Move stream down
      s.y += s.speed * 0.5;
      
      // Reset when off screen
      if (s.y > c.height + 50) {
        s.y = -20;
        s.chars = [];
      }
      
      // Occasional flash on leading char
      if (Math.random() > 0.995 && s.chars.length > 0) {
        var lead = s.chars[s.chars.length - 1];
        ctx.fillStyle = "#ffffff";
        ctx.fillText(lead.char, s.x, lead.y);
      }
    }
    
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
  }, 35);
})();

(function() {
  var c = document.getElementById("grid-canvas");
  if (!c) return;
  var ctx = c.getContext("2d");
  c.width = window.innerWidth;
  c.height = window.innerHeight;
  var t = 0;
  
  function loop() {
    t += 0.02;
    ctx.fillStyle = "rgba(10,10,15,0.1)";
    ctx.fillRect(0, 0, c.width, c.height);
    ctx.strokeStyle = "#5533aa44";
    ctx.lineWidth = 1;
    var cy = c.height / 2;
    var size = 40 + Math.sin(t) * 10;
    for (var x = 0; x < c.width; x += size) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, c.height);
      ctx.stroke();
    }
    for (var y = 0; y < c.height; y += size) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(c.width, y);
      ctx.stroke();
    }
    for (var r = 0; r < 3; r++) {
      var rad = 100 + r * 150 + Math.sin(t + r) * 30;
      ctx.beginPath();
      ctx.arc(c.width / 2, cy, rad, 0, Math.PI * 2);
      ctx.strokeStyle = "rgba(255,119,170," + (0.3 - r * 0.1) + ")";
      ctx.stroke();
    }
    requestAnimationFrame(loop);
  }
  loop();
})();

(function() {
  for (var i = 0; i < 30; i++) {
    var p = document.createElement("div");
    p.className = "particle";
    p.style.left = (Math.random() * 100) + "%";
    p.style.top = (Math.random() * 100) + "%";
    var sz = 5 + Math.random() * 15;
    p.style.width = sz + "px";
    p.style.height = sz + "px";
    p.style.animationDelay = Math.random() * 5 + "s";
    p.style.background = "radial-gradient(circle, rgba(255,119,170,0.4) 0%, transparent 70%)";
    document.body.appendChild(p);
  }
})();

function showKeyModal() { document.getElementById("key-modal").classList.add("show"); }
function hideKeyModal() { document.getElementById("key-modal").classList.remove("show"); }

async function saveKeys() {
  var keys = {
    openrouter: document.getElementById("key-openrouter").value,
    github: document.getElementById("key-copilot").value,
    mistral: document.getElementById("key-mistral").value,
    gemini: document.getElementById("key-gemini").value
  };
  var toSend = {};
  for (var k in keys) if (keys[k]) toSend[k] = keys[k];
  if (Object.keys(toSend).length === 0) { hideKeyModal(); return; }
  try {
    var r = await fetch("/keys", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(toSend)
    });
    var j = await r.json();
    alert("Keys updated!");
    hideKeyModal();
    loadKeyStatus();
  } catch(e) { alert("Error: " + e); }
}

async function loadKeyStatus() {
  try {
    var r = await fetch("/keys/status");
    var j = await r.json();
    var s = j.status || {};
    document.getElementById("dot-openrouter").className = "dot " + (s.openrouter && s.openrouter.has ? "on" : "off");
    document.getElementById("dot-copilot").className = "dot " + (s.github && s.github.has ? "on" : "off");
    document.getElementById("dot-mistral").className = "dot " + (s.mistral && s.mistral.has ? "on" : "off");
    document.getElementById("dot-gemini").className = "dot " + (s.gemini && s.gemini.has ? "on" : "off");
  } catch(e) {}
}

loadKeyStatus();