import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Body & Backgrounds
html = html.replace('bg-white', 'bg-transparent')
html = html.replace('bg-slate-50', 'bg-transparent')
html = html.replace('bg-slate-100', 'bg-slate-800/50')
html = html.replace('tech-grid-pattern', 'tech-grid-pattern dark-mesh-bg')
html = re.sub(r'<body class="([^"]+)">', r'<body class="\1 bg-[#0A0E17] text-slate-300">', html)

# 2. Text Colors
html = html.replace('text-slate-900', 'text-white')
html = html.replace('text-slate-800', 'text-slate-100')
html = html.replace('text-slate-700', 'text-slate-300')
html = html.replace('text-slate-600', 'text-slate-400')
html = html.replace('text-slate-500', 'text-slate-400')

# 3. Borders
html = html.replace('border-slate-200', 'border-white/10')
html = html.replace('border-slate-300', 'border-white/20')

# 4. Header (Floating Island)
header_old = r'<header class="sticky top-0 z-50 bg-transparent/80 backdrop-blur-xl border-b border-white/20 shadow-sm">'
header_new = r'<header class="fixed top-4 left-4 right-4 z-50 glass-island rounded-2xl max-w-7xl mx-auto px-4 transition-all">'
html = html.replace(header_old, header_new)

# Update Logo
logo_old = r'<span class="font-extrabold text-xl tracking-tight text-white block leading-none">Antigravity</span>\s*<span class="text-\[10px\] font-bold px-1.5 py-0.5 rounded bg-slate-800/50 text-slate-400 border border-white/10">Google Tech</span>'
logo_new = r'<span class="font-extrabold text-xl tracking-tight text-white block leading-none font-mono">ANTIGRAVITY // LAB</span> <span class="flex items-center space-x-1.5 text-[10px] font-bold px-2 py-0.5 rounded-full bg-cyan-900/30 text-cyan-400 border border-cyan-500/30"><span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span><span>SYS_ACTIVE</span></span>'
html = re.sub(r'<span class="font-extrabold text-xl[^>]+>Antigravity</span>\s*<span[^>]+>Google Tech</span>', logo_new, html)

# 5. CTAs
btn_old = r'bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-(sm|base) shadow-xl shadow-indigo-600/2[05] (hover:scale-\[?1\.02\]? )?transition-all'
btn_new = r'btn-cyan-glow text-white font-bold text-\1 transition-all'
html = re.sub(btn_old, btn_new, html)
html = html.replace('bg-indigo-600 hover:bg-indigo-700', 'btn-cyan-glow')

# 6. Icons to Glow Boxes (Regex heuristic for some containers)
# For the profiles section
html = html.replace('bg-indigo-50 text-indigo-700', 'glow-box-cyan text-cyan-400')
html = html.replace('bg-sky-100 text-sky-600', 'glow-box-blue text-blue-400')
html = html.replace('bg-emerald-50 text-emerald-600', 'glow-box-emerald text-emerald-400')
html = html.replace('bg-indigo-50 text-indigo-600', 'glow-box-cyan text-cyan-400')
html = html.replace('bg-emerald-50 text-emerald-600', 'glow-box-emerald text-emerald-400')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
