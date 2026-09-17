import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('<script>')
if len(parts) > 1:
    before = parts[0]
    after = parts[1].split('</script>')[1]
    
    good_script = """<script>
    function openModal() {
      document.getElementById('reservation-modal').classList.remove('hidden');
    }
    function closeModal() {
      document.getElementById('reservation-modal').classList.add('hidden');
    }
    function handleFormSubmit(e) {
      e.preventDefault();
      const form = e.target;
      const btn = form.querySelector('button[type="submit"]');
      
      const nombre = document.getElementById('f_nombre').value;
      const correo = document.getElementById('f_correo').value;
      const cod = document.getElementById('f_cod').value;
      const tel = document.getElementById('f_tel').value;
      const perfil = document.getElementById('f_perfil').value;
      const pais = document.getElementById('f_pais').value;
      
      const mensaje = `¡Hola! Quiero aplicar al Laboratorio Antigravity. Mis datos son:\\n\\n*Nombre:* ${nombre}\\n*Correo:* ${correo}\\n*WhatsApp:* ${cod} ${tel}\\n*Perfil:* ${perfil}\\n*País:* ${pais}`;
      const whatsappUrl = `https://wa.me/573138544974?text=${encodeURIComponent(mensaje)}`;
      
      const originalText = btn.innerHTML;
      btn.innerHTML = `<span class="animate-spin inline-block w-5 h-5 border-2 border-white/30 border-t-white rounded-full"></span> <span>Procesando...</span>`;
      btn.disabled = true;
      
      setTimeout(() => {
        btn.innerHTML = `<span>¡Abriendo WhatsApp!</span> <svg class="w-5 h-5 ml-1 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>`;
        btn.classList.replace('bg-blue-800', 'bg-emerald-600');
        setTimeout(() => {
          window.open(whatsappUrl, '_blank');
          closeModal();
          form.reset();
          btn.innerHTML = originalText;
          btn.classList.replace('bg-emerald-600', 'bg-blue-800');
          btn.disabled = false;
        }, 1000);
      }, 800);
    }
  </script>"""
    
    new_html = before + good_script + after
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
