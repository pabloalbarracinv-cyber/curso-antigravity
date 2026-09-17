import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Floating WhatsApp Button
html = html.replace('href="https://wa.me/numerodetelefono"', 'href="https://wa.me/573138544974?text=Hola,%20tengo%20una%20duda%20sobre%20el%20Laboratorio%20Antigravity"')

# 2. Update Modal Form
old_modal = r'<!-- MODAL DE RESERVA \(FORMULARIO\) -->.*?<script>'
new_modal = '''<!-- MODAL DE RESERVA (FORMULARIO) -->
  <!-- ========================================================================= -->
  <div id="reservation-modal" class="fixed inset-0 z-[100] hidden">
    <!-- Fondo oscuro -->
    <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" onclick="closeModal()"></div>
    
    <!-- Contenedor del Modal -->
    <div class="absolute inset-0 flex items-center justify-center p-4">
      <div class="bg-white w-full max-w-md rounded-3xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        
        <div class="bg-blue-800 p-6 text-white relative">
          <button onclick="closeModal()" class="absolute top-4 right-4 text-white/70 hover:text-white transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
          <h3 class="text-2xl font-serif font-bold">Aplica al Laboratorio</h3>
          <p class="text-blue-100 text-sm mt-1">
            Completa tus datos para enviarlos por WhatsApp.
          </p>
        </div>

        <div class="p-6 overflow-y-auto">
          <form id="lead-form" onsubmit="handleFormSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Nombre Completo</label>
              <input id="f_nombre" type="text" required placeholder="Tu nombre y apellido" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-50">
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Correo Electrónico</label>
              <input id="f_correo" type="email" required placeholder="tunombre@correo.com" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-50">
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">WhatsApp</label>
              <div class="flex">
                <select id="f_cod" class="w-24 px-2 py-2.5 rounded-l-xl border border-r-0 border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-100">
                  <option value="+57">🇨🇴 +57</option>
                  <option value="+52">🇲🇽 +52</option>
                  <option value="+1">🇺🇸 +1</option>
                  <option value="+34">🇪🇸 +34</option>
                  <option value="+54">🇦🇷 +54</option>
                  <option value="+56">🇨🇱 +56</option>
                  <option value="+51">🇵🇪 +51</option>
                  <option value="">Otro</option>
                </select>
                <input id="f_tel" type="tel" required placeholder="Número telefónico" class="w-full px-4 py-2.5 rounded-r-xl border border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-50">
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">Tu Perfil</label>
              <select id="f_perfil" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-50">
                <option value="">Selecciona tu perfil...</option>
                <option value="Empresario solo">Empresario (Solo)</option>
                <option value="Empresario con equipo">Empresario (Con Equipo)</option>
                <option value="Emprendedor">Emprendedor</option>
                <option value="Empleado / Autodidacta">Empleado / Autodidacta</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">País</label>
              <input id="f_pais" type="text" required placeholder="Ej. Colombia, México, España" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:border-blue-500 bg-slate-50">
            </div>

            <button type="submit" class="w-full py-4 rounded-xl bg-blue-800 hover:bg-blue-900 text-white font-bold text-sm shadow-xl transition-all flex items-center justify-center space-x-2 mt-4">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
              <span>Enviar aplicación por WhatsApp</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>

  <script>'''

html = re.sub(old_modal, new_modal, html, flags=re.DOTALL)

# 3. Update the script block containing handleFormSubmit
old_script = r'function handleFormSubmit\(e\).*?\}'
new_script = '''function handleFormSubmit(e) {
      e.preventDefault();
      const form = e.target;
      const btn = form.querySelector('button[type="submit"]');
      
      const nombre = document.getElementById('f_nombre').value;
      const correo = document.getElementById('f_correo').value;
      const cod = document.getElementById('f_cod').value;
      const tel = document.getElementById('f_tel').value;
      const perfil = document.getElementById('f_perfil').value;
      const pais = document.getElementById('f_pais').value;
      
      const mensaje = ¡Hola! Quiero aplicar al Laboratorio Antigravity. Mis datos son:\n\n*Nombre:* \n*Correo:* \n*WhatsApp:*  \n*Perfil:* \n*País:* ;
      const whatsappUrl = https://wa.me/573138544974?text=;
      
      const originalText = btn.innerHTML;
      btn.innerHTML = <span class="animate-spin inline-block w-5 h-5 border-2 border-white/30 border-t-white rounded-full"></span> <span>Procesando...</span>;
      btn.disabled = true;
      
      setTimeout(() => {
        btn.innerHTML = <span>¡Abriendo WhatsApp!</span> <svg class="w-5 h-5 ml-1 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>;
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
    }'''

html = re.sub(old_script, new_script, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
