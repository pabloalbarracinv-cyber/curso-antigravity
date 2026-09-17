import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_section = r'<!-- 3\. POSIBILIDADES -->\s*<section class="py-24 px-4 sm:px-8 max-w-7xl mx-auto border-t border-slate-200">.*?</section>'

new_section = '''<!-- 3. POSIBILIDADES (Contraste Oscuro) -->
  <section class="relative py-32 bg-[#0f172a] overflow-hidden">
    <!-- Fondo decorativo tipo grid/blueprint sutil -->
    <div class="absolute inset-0 opacity-[0.03]" style="background-image: linear-gradient(#ffffff 1px, transparent 1px), linear-gradient(90deg, #ffffff 1px, transparent 1px); background-size: 40px 40px;"></div>
    
    <div class="relative z-10 px-4 sm:px-8 max-w-7xl mx-auto">
      <div class="text-center max-w-3xl mx-auto mb-20">
        <span class="text-xs font-bold tracking-widest text-blue-400 uppercase mb-4 block">¿Qué puedes construir?</span>
        <h2 class="text-4xl md:text-5xl font-serif font-bold text-[#faf8f2] leading-tight mb-6">
          El límite es tu imaginación
        </h2>
        <p class="text-lg text-slate-400">
          Desde automatizar tareas cotidianas hasta desarrollar el próximo unicornio tecnológico. Este laboratorio te da la capacidad de crear a cualquier escala.
        </p>
      </div>

      <div class="grid lg:grid-cols-3 gap-8">
        
        <!-- Tarjeta 1: Operaciones -->
        <div class="group bg-white/5 border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
            <svg class="w-24 h-24 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </div>
          <h3 class="font-bold text-[#faf8f2] text-xl mb-6 relative z-10">Automatización Cotidiana</h3>
          <ul class="space-y-4 text-sm text-slate-400 relative z-10">
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Asistentes de WhatsApp con memoria</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Cotizadores dinámicos en tiempo real</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> CRMs integrados y páginas comerciales</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Sistemas de reservas automáticos</li>
          </ul>
        </div>

        <!-- Tarjeta 2: Software Especializado -->
        <div class="group bg-white/5 border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
            <svg class="w-24 h-24 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
          </div>
          <h3 class="font-bold text-[#faf8f2] text-xl mb-6 relative z-10">Software Corporativo</h3>
          <ul class="space-y-4 text-sm text-slate-400 relative z-10">
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Software especializado por área (RRHH, Logística)</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Dashboards de inteligencia de negocios</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Plataformas de investigación y desarrollo</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Herramientas internas a la medida</li>
          </ul>
        </div>

        <!-- Tarjeta 3: Impacto Masivo -->
        <div class="group bg-blue-900/20 border border-blue-500/30 rounded-3xl p-8 hover:bg-blue-900/40 transition-all duration-300 relative overflow-hidden shadow-[0_0_40px_rgba(37,99,235,0.1)]">
          <div class="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity text-blue-400">
            <svg class="w-24 h-24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M14 10l-2 1m0 0l-2-1m2 1v2.5M20 7l-2 1m2-1l-2-1m2 1v2.5M14 4l-2-1-2 1M4 7l2-1M4 7l2 1M4 7v2.5M12 21l-2-1m2 1l2-1m-2 1v-2.5M6 18l-2-1v-2.5M18 18l2-1v-2.5"/></svg>
          </div>
          <h3 class="font-bold text-[#faf8f2] text-xl mb-6 relative z-10">Plataformas Disruptivas</h3>
          <ul class="space-y-4 text-sm text-slate-300 relative z-10 font-medium">
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> "Tu propio Uber" o Marketplaces bidireccionales</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Startups SaaS impulsadas por IA</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Aplicaciones web y móviles complejas</li>
            <li class="flex items-start gap-3"><span class="text-blue-400 mt-0.5">✦</span> Modelos de ciencia de datos aplicada</li>
          </ul>
        </div>
      </div>

      <!-- Manuscrito -->
      <div class="mt-16 text-center font-handwriting text-3xl text-[#faf8f2] opacity-80 -rotate-2">
        "Tu proyecto no tiene que parecerse a ninguno de estos.<br>
        <span class="text-blue-400">La idea es que construyas el tuyo.</span>"
      </div>
    </div>
  </section>'''

html = re.sub(old_section, new_section, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
