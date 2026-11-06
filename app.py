import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vision Media Controller | PRCV",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

      html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0f19 !important;
        color: #e5e7eb !important;
        font-family: 'IBM Plex Sans', sans-serif !important;
      }
      [data-testid="stHeader"] {
        background: rgba(11, 15, 25, 0.72) !important;
        backdrop-filter: blur(12px);
      }
      [data-testid="stToolbar"] { visibility: hidden; }
      [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0b0f19 100%) !important;
        border-right: 1px solid #1f2937;
      }
      [data-testid="stSidebar"] * { color: #e5e7eb !important; }
      .block-container { padding-top: 1.1rem; max-width: 1480px; }

      .studio-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 58%, #111827 100%);
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 22px 26px 20px;
        margin-bottom: 8px;
        position: relative;
        overflow: hidden;
      }
      .studio-header::before {
        content: "";
        position: absolute;
        inset: 0 auto auto 0;
        width: 8px;
        height: 100%;
        background: #a3e635;
      }
      .studio-kicker {
        color: #a3e635;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        margin: 0 0 8px 0;
      }
      .studio-header h1 {
        color: #f8fafc;
        font-size: 1.72rem;
        line-height: 1.2;
        margin: 0 0 8px 0;
        font-weight: 700;
      }
      .studio-meta {
        color: #94a3b8;
        font-size: 14px;
        margin: 0;
      }
      .studio-meta b { color: #e2e8f0; }
      .pill-row { margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap; }
      .pill {
        background: rgba(163, 230, 53, 0.08);
        border: 1px solid rgba(163, 230, 53, 0.28);
        color: #a3e635;
        border-radius: 999px;
        padding: 4px 10px;
        font-size: 11px;
        font-family: 'IBM Plex Mono', monospace;
        letter-spacing: 0.04em;
      }
      .panel-title {
        font-size: 12px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #a3e635;
        font-family: 'IBM Plex Mono', monospace;
        margin: 4px 0 12px 0;
      }
      .cheat-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 10px;
      }
      .cheat-card h4 {
        margin: 0 0 4px 0;
        color: #f1f5f9;
        font-size: 14px;
      }
      .cheat-card p {
        margin: 0;
        color: #94a3b8;
        font-size: 12.5px;
        line-height: 1.45;
      }
      .kbd {
        display: inline-block;
        background: #0f172a;
        border: 1px solid #334155;
        color: #a3e635;
        border-radius: 6px;
        padding: 1px 7px;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
      }
      .gauge-wrap {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 10px;
      }
      .gauge-label {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #94a3b8;
        margin-bottom: 6px;
        font-family: 'IBM Plex Mono', monospace;
      }
      .gauge-track {
        height: 7px;
        background: #0f172a;
        border-radius: 999px;
        overflow: hidden;
      }
      .gauge-fill {
        height: 100%;
        width: 72%;
        background: linear-gradient(90deg, #65a30d, #a3e635);
        border-radius: 999px;
      }
      .gauge-fill.alt { width: 38%; background: linear-gradient(90deg, #22d3ee, #a3e635); }
      .footnote {
        color: #64748b;
        font-size: 11.5px;
        line-height: 1.5;
      }
      [data-testid="stExpander"] {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="studio-header">
      <p class="studio-kicker">Pattern Recognition &amp; Computer Vision · CSE-B · 7th Semester</p>
      <h1>Vision-Based Hand Gesture Media Controller</h1>
      <p class="studio-meta">
        Author: <b>Kuthadi Ratnakshaya</b> &nbsp;·&nbsp; Enrollment No:
        <b>10117702723</b> &nbsp;·&nbsp; Programme: <b>CSE-B</b> &nbsp;·&nbsp;
        Term: <b>7th Semester</b>
      </p>
      <div class="pill-row">
        <span class="pill">MediaPipe Hands · 21 Landmarks</span>
        <span class="pill">Client-side WebGL</span>
        <span class="pill">Zero backend latency</span>
        <span class="pill">Big Buck Bunny demo reel</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown('<p class="panel-title">Control Panel</p>', unsafe_allow_html=True)
    st.markdown("### Gesture Cheatsheet")
    st.markdown(
        """
        <div class="cheat-card">
          <h4>Pinch · Play / Pause</h4>
          <p>2D Euclidean distance between <span class="kbd">LM 4</span> Thumb Tip
          and <span class="kbd">LM 8</span> Index Tip. Fire when
          <span class="kbd">d &lt; 0.05</span> with a <span class="kbd">600 ms</span>
          debounce cooldown.</p>
        </div>
        <div class="cheat-card">
          <h4>Vertical Y-Axis · Volume</h4>
          <p>Index Tip <span class="kbd">LM 8</span> Y-coordinate is mapped to
          <span class="kbd">mediaPlayer.volume</span>. Raise the hand to increase
          level; lower it to fade down. EMA smoothing keeps the fader studio-quiet.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("### Real-time Telemetry")
    st.markdown(
        """
        <div class="gauge-wrap">
          <div class="gauge-label"><span>TARGET THROUGHPUT</span><span>30+ FPS</span></div>
          <div class="gauge-track"><div class="gauge-fill"></div></div>
        </div>
        <div class="gauge-wrap">
          <div class="gauge-label"><span>INFERENCE BUDGET</span><span>&lt; 15 ms</span></div>
          <div class="gauge-track"><div class="gauge-fill alt"></div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.metric("Landmark graph", "21 / 21")
    st.metric("Pinch threshold", "0.05 NDC")
    st.metric("Debounce window", "600 ms")
    st.caption("Live FPS, pinch distance, and volume are streamed inside the capture studio below.")
    st.markdown("---")
    st.markdown(
        '<p class="footnote">Grant camera permission when the browser prompts. '
        "All inference stays on-device via WebGL shaders — frames never leave this tab.</p>",
        unsafe_allow_html=True,
    )

ENGINE_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #0b0f19;
      --card: #1e293b;
      --line: #334155;
      --lime: #a3e635;
      --text: #e5e7eb;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; }
    html, body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--text);
      font-family: 'IBM Plex Sans', system-ui, sans-serif;
    }
    .studio {
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.9fr);
      gap: 14px;
      padding: 4px;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 16px;
      overflow: hidden;
    }
    .card-hd {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 14px;
      border-bottom: 1px solid var(--line);
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    .live-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--lime);
      box-shadow: 0 0 0 0 rgba(163, 230, 53, 0.7);
      animation: pulse 1.6s infinite;
      display: inline-block;
      margin-right: 8px;
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(163, 230, 53, 0.55); }
      70% { box-shadow: 0 0 0 8px rgba(163, 230, 53, 0); }
      100% { box-shadow: 0 0 0 0 rgba(163, 230, 53, 0); }
    }
    .stage {
      position: relative;
      width: 100%;
      background: #000;
      aspect-ratio: 16 / 11;
      min-height: 420px;
    }
    #webcam, #overlay {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scaleX(-1);
    }
    #overlay { z-index: 2; }
    .player-wrap { padding: 12px; }
    #demo_player {
      width: 100%;
      border-radius: 10px;
      background: #000;
      outline: none;
    }
    .badges {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      padding: 0 12px 12px;
    }
    .badge {
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      border: 1px solid var(--line);
      background: #0f172a;
      color: var(--muted);
    }
    .badge.active { color: var(--lime); border-color: rgba(163, 230, 53, 0.45); }
    .badge.warn { color: #fbbf24; border-color: rgba(251, 191, 36, 0.4); }
    .telemetry {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      padding: 12px;
    }
    .metric {
      background: #0f172a;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px;
    }
    .metric span {
      display: block;
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    .metric strong {
      display: block;
      margin-top: 6px;
      font-size: 22px;
      color: var(--lime);
      font-variant-numeric: tabular-nums;
    }
    .bar {
      margin-top: 10px;
      height: 6px;
      background: #1e293b;
      border-radius: 999px;
      overflow: hidden;
    }
    .bar > i {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #65a30d, #a3e635);
    }
    .log {
      margin: 0 12px 12px;
      background: #0b0f19;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 10px 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 12px;
      color: var(--lime);
      min-height: 44px;
    }
    .hint {
      padding: 0 12px 14px;
      color: var(--muted);
      font-size: 12.5px;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <div class="studio">
    <section class="card">
      <div class="card-hd">
        <span><i class="live-dot"></i>Capture · MediaPipe Hands WebGL</span>
        <span id="camState">BOOTING</span>
      </div>
      <div class="stage">
        <video id="webcam" autoplay playsinline muted></video>
        <canvas id="overlay"></canvas>
      </div>
      <div class="badges">
        <div class="badge" id="badgePlay">PAUSED</div>
        <div class="badge" id="badgeVol">VOLUME 70%</div>
        <div class="badge" id="badgeHand">NO HAND</div>
      </div>
    </section>

    <section class="card">
      <div class="card-hd"><span>Program Feed · Big Buck Bunny</span><span>HTML5</span></div>
      <div class="player-wrap">
        <video id="demo_player" controls preload="metadata" playsinline>
          <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="telemetry">
        <div class="metric">
          <span>Throughput</span>
          <strong id="fpsVal">00 FPS</strong>
          <div class="bar"><i id="fpsBar"></i></div>
        </div>
        <div class="metric">
          <span>Pinch Distance</span>
          <strong id="pinchVal">—</strong>
          <div class="bar"><i id="pinchBar"></i></div>
        </div>
        <div class="metric">
          <span>Index Y (LM 8)</span>
          <strong id="yVal">—</strong>
          <div class="bar"><i id="yBar"></i></div>
        </div>
        <div class="metric">
          <span>Cooldown</span>
          <strong id="cdVal">READY</strong>
          <div class="bar"><i id="cdBar"></i></div>
        </div>
      </div>
      <div class="log" id="status">Status: Initializing MediaPipe Hands…</div>
      <p class="hint">
        Pinch thumb + index to toggle playback. Move the index fingertip vertically
        to ride volume. Landmarks 0–20 are projected onto the overlay canvas each frame.
      </p>
    </section>
  </div>

  <script>
    const HAND_CONNECTIONS = [
      [0, 1], [1, 2], [2, 3], [3, 4],
      [0, 5], [5, 6], [6, 7], [7, 8],
      [5, 9], [9, 10], [10, 11], [11, 12],
      [9, 13], [13, 14], [14, 15], [15, 16],
      [13, 17], [17, 18], [18, 19], [19, 20],
      [0, 17], [5, 17]
    ];

    const PINCH_THRESHOLD = 0.05;
    const DEBOUNCE_MS = 600;
    const EMA_ALPHA = 0.22;

    const videoElement = document.getElementById('webcam');
    const canvasElement = document.getElementById('overlay');
    const canvasCtx = canvasElement.getContext('2d');
    const mediaPlayer = document.getElementById('demo_player');
    const statusDiv = document.getElementById('status');
    const badgePlay = document.getElementById('badgePlay');
    const badgeVol = document.getElementById('badgeVol');
    const badgeHand = document.getElementById('badgeHand');
    const camState = document.getElementById('camState');

    let lastActionTime = 0;
    let smoothedVolume = 0.7;
    let frames = 0;
    let fps = 0;
    let fpsStamp = performance.now();
    mediaPlayer.volume = smoothedVolume;

    function setStatus(message) {
      statusDiv.textContent = message;
    }

    function updatePlaybackBadge() {
      const playing = !mediaPlayer.paused;
      badgePlay.textContent = playing ? 'PLAYING' : 'PAUSED';
      badgePlay.classList.toggle('active', playing);
      badgePlay.classList.toggle('warn', !playing);
    }

    function updateVolumeBadge(vol) {
      const pct = Math.round(vol * 100);
      badgeVol.textContent = 'VOLUME ' + pct + '%';
      badgeVol.classList.add('active');
    }

    mediaPlayer.addEventListener('play', updatePlaybackBadge);
    mediaPlayer.addEventListener('pause', updatePlaybackBadge);
    updatePlaybackBadge();
    updateVolumeBadge(smoothedVolume);

    function landmarkXY(landmark, width, height) {
      return [landmark.x * width, landmark.y * height];
    }

    function drawSkeleton(landmarks, width, height) {
      canvasCtx.lineWidth = 3;
      canvasCtx.strokeStyle = '#a3e635';
      canvasCtx.lineCap = 'round';
      for (const [a, b] of HAND_CONNECTIONS) {
        const [x1, y1] = landmarkXY(landmarks[a], width, height);
        const [x2, y2] = landmarkXY(landmarks[b], width, height);
        canvasCtx.beginPath();
        canvasCtx.moveTo(x1, y1);
        canvasCtx.lineTo(x2, y2);
        canvasCtx.stroke();
      }
      landmarks.forEach((lm, idx) => {
        const [x, y] = landmarkXY(lm, width, height);
        canvasCtx.beginPath();
        canvasCtx.arc(x, y, idx === 4 || idx === 8 ? 7 : 4, 0, Math.PI * 2);
        canvasCtx.fillStyle = (idx === 4 || idx === 8) ? '#f8fafc' : '#22d3ee';
        canvasCtx.fill();
        canvasCtx.strokeStyle = '#0b0f19';
        canvasCtx.lineWidth = 1.5;
        canvasCtx.stroke();
      });
    }

    function onResults(results) {
      const width = videoElement.videoWidth || 640;
      const height = videoElement.videoHeight || 480;
      if (canvasElement.width !== width) canvasElement.width = width;
      if (canvasElement.height !== height) canvasElement.height = height;

      canvasCtx.save();
      canvasCtx.clearRect(0, 0, width, height);

      frames += 1;
      const nowPerf = performance.now();
      if (nowPerf - fpsStamp >= 1000) {
        fps = frames;
        frames = 0;
        fpsStamp = nowPerf;
        document.getElementById('fpsVal').textContent = String(fps).padStart(2, '0') + ' FPS';
        document.getElementById('fpsBar').style.width = Math.min(100, (fps / 30) * 100) + '%';
      }

      const now = Date.now();
      const cooldownLeft = Math.max(0, DEBOUNCE_MS - (now - lastActionTime));
      document.getElementById('cdVal').textContent = cooldownLeft > 0 ? cooldownLeft + ' ms' : 'READY';
      document.getElementById('cdBar').style.width = ((DEBOUNCE_MS - cooldownLeft) / DEBOUNCE_MS) * 100 + '%';

      if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
        const landmarks = results.multiHandLandmarks[0];
        drawSkeleton(landmarks, width, height);

        const thumb = landmarks[4];
        const index = landmarks[8];
        const distance = Math.hypot(index.x - thumb.x, index.y - thumb.y);

        badgeHand.textContent = 'HAND LOCKED';
        badgeHand.classList.add('active');
        document.getElementById('pinchVal').textContent = distance.toFixed(3);
        document.getElementById('pinchBar').style.width = Math.min(100, (distance / 0.25) * 100) + '%';
        document.getElementById('yVal').textContent = index.y.toFixed(3);
        document.getElementById('yBar').style.width = Math.round((1 - index.y) * 100) + '%';

        const targetVolume = Math.max(0, Math.min(1, 1 - index.y));
        smoothedVolume = EMA_ALPHA * targetVolume + (1 - EMA_ALPHA) * smoothedVolume;
        mediaPlayer.volume = smoothedVolume;
        updateVolumeBadge(smoothedVolume);

        if (distance < PINCH_THRESHOLD && (now - lastActionTime > DEBOUNCE_MS)) {
          if (mediaPlayer.paused) {
            mediaPlayer.play().catch(() => {});
            setStatus('ACTION DETECTED: PLAY (Pinch d=' + distance.toFixed(3) + ')');
          } else {
            mediaPlayer.pause();
            setStatus('ACTION DETECTED: PAUSE (Pinch d=' + distance.toFixed(3) + ')');
          }
          lastActionTime = now;
          updatePlaybackBadge();
        } else {
          const playLabel = mediaPlayer.paused ? 'PAUSED' : 'PLAYING';
          setStatus(
            'TRACKING ACTIVE | ' + playLabel +
            ' | VOLUME ' + Math.round(smoothedVolume * 100) + '%' +
            ' | pinch=' + distance.toFixed(3)
          );
        }
      } else {
        badgeHand.textContent = 'NO HAND';
        badgeHand.classList.remove('active');
        document.getElementById('pinchVal').textContent = '—';
        document.getElementById('yVal').textContent = '—';
        document.getElementById('pinchBar').style.width = '0%';
        document.getElementById('yBar').style.width = '0%';
        setStatus('Status: Looking for hands…');
      }

      canvasCtx.restore();
    }

    function bootHands() {
      if (typeof Hands === 'undefined') {
        setStatus('Error: MediaPipe Hands failed to load from CDN.');
        camState.textContent = 'CDN ERROR';
        return;
      }

      const hands = new Hands({
        locateFile: (file) => 'https://cdn.jsdelivr.net/npm/@mediapipe/hands/' + file
      });
      hands.setOptions({
        maxNumHands: 1,
        modelComplexity: 1,
        minDetectionConfidence: 0.7,
        minTrackingConfidence: 0.7
      });
      hands.onResults(onResults);

      const startWithCameraUtils = () => {
        if (typeof Camera === 'undefined') return false;
        const camera = new Camera(videoElement, {
          onFrame: async () => { await hands.send({ image: videoElement }); },
          width: 640,
          height: 480
        });
        camera.start();
        camState.textContent = 'LIVE';
        setStatus('Status: Camera pipeline live. Present a hand to the lens.');
        return true;
      };

      if (startWithCameraUtils()) return;

      navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480, facingMode: 'user' },
        audio: false
      }).then((stream) => {
        videoElement.srcObject = stream;
        camState.textContent = 'LIVE';
        const loop = async () => {
          if (videoElement.readyState >= 2) {
            await hands.send({ image: videoElement });
          }
          requestAnimationFrame(loop);
        };
        videoElement.addEventListener('loadeddata', loop, { once: true });
        setStatus('Status: Camera pipeline live. Present a hand to the lens.');
      }).catch((err) => {
        camState.textContent = 'NO CAMERA';
        setStatus('Camera blocked: ' + err.message + '. Allow webcam access and reload.');
      });
    }

    bootHands();
  </script>
</body>
</html>
"""

components.html(ENGINE_HTML, height=820, scrolling=False)

with st.expander("System architecture & examiner notes", expanded=False):
    st.markdown(
        r"""
**Client-side execution pipeline**

1. **HTML5 capture** — webcam frames are acquired in-browser (`Camera` from `@mediapipe/camera_utils`).
2. **BlazePalm + hand landmark network** — MediaPipe Hands regresses 21 normalized 3-D landmarks per frame on WebGL.
3. **Pinch heuristic** — \( d_p = \sqrt{(x_8-x_4)^2 + (y_8-y_4)^2} \). A falling edge below \(0.05\) with a 600 ms refractory period toggles play/pause.
4. **Volume fader** — index-tip \(y_8\) is inverted and exponentially smoothed onto `HTMLMediaElement.volume`.
5. **Overlay compositor** — landmarks and skeleton connectors are painted on a canvas locked to the camera texture.

**Privacy** — inference never leaves the tab. There is no Python OpenCV loop, no uploaded frames, and no server-side model host. That is why `packages.txt` only lists a Mesa GL stub for Streamlit Cloud compatibility and `requirements.txt` is Streamlit-only.
        """
    )
