import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add background color to the Hero section to differentiate it for the wave
# Actually, the user image has a beige background, so let's just add the SVG wave at the bottom of the hero section.
wave_svg = '''
  <!-- Wavy Divider -->
  <div class="absolute bottom-0 left-0 w-full overflow-hidden leading-none z-0 transform translate-y-[99%]">
    <svg class="relative block w-full h-[60px] md:h-[120px]" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" fill="#faf8f2"></path>
    </svg>
  </div>
'''

# Update the Hero section tag to be relative and have a slightly darker background so the wave is visible
old_hero_tag = '<section class="relative z-10 pt-16 pb-24 px-4 sm:px-8 max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center">'
new_hero_tag = '<section class="relative z-10 pt-16 pb-32 px-4 sm:px-8 max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center">'
html = html.replace(old_hero_tag, new_hero_tag)

# Update the right column
old_right_col = r'<div class="relative w-full h-\[500px\] flex items-center justify-center">.*?</div>\s*</section>'
new_right_col = '''<div class="relative w-full h-[500px] lg:h-[600px] flex flex-col justify-center -mr-10 lg:-mr-32">
      <!-- Arte Compuesto (Bocetos, Laptop, Proceso) -->
      <img src="assets/hero_art.jpg" class="w-full h-full object-contain object-right" alt="Laboratorio de Creación" style="mix-blend-mode: multiply; transform: scale(1.15); transform-origin: right center;">
    </div>
  </section>'''
html = re.sub(old_right_col, new_right_col, html, flags=re.DOTALL)

# Let's wrap the hero in a container that has the background and the wave
old_hero_start = '<!-- 1. HERO -->'
new_hero_start = '''<!-- 1. HERO -->
<div class="relative bg-[#f0eade] border-b border-[#e5dfd3]">
'''
html = html.replace(old_hero_start, new_hero_start)

# We need to close the div after the section
html = html.replace('</section>\n\n  <div class="w-full h-px bg-slate-200"></div>', '</section>\n' + wave_svg + '\n</div>\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
