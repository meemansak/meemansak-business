const canonical='https://meemansak.github.io/business-card/';
document.querySelectorAll('[data-share]').forEach(button=>button.addEventListener('click',async()=>{
 const status=document.getElementById('status');
 try{if(navigator.share){await navigator.share({title:'Meemansak Bharti',text:'Wedditors · Capture Camera Productions — connect with Meemansak Bharti',url:canonical});status.textContent='';}else{await navigator.clipboard.writeText(canonical);status.textContent='Link copied. Ready to share.';}}catch(error){if(error.name!=='AbortError'){status.textContent='Copy this link to share: '+canonical;}}
}));

const nameHeading=document.querySelector('h1');
nameHeading.addEventListener('pointermove',event=>{const bounds=nameHeading.getBoundingClientRect();nameHeading.style.setProperty('--glow-x',((event.clientX-bounds.left)/bounds.width*100)+'%');nameHeading.style.setProperty('--glow-y',((event.clientY-bounds.top)/bounds.height*100)+'%');});

