import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_right_col = r'<div class="relative w-full h-\[500px\].*?</div>\s*</section>'

new_right_col = '''<div class="relative w-full h-[500px] lg:h-[600px] flex items-center justify-center">
      
      <!-- Da Vinci Flying Machine Background -->
      <div class="absolute inset-0 z-0 flex items-center justify-center opacity-80" style="mix-blend-mode: multiply;">
        <img src="assets/davinci_hero.jpg" class="w-full h-full object-cover rounded-[3rem]" alt="Da Vinci Sketch" style="mask-image: radial-gradient(circle at center, black 40%, transparent 70%); -webkit-mask-image: radial-gradient(circle at center, black 40%, transparent 70%);">
      </div>
      
      <!-- Cita manuscrita -->
      <div class="absolute top-10 right-0 -rotate-6 font-handwriting text-2xl md:text-3xl text-slate-700 opacity-90 max-w-[250px] z-10 leading-tight">
        "La imaginación es el principio de toda creación."
      </div>

      <!-- Diagrama de Proceso (Estilo Boceto) -->
      <div class="relative z-20 w-full max-w-lg mx-auto flex items-center justify-between px-2 sm:px-4 mt-20">
        <!-- Línea conectora dashed -->
        <div class="absolute left-10 right-10 top-8 border-t border-dashed border-slate-500 -z-10"></div>
        
        <!-- IDEA -->
        <div class="flex flex-col items-center">
          <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-full border border-slate-700 flex items-center justify-center bg-[#f0eade] shadow-sm relative group">
            <svg class="w-6 h-6 sm:w-7 sm:h-7 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
          </div>
          <span class="mt-3 font-serif font-bold text-[10px] sm:text-xs tracking-widest text-slate-800">IDEA</span>
        </div>

        <!-- AGENTE -->
        <div class="flex flex-col items-center">
          <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-full border border-slate-700 flex items-center justify-center bg-[#f0eade] shadow-sm">
            <svg class="w-6 h-6 sm:w-7 sm:h-7 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
          </div>
          <span class="mt-3 font-serif font-bold text-[10px] sm:text-xs tracking-widest text-slate-800">AGENTE</span>
        </div>

        <!-- CONSTRUCCIÓN -->
        <div class="flex flex-col items-center">
          <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-full border border-slate-700 flex items-center justify-center bg-[#f0eade] shadow-sm">
            <svg class="w-6 h-6 sm:w-7 sm:h-7 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <span class="mt-3 font-serif font-bold text-[10px] sm:text-xs tracking-widest text-slate-800">CONSTRUCCIÓN</span>
        </div>

        <!-- PRODUCTO -->
        <div class="flex flex-col items-center relative">
          <!-- Acuarela Azul (Simulada con Blur) -->
          <div class="absolute top-0 w-20 h-20 bg-blue-700/20 blur-xl rounded-full -z-10 mix-blend-multiply"></div>
          <div class="absolute top-2 w-16 h-16 bg-blue-600/30 blur-md rounded-full -z-10 mix-blend-multiply border-r-4 border-blue-500 rounded-tr-[50px] rounded-br-[20px] transform rotate-12"></div>
          
          <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-full border border-slate-700 flex items-center justify-center bg-[#f0eade] shadow-sm relative">
            <svg class="w-6 h-6 sm:w-7 sm:h-7 text-slate-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
          </div>
          <span class="mt-3 font-serif font-bold text-[10px] sm:text-xs tracking-widest text-slate-800">PRODUCTO</span>
        </div>
      </div>
    </div>
  </section>'''

html = re.sub(old_right_col, new_right_col, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
