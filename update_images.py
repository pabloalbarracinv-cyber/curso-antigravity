import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add hero sketch image
hero_old = r'<div class="relative w-full h-\[500px\] flex items-center justify-center">'
hero_new = r'''<div class="relative w-full h-[500px] flex items-center justify-center">
      <!-- Imagen Boceto Da Vinci Hero -->
      <div class="absolute inset-0 z-0 flex items-center justify-center opacity-70" style="mix-blend-mode: multiply;">
        <img src="assets/davinci_hero.jpg" class="w-full h-full object-cover object-center rounded-[3rem]" alt="Da Vinci Sketch" style="mask-image: radial-gradient(circle, black 30%, transparent 70%); -webkit-mask-image: radial-gradient(circle, black 30%, transparent 70%);">
      </div>
'''
html = html.replace(hero_old, hero_new)

# Add geometry sketch to Modulos section
modulos_old = r'<div class="space-y-8">'
modulos_new = r'''<div class="absolute top-10 right-10 z-0 opacity-40 pointer-events-none hidden lg:block" style="mix-blend-mode: multiply;">
        <img src="assets/davinci_geometry.jpg" class="w-96 h-96 object-cover rounded-full" alt="Geometry Sketch" style="mask-image: radial-gradient(circle, black 30%, transparent 70%); -webkit-mask-image: radial-gradient(circle, black 30%, transparent 70%);">
      </div>
      <div class="space-y-8 relative z-10">'''
html = html.replace(modulos_old, modulos_new)

# Add class 'relative' to modulos section container
html = html.replace('<div class="max-w-7xl mx-auto px-4 sm:px-8 grid lg:grid-cols-2 gap-16 items-center">', '<div class="max-w-7xl mx-auto px-4 sm:px-8 grid lg:grid-cols-2 gap-16 items-center relative">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
