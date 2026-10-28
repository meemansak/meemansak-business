from pathlib import Path
p=Path(__file__).parent
f=p/'dist/index.html';s=f.read_text(encoding='utf-8')
s=s.replace('<a href="#" class="monogram" aria-label="Meemansak Bharti home">mb<span>.</span></a>','')
for arrow in [' <span>↗</span>',' <span>↓</span>']:s=s.replace(arrow,'')
s=s.replace('<p class="eyebrow">MEEMANSAK BHARTI</p>','<p class="eyebrow">PRODUCTION · POST-PRODUCTION · TECHNOLOGY</p>')
s=s.replace('<em>Bharti.</em>','<span>Bharti</span>')
s=s.replace('</h1><div class="roles">','</h1><p class="bio">Creative operations, production &amp; post-production.<br>Exploring what’s next with AI automation and software.</p><div class="roles">')
s=s.replace('<h2>Wedditors</h2>','<h2>Wedditors</h2><p class="description">Post-production agency</p>')
s=s.replace('<h2>Capture Camera <small>Productions</small></h2>','<h2>Capture Camera Productions</h2><p class="description">Commercial production &amp; post-production</p>')
s=s.replace('<h2>Personally</h2>','<h2>Meemansak</h2><p class="description">AI automation &amp; software in the making.<br>A few new things are taking shape.</p>')
f.write_text(s,encoding='utf-8')
f=p/'dist/style.css';s=f.read_text(encoding='utf-8');s+='''
/* Refined typography and quiet, interactive light. */
header{justify-content:space-between;height:88px}
h1,h2,.footer-title{font-style:normal;font-weight:400}
h1{position:relative;isolation:isolate;cursor:default;transition:text-shadow .5s ease;color:var(--green);margin-bottom:18px}
h1>span{display:block}
h1::before{content:"";position:absolute;inset:-35px;z-index:-1;background:radial-gradient(ellipse at var(--glow-x,50%) var(--glow-y,50%),#c7b57555,transparent 66%);filter:blur(18px);opacity:0;transition:opacity .5s ease;pointer-events:none}
h1:hover{text-shadow:0 0 20px #aa945c55,0 0 48px #b7a56b55}
h1:hover::before{opacity:1}
.bio{font-size:11px;line-height:1.9;color:var(--muted);margin:0 0 20px}
.hero{padding:44px 0;gap:62px}.portrait{height:410px}
.description{font-size:10px;line-height:1.8;color:var(--muted);margin:0 0 8px}
h2{font-size:25px}.brand>a{font-size:10px}.qr img{width:120px;height:120px}
.footer-title{font-size:22px}.button{justify-content:center;min-width:127px}
@media(max-width:850px){.hero{gap:36px}h1{font-size:51px}h2{font-size:22px}}
@media(max-width:600px){header{height:72px}.hero{gap:27px;padding:28px 0}.portrait{height:300px}h1{font-size:clamp(40px,12.8vw,58px)}h1 br{display:none}.eyebrow{font-size:6px;letter-spacing:1.55px}.bio{font-size:10px}h2{font-size:25px}.qr img{width:105px;height:105px}.footer-title{font-size:19px}.button{min-width:0}footer{gap:14px}}
@media(prefers-reduced-motion:reduce){h1,h1::before{transition:none}h1::before{filter:none}}
''';f.write_text(s,encoding='utf-8')
f=p/'dist/app.js';s=f.read_text(encoding='utf-8');s+='''
const nameHeading=document.querySelector('h1');
nameHeading.addEventListener('pointermove',event=>{const bounds=nameHeading.getBoundingClientRect();nameHeading.style.setProperty('--glow-x',((event.clientX-bounds.left)/bounds.width*100)+'%');nameHeading.style.setProperty('--glow-y',((event.clientY-bounds.top)/bounds.height*100)+'%');});
''';f.write_text(s,encoding='utf-8')
