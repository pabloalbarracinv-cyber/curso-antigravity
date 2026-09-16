import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

p1_old = r'<div class="w-12 h-12 rounded-2xl glow-box-cyan text-cyan-400 flex items-center justify-center mb-6">\s*<svg class="w-6 h-6".*?</svg>\s*</div>'
p1_new = r'<div class="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 text-xs font-mono text-cyan-400 mb-6 shadow-[0_0_15px_rgba(6,182,212,0.15)]"><span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span><span>sys.startup()</span></div>'

p2_old = r'<div class="w-12 h-12 rounded-2xl glow-box-blue text-blue-400 flex items-center justify-center mb-6">\s*<svg class="w-6 h-6".*?</svg>\s*</div>'
p2_new = r'<div class="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 text-xs font-mono text-blue-400 mb-6 shadow-[0_0_15px_rgba(37,99,235,0.15)]"><span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span><span>[Admin] connected</span></div>'

p3_old = r'<div class="w-12 h-12 rounded-2xl glow-box-emerald text-emerald-400 flex items-center justify-center mb-6">\s*<svg class="w-6 h-6".*?</svg>\s*</div>'
p3_new = r'<div class="inline-flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 text-xs font-mono text-emerald-400 mb-6 shadow-[0_0_15px_rgba(16,185,129,0.15)]"><span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span><span>db: supabase.connected</span></div>'

html = re.sub(p1_old, p1_new, html, flags=re.DOTALL)
html = re.sub(p2_old, p2_new, html, flags=re.DOTALL)
html = re.sub(p3_old, p3_new, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
