# app.py
# pip install flask
# run: python app.py
# open: http://127.0.0.1:5000

from flask import Flask, Response
import os

app = Flask(__name__)

# ====== PERSONALIZE HERE ======
GIRL_NAME = "Manya"
SECRET_PASSWORD = "meow"  # her nickname (case-insensitive match)
NOTE_TEXT = (
    "You have this unfair ability to distract me without even trying. Just like how I easily get distracted by cats."
    "Just a little reminder: you’re adorable, you’re loved, and you make my world loveable."
    "If I were there right now, I’d steal your attention, keep you close,\n"
    "and remind you exactly how adorable you are.\n\n"
    "Come here 🧸💋\n"
    "Your teddy isn’t the only one sending kisses tonight."
)
TEDDY_GIF_URL = "https://media1.tenor.com/m/2QbMJ6FR9TQAAAAd/loveyou-ted.gif"
# ==============================

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>💌 For You</title>
  <style>
    :root{
      --bg1:#ffd6ea; --bg2:#d7f7ff; --ink:#1f1a2b; --muted:#5a516e;
      --card: rgba(255,255,255,0.72); --stroke: rgba(255,255,255,0.55);
      --shadow: 0 20px 60px rgba(31,26,43,.18);
      --accent:#ff4fa6; --accent2:#6b5bff; --radius: 28px;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
      color:var(--ink);
      overflow-x:hidden;
      background: radial-gradient(1200px 900px at 20% 10%, var(--bg2), transparent 60%),
                  radial-gradient(1000px 900px at 80% 20%, var(--bg1), transparent 55%),
                  radial-gradient(1000px 900px at 40% 90%, #fff7d7, transparent 60%),
                  #fff;
    }
    .bg-blobs{position:fixed; inset:0; pointer-events:none; z-index:0;}
    .blob{
      position:absolute; filter: blur(30px); opacity:.45; border-radius: 999px;
      transform: translateZ(0); animation: float 10s ease-in-out infinite;
    }
    .b1{width:380px;height:380px;left:-120px;top:10%;background:#ff8bc7;animation-duration:12s}
    .b2{width:420px;height:420px;right:-160px;top:5%;background:#7be7ff;animation-duration:14s}
    .b3{width:460px;height:460px;left:20%;bottom:-220px;background:#b8a6ff;animation-duration:16s}
    @keyframes float{0%,100%{transform: translate(0,0) scale(1)} 50%{transform: translate(18px,-18px) scale(1.05)}}

    .shell{
      position:relative; z-index:1; min-height:100%;
      display:flex; flex-direction:column; align-items:center; justify-content:center;
      padding:28px 18px; gap:18px;
    }
    .top{width:min(560px, 92vw); display:flex; align-items:center; justify-content:space-between;}
    .pill{
      padding:10px 14px; border-radius:999px;
      background: rgba(255,255,255,0.55);
      border:1px solid rgba(255,255,255,0.65);
      backdrop-filter: blur(10px);
      box-shadow: 0 8px 24px rgba(31,26,43,.08);
      font-size:14px; color:var(--muted);
    }
    .icon-btn{
      width:44px;height:44px;border-radius:14px;
      border:1px solid rgba(255,255,255,0.75);
      background: rgba(255,255,255,0.55);
      backdrop-filter: blur(10px);
      cursor:pointer; font-size:18px;
      box-shadow: 0 10px 26px rgba(31,26,43,.10);
      transition: transform .15s ease, box-shadow .15s ease;
    }
    .icon-btn:hover{transform: translateY(-1px); box-shadow: 0 14px 30px rgba(31,26,43,.14);}
    .icon-btn:active{transform: translateY(1px) scale(.98);}

    .card{
      width:min(560px, 92vw);
      padding:26px 22px 18px;
      border-radius: var(--radius);
      background: var(--card);
      border: 1px solid var(--stroke);
      box-shadow: var(--shadow);
      backdrop-filter: blur(14px);
      position:relative;
    }
    .badge{
      position:absolute; top:14px; right:14px;
      width:46px; height:46px; display:grid; place-items:center;
      border-radius: 16px;
      background: linear-gradient(135deg, rgba(255,79,166,.25), rgba(107,91,255,.18));
      border:1px solid rgba(255,255,255,.55);
    }
    h1{margin:8px 0 8px; font-size: clamp(26px, 4vw, 36px); letter-spacing:-.02em;}
    .sub{margin:0 0 14px; color: var(--muted); line-height:1.4; font-size: 15px;}
    .accent{
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      -webkit-background-clip:text; background-clip:text; color:transparent;
      font-weight:800;
    }
    .teddy-wrap{display:flex; align-items:center; justify-content:center; padding:14px 0 6px; width:100%;}
    .teddy{
      width:min(340px, 82vw);
      max-height: 360px;
      height:auto;
      object-fit: contain;
      background: rgba(255,255,255,0.35);
      border-radius: 24px; border:1px solid rgba(255,255,255,0.55);
      box-shadow: 0 18px 40px rgba(31,26,43,.18);
      transform-origin:center; transition: transform .22s ease;
      user-select:none;
    }
    .teddy.shy{transform: scale(.98) rotate(-1.2deg)}
    .teddy.kiss{transform: scale(1.02) rotate(1deg)}

    .stats{display:grid; grid-template-columns:1fr 1fr; gap:12px; margin: 10px 0 14px;}
    .stat{
      padding:12px 14px; border-radius: 20px;
      background: rgba(255,255,255,0.55);
      border: 1px solid rgba(255,255,255,0.60);
    }
    .stat-num{font-size:22px;font-weight:900}
    .stat-label{font-size:13px;color:var(--muted)}

    .actions{display:flex; gap:12px; flex-wrap:wrap;}
    .btn{
      flex:1; min-width: 170px;
      padding:12px 14px; border-radius: 18px;
      border:1px solid rgba(255,255,255,0.65);
      cursor:pointer; font-weight:800;
      transition: transform .15s ease, box-shadow .15s ease;
    }
    .btn:hover{transform: translateY(-1px); box-shadow: 0 14px 30px rgba(31,26,43,.14);}
    .btn:active{transform: translateY(1px) scale(.99);}
    .primary{background: linear-gradient(135deg, rgba(255,79,166,.92), rgba(107,91,255,.86)); color:white; border:none;}
    .ghost{background: rgba(255,255,255,0.6); color:var(--ink);}

    .hint{margin:12px 2px 0; color:var(--muted); font-size:12.5px; text-align:center;}
    .footer{width:min(560px, 92vw); display:flex; align-items:center; justify-content:space-between; color:var(--muted); font-size:13px;}
    .linkish{background:none; border:none; color: var(--accent2); font-weight:800; cursor:pointer; padding:6px 8px; border-radius: 12px;}
    .linkish:hover{background: rgba(107,91,255,.10);}

    .modal{
      position:fixed; inset:0; display:none;
      align-items:center; justify-content:center;
      padding:18px;
      background: rgba(0,0,0,.30);
      backdrop-filter: blur(8px);
      z-index: 50;
    }
    .modal.show{display:flex;}
    .modal-card{
      width:min(520px, 92vw);
      background: rgba(255,255,255,.80);
      border:1px solid rgba(255,255,255,.70);
      border-radius: 28px;
      box-shadow: 0 30px 80px rgba(0,0,0,.25);
      padding:22px;
      position:relative;
    }
    .close{position:absolute; right:14px; top:14px;}
    .note{color:var(--muted); line-height:1.55; margin:10px 0 16px;}
    .modal-actions{display:flex; gap:12px; flex-wrap:wrap;}
    .tiny{margin:12px 0 0; font-size:12px; color:var(--muted);}

    .toast{
      position: fixed; left: 50%; bottom: 18px;
      transform: translateX(-50%);
      background: rgba(255,255,255,0.78);
      border: 1px solid rgba(255,255,255,0.75);
      backdrop-filter: blur(10px);
      padding:10px 14px; border-radius: 999px;
      box-shadow: 0 16px 44px rgba(31,26,43,.20);
      font-weight:800; color: var(--ink);
      opacity: 0; pointer-events:none;
      transition: opacity .25s ease, transform .25s ease;
      z-index: 60;
    }
    .toast.show{opacity:1; transform: translateX(-50%) translateY(-4px);}

    .pop{
      position: fixed; left: 0; top: 0;
      font-size: 18px;
      transform: translate(-50%, -50%);
      animation: rise 1.4s ease forwards;
      pointer-events:none; z-index: 40;
      filter: drop-shadow(0 10px 18px rgba(31,26,43,.18));
    }
    @keyframes rise{
      0%{opacity:0; transform: translate(-50%,-30%) scale(.6)}
      20%{opacity:1}
      100%{opacity:0; transform: translate(-50%,-140%) scale(1.2)}
    }

    .kiss{
      position: fixed;
      width: 44px; height: 44px;
      display:grid; place-items:center;
      border-radius: 18px;
      background: rgba(255,255,255,0.78);
      border: 1px solid rgba(255,255,255,0.85);
      box-shadow: 0 18px 40px rgba(31,26,43,.20);
      cursor:pointer; z-index: 45;
      animation: bob 1.2s ease-in-out infinite;
      user-select:none;
    }
    @keyframes bob{0%,100%{transform: translate(-50%,-50%)} 50%{transform: translate(-50%,-56%)}}

    /* Password lock UI */
    .lock{display:flex; gap:10px; flex-wrap:wrap; margin-top:12px;}
    .pwd{
      flex: 1; min-width: 190px;
      padding: 12px 14px;
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.75);
      background: rgba(255,255,255,0.65);
      outline: none;
      font-weight: 800;
      color: var(--ink);
      box-shadow: 0 10px 26px rgba(31,26,43,.10);
    }
    .pwd:focus{
      border-color: rgba(107,91,255,0.55);
      box-shadow: 0 16px 38px rgba(31,26,43,.14);
    }
    .hintline{margin-top: 10px; text-align:left;}
    .note-area{margin-top:6px;}
    .shake{animation: shake .32s ease-in-out;}
    @keyframes shake{0%,100%{transform: translateX(0)} 25%{transform: translateX(-6px)} 50%{transform: translateX(6px)} 75%{transform: translateX(-4px)}}
  </style>
</head>

<body>
  <div class="bg-blobs" aria-hidden="true">
    <span class="blob b1"></span>
    <span class="blob b2"></span>
    <span class="blob b3"></span>
  </div>

  <main class="shell">
    <header class="top">
      <div class="pill">✨ a tiny surprise</div>
      <button id="musicBtn" class="icon-btn" aria-label="Toggle music" title="Toggle music">♪</button>
    </header>

    <section class="card">
      <div class="badge">💗</div>

      <h1>
        Hey <span id="herName" class="accent"></span> 🧸
      </h1>
      <p class="sub">
        Your teddy is here to send you <span class="accent">flying kisses</span>.
        Tap anywhere to sprinkle love ✨
      </p>

      <div class="teddy-wrap">
        <img id="teddyGif" class="teddy" src="{TEDDY_GIF_URL}" alt="Teddy sending flying kisses" onerror="this.onerror=null;this.src='https://media1.tenor.com/m/2QbMJ6FR9TQAAAAd/loveyou-ted.gif';" />
      </div>

      <div class="stats">
        <div class="stat">
          <div class="stat-num" id="kisses">0</div>
          <div class="stat-label">Kisses caught</div>
        </div>
        <div class="stat">
          <div class="stat-num" id="hearts">0</div>
          <div class="stat-label">Hearts made</div>
        </div>
      </div>

      <div class="actions">
        <button id="openNote" class="btn primary">Open your surprise 💌</button>
        <button id="catchKiss" class="btn ghost">Catch a kiss 💋</button>
      </div>

      <p class="hint">Pro tip: try tapping the teddy 🐻 — it’s shy.</p>
    </section>

    <footer class="footer">
      <span>made with 💞</span>
      <button id="shareTip" class="linkish">how to share?</button>
    </footer>
  </main>

  <!-- Love Note Modal (LOCKED) -->
  <div id="modal" class="modal" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="modal-card">
      <button id="closeModal" class="icon-btn close" aria-label="Close">×</button>

      <h2>One tiny secret first… 🔒</h2>
      <p class="note" style="margin-top:8px">
        Enter your nickname (the one I call you) to unlock your surprise 💗
      </p>

      <div class="lock">
        <input id="pwd" class="pwd" type="text" inputmode="text" autocomplete="off"
               placeholder="Type your nickname…" />
        <button id="unlockBtn" class="btn primary">Unlock 💞</button>
      </div>

      <p id="pwdHint" class="tiny hintline">Hint: it’s short & cute 👀</p>

      <div id="noteArea" class="note-area" hidden>
        <h2 style="margin-top:14px">For <span id="herName2" class="accent"></span> 💕</h2>
        <p id="noteText" class="note"></p>

        <div class="modal-actions">
          <button id="confetti" class="btn primary">Celebrate us ✨</button>
          <button id="copyMsg" class="btn ghost">Copy sweet message</button>
        </div>

        <p class="tiny">(Unlocked ✅ Now smile for me 😌)</p>
      </div>
    </div>
  </div>

  <div id="toast" class="toast" aria-live="polite"></div>

  <!-- Optional: if you want music, host an mp3 and put its URL here -->
  <audio id="bgm" preload="auto" loop>
    <!-- example: <source src="/static/music.mp3" type="audio/mpeg" /> -->
  </audio>

  <script>
    // ====== Personalize from Python ======
    const GIRL_NAME = "Manya";
    const SECRET_PASSWORD = "meow";
    const NOTE_TEXT = "You have this unfair ability to distract me without even trying. Just like how I easily get distracted by cats."
    "Just a little reminder: you’re adorable, you’re loved, and you make my world loveable."
    "If I were there right now, I’d steal your attention, keep you close,"
    "and remind you exactly how adorable you are."
    "Come here 🧸💋"
    "Your teddy isn’t the only one sending kisses tonight.";
    // ==============================

    const el = (id) => document.getElementById(id);

    const herName = el("herName");
    const herName2 = el("herName2");
    const noteText = el("noteText");
    const kissesEl = el("kisses");
    const heartsEl = el("hearts");
    const teddy = el("teddyGif");
    const modal = el("modal");
    const toast = el("toast");
    const bgm = el("bgm");
    const musicBtn = el("musicBtn");

    let kisses = 0;
    let hearts = 0;
    let musicOn = false;

    function setTextSafe(node, text) {
      if (node) node.textContent = text;
    }

    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add("show");
      clearTimeout(showToast._t);
      showToast._t = setTimeout(() => toast.classList.remove("show"), 1400);
    }

    function rand(min, max) {
      return Math.random() * (max - min) + min;
    }

    function popEmoji(x, y, emoji) {
      const s = document.createElement("div");
      s.className = "pop";
      s.textContent = emoji;
      s.style.left = `${x}px`;
      s.style.top = `${y}px`;
      s.style.fontSize = `${rand(16, 28)}px`;
      s.style.transform = `translate(-50%, -50%) rotate(${rand(-18, 18)}deg)`;
      document.body.appendChild(s);
      setTimeout(() => s.remove(), 1400);
    }

    function sprinkleLove(x, y) {
      const emojis = ["💗", "💖", "✨", "💞", "💘", "🌸"];
      const n = Math.floor(rand(3, 7));
      for (let i = 0; i < n; i++) {
        setTimeout(() => {
          popEmoji(x + rand(-18, 18), y + rand(-18, 18), emojis[Math.floor(rand(0, emojis.length))]);
        }, i * 60);
      }
      hearts += 1;
      heartsEl.textContent = String(hearts);
    }

    function openModal() {
      modal.classList.add("show");
      modal.setAttribute("aria-hidden", "false");

      const pwd = el("pwd");
      const noteArea = el("noteArea");
      const hint = el("pwdHint");

      if (pwd) pwd.value = "";
      if (noteArea) noteArea.hidden = true;

      // 👇 start with no hint
      if (hint) hint.textContent = "";

      // 👇 delayed hint (2 seconds)
      setTimeout(() => {
        if (hint) {
          hint.textContent = "Hint: I call you this when you act extra cute 😼";
        }
    , 2000);

  showToast("Say the magic nickname… 🔒");
  setTimeout(() => pwd?.focus?.(), 50);
}


    function closeModal() {
      modal.classList.remove("show");
      modal.setAttribute("aria-hidden", "true");
    }

    function spawnKiss() {
      const k = document.createElement("button");
      k.className = "kiss";
      k.type = "button";
      k.setAttribute("aria-label", "Kiss token");
      k.textContent = "💋";

      const x = rand(60, window.innerWidth - 60);
      const y = rand(120, window.innerHeight - 120);
      k.style.left = `${x}px`;
      k.style.top = `${y}px`;

      const ttl = setTimeout(() => {
        k.remove();
        showToast("The kiss got shy 😳");
      }, 4000);

      k.addEventListener("click", () => {
        clearTimeout(ttl);
        kisses += 1;
        kissesEl.textContent = String(kisses);
        showToast("Kiss caught! 💋 +1");
        sprinkleLove(x, y);
        k.remove();
      });

      document.body.appendChild(k);
    }

    function tinyConfetti() {
      const burst = ["✨", "💖", "💗", "🌸", "💞", "🎀"];
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;

      for (let i = 0; i < 40; i++) {
        setTimeout(() => {
          popEmoji(cx + rand(-180, 180), cy + rand(-140, 140), burst[Math.floor(rand(0, burst.length))]);
        }, i * 18);
      }
      showToast("Yayyy 💞");
    }

    async function copySweetMessage() {
      const msg = `Hey ${GIRL_NAME} 💗\\n\\n${NOTE_TEXT}\\n\\n— from me 🧸`;
      try {
        await navigator.clipboard.writeText(msg);
        showToast("Copied! Send it to her 💌");
      } catch {
        showToast("Copy failed 😅 (browser blocked it)");
      }
    }

    function toggleMusic() {
      musicOn = !musicOn;
      if (musicOn) {
        bgm.volume = 0.35;
        bgm.play().catch(() => {
          showToast("Tap once, then press ♪ again 💗");
          musicOn = false;
        });
      } else {
        bgm.pause();
      }
      musicBtn.textContent = musicOn ? "♫" : "♪";
    }

    // Password unlock
    const unlockBtn = el("unlockBtn");
    const pwdInput = el("pwd");

    function normalize(s) {
      return String(s || "").trim().toLowerCase();
    }

    function wrongPasswordFeedback() {
      const card = modal.querySelector(".modal-card");
      card.classList.remove("shake");
      void card.offsetWidth;
      card.classList.add("shake");

      showToast("Oops 😳 try again");
      sprinkleLove(window.innerWidth/2, window.innerHeight/2);
    }

    function unlockNow() {
      const attempt = normalize(pwdInput.value);
      if (attempt === normalize(SECRET_PASSWORD)) {
        el("noteArea").hidden = false;
        el("pwdHint").textContent = "Unlocked ✅ you’re so cute 💗";
        showToast("Unlocked! 💞");

        tinyConfetti();
        teddy.classList.add("kiss");
        setTimeout(() => teddy.classList.remove("kiss"), 260);
      } else {
        el("pwdHint").textContent = "Hint: it’s the nickname I call you 😌";
        wrongPasswordFeedback();
      }
    }

    // Personalize content
    setTextSafe(herName, GIRL_NAME);
    setTextSafe(herName2, GIRL_NAME);
    setTextSafe(noteText, NOTE_TEXT);

    // Tap anywhere for hearts/sparkles (avoid buttons)
    window.addEventListener("pointerdown", (e) => {
      if (e.target.closest("button") || e.target.closest("input")) return;
      sprinkleLove(e.clientX, e.clientY);
    });

    // Teddy interactions
    teddy.addEventListener("click", (e) => {
      teddy.classList.add("kiss");
      sprinkleLove(e.clientX, e.clientY);
      showToast("Teddy sent you a kiss 😘");
      setTimeout(() => teddy.classList.remove("kiss"), 260);
    });
    teddy.addEventListener("mouseenter", () => teddy.classList.add("shy"));
    teddy.addEventListener("mouseleave", () => teddy.classList.remove("shy"));

    // Buttons
    el("openNote").addEventListener("click", openModal);
    el("closeModal").addEventListener("click", closeModal);
    modal.addEventListener("click", (e) => { if (e.target === modal) closeModal(); });

    el("catchKiss").addEventListener("click", () => {
      spawnKiss();
      showToast("Catch it fast! 💋");
    });

    el("confetti")?.addEventListener("click", tinyConfetti);
    el("copyMsg")?.addEventListener("click", copySweetMessage);

    el("shareTip").addEventListener("click", () => {
      showToast("Deploy this Flask app & share the URL 💗");
    });

    musicBtn.addEventListener("click", toggleMusic);

    unlockBtn.addEventListener("click", unlockNow);
    pwdInput.addEventListener("keydown", (e) => { if (e.key === "Enter") unlockNow(); });

    setTimeout(() => showToast("Tap anywhere ✨"), 700);
  </script>
</body>
</html>
"""

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    # For deployment platforms, use: gunicorn app:app
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
