import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_instructor = r'<div class="w-32 h-32 rounded-full bg-slate-300 shrink-0 overflow-hidden border-4 border-white shadow-md relative">.*?</div>\s*<div class="text-sm text-slate-600 space-y-4">.*?</div>'

new_instructor = '''<div class="w-32 h-32 rounded-full bg-slate-300 shrink-0 overflow-hidden border-4 border-white shadow-md relative">
          <img src="assets/instructor.jpg" alt="Instructor" class="w-full h-full object-cover">
        </div>
        <div class="text-sm text-slate-600 space-y-3">
          <h3 class="font-bold text-slate-900 text-lg">Pablo Albarracín</h3>
          <ul class="space-y-1.5 text-xs text-slate-600">
            <li class="flex items-start gap-1.5"><span class="text-blue-500">•</span> Ingeniero en Logística y Transporte.</li>
            <li class="flex items-start gap-1.5"><span class="text-blue-500">•</span> Candidato a Maestría en Comercio y Logística Internacional.</li>
            <li class="flex items-start gap-1.5"><span class="text-blue-500">•</span> Director de operaciones, emprendedor y docente universitario.</li>
            <li class="flex items-start gap-1.5"><span class="text-blue-500">•</span> Amante del mundo electrónico y computacional.</li>
          </ul>
          
          <p class="pt-3 font-handwriting text-2xl text-blue-800 leading-tight -rotate-1">
            "La imaginación es el camino seguro al conocimiento."
          </p>
          <p class="text-[11px] text-slate-500 italic pt-1">
            Hijo, esposo, padre y amigo. Yo tampoco empecé siendo programador de agentes; descubrí que estas herramientas permiten construir lo inimaginable.
          </p>
        </div>'''

html = re.sub(old_instructor, new_instructor, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
