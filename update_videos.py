import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tools = ['Gemini', 'Claude', 'OpenAI', 'Google', 'Omni', 'Stitch', 'Labs', 'Spark', 'Gems', 'Nano Banana', 'NoteBook', 'Deep Research', 'Workspace', 'Antigravity', 'GitHub', 'Vercel', 'Supabase']

tools_html = ''
for tool in tools:
    tools_html += f'''
            <div class="px-5 py-2.5 bg-white border border-slate-200 rounded-xl shadow-sm flex items-center gap-2.5 hover:border-blue-400 hover:-translate-y-1 transition-all cursor-default">
              <div class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></div>
              <span class="text-slate-700 font-bold text-sm">{tool}</span>
            </div>'''

tools_html += f'''
            <div class="px-5 py-2.5 bg-blue-50 border border-blue-200 rounded-xl shadow-sm flex items-center gap-2.5 cursor-default">
              <span class="text-blue-800 font-bold text-sm">...y más</span>
            </div>'''

new_sections = f'''
  <!-- HERRAMIENTAS -->
  <section class="py-24 bg-[#faf8f2] border-b border-slate-200">
    <div class="max-w-5xl mx-auto px-4 sm:px-8 text-center">
      <span class="text-xs font-bold tracking-widest text-slate-500 uppercase mb-4 block">El Ecosistema</span>
      <h2 class="text-3xl md:text-4xl font-serif font-bold text-slate-900 mb-12">
        Herramientas que dominarás
      </h2>
      
      <div class="flex flex-wrap justify-center gap-4">
        {tools_html}
      </div>
    </div>
  </section>

  <!-- VIDEOS (CARRUSEL) -->
  <section class="py-24 bg-[#f4efe6] border-b border-slate-200 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
        <div>
          <span class="text-xs font-bold tracking-widest text-slate-500 uppercase mb-4 block">En Acción</span>
          <h2 class="text-3xl md:text-4xl font-serif font-bold text-slate-900">
            El laboratorio por dentro
          </h2>
        </div>
        <div class="flex items-center gap-2 text-blue-800 bg-blue-100/50 px-4 py-2 rounded-full border border-blue-200 w-fit">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          <span class="text-xs font-bold uppercase tracking-wider">Desliza para ver</span>
        </div>
      </div>
      
      <!-- Contenedor Carrusel -->
      <div class="flex overflow-x-auto gap-6 pb-8 snap-x snap-mandatory [&::-webkit-scrollbar]:hidden" style="scrollbar-width: none;">
        
        <!-- Video 1 -->
        <div class="min-w-[85vw] md:min-w-[450px] max-w-[500px] flex-shrink-0 snap-center bg-white rounded-3xl p-5 shadow-xl border border-slate-200">
          <div class="aspect-video w-full rounded-2xl overflow-hidden bg-slate-900 mb-5 relative shadow-inner">
            <iframe width="100%" height="100%" src="https://www.youtube.com/embed/xlALU-kyFdw" title="Video de muestra" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          </div>
          <h3 class="font-bold text-slate-900 text-lg">Construcción en Tiempo Real</h3>
          <p class="text-sm text-slate-500 mt-2 leading-relaxed">Observa cómo transformamos instrucciones en español en una aplicación completamente funcional en cuestión de minutos.</p>
        </div>

        <!-- Video 2 -->
        <div class="min-w-[85vw] md:min-w-[450px] max-w-[500px] flex-shrink-0 snap-center bg-white rounded-3xl p-5 shadow-xl border border-slate-200">
          <div class="aspect-video w-full rounded-2xl overflow-hidden bg-slate-900 mb-5 relative shadow-inner">
            <iframe width="100%" height="100%" src="https://www.youtube.com/embed/b2qw3rDNX0Q" title="Video de muestra" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          </div>
          <h3 class="font-bold text-slate-900 text-lg">El Poder de la Integración</h3>
          <p class="text-sm text-slate-500 mt-2 leading-relaxed">Descubre el flujo de trabajo completo: desde la conexión inteligente a la base de datos hasta el despliegue automático en la nube.</p>
        </div>

        <!-- Video 3 -->
        <div class="min-w-[85vw] md:min-w-[450px] max-w-[500px] flex-shrink-0 snap-center bg-white rounded-3xl p-5 shadow-xl border border-slate-200">
          <div class="aspect-video w-full rounded-2xl overflow-hidden bg-slate-900 mb-5 relative shadow-inner">
            <iframe width="100%" height="100%" src="https://www.youtube.com/embed/SzmfH4P00vI?start=18" title="Video de muestra" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          </div>
          <h3 class="font-bold text-slate-900 text-lg">Agentes en Acción</h3>
          <p class="text-sm text-slate-500 mt-2 leading-relaxed">Un vistazo exclusivo a cómo los agentes autónomos de Antigravity resuelven problemas lógicos complejos paso a paso.</p>
        </div>

      </div>
    </div>
  </section>
'''

# Find the end of the Instructor section to insert this
# The section is: <section id="instructor" ...> ... </section>
# And then <!-- 6. CIERRE Y PRECIO --> starts
insert_point = r'(</section>\s*)(<!-- 6\. CIERRE Y PRECIO -->)'
html = re.sub(insert_point, r'\g<1>' + new_sections + r'\n\n  \g<2>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
