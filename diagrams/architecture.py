"""Generates architecture.png for this lab. Run: python3 architecture.py"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 6.2), dpi=150)
ax.set_xlim(0, 14); ax.set_ylim(0, 6.2); ax.axis('off')
blue, dark, grey = '#0078D4', '#1B1B1B', '#605E5C'

def box(x, y, w, h, fc, ec, lw=1.5, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, ls=ls))

def arrow(x1, y1, x2, y2, c=dark):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=18, lw=2, color=c))

ax.text(7, 5.85, 'Azure Static Website Hosting with Blob Storage', ha='center', fontsize=17, weight='bold', color=dark)
box(0.3, 2.0, 2.1, 1.9, '#F3F2F1', grey)
ax.text(1.35, 3.25, 'Internet user', ha='center', fontsize=12, weight='bold', color=dark)
ax.text(1.35, 2.65, 'Web browser', ha='center', fontsize=10, color=grey)

box(3.8, 0.45, 9.9, 4.95, '#FFFFFF', blue, 1.2, '--')
ax.text(4.0, 5.1, 'Azure subscription  |  Region: East US', fontsize=10, color=blue, weight='bold')
box(4.1, 0.75, 9.3, 4.05, '#F5FAFF', '#8AB8E6', 1.2)
ax.text(4.3, 4.5, 'Resource group: lab1staticwebsite', fontsize=10.5, color=dark, weight='bold')
box(4.4, 1.05, 8.7, 3.15, '#E6F2FB', blue, 1.6)
ax.text(4.6, 3.88, 'Storage account: labstaticwebsite3  (Standard performance, LRS)', fontsize=10.5, color=dark, weight='bold')

box(4.7, 1.45, 3.0, 2.1, '#FFFFFF', blue)
ax.text(6.2, 3.05, 'Static website', ha='center', fontsize=11.5, weight='bold', color=blue)
ax.text(6.2, 2.55, 'Primary endpoint', ha='center', fontsize=9.5, color=grey)
ax.text(6.2, 2.15, '*.z13.web.core.windows.net', ha='center', fontsize=9, color=dark, family='monospace')
ax.text(6.2, 1.7, 'Index: index.html  |  Error: 404.html', ha='center', fontsize=8.5, color=grey)

box(8.5, 1.45, 4.3, 2.1, '#FFFFFF', blue)
ax.text(10.65, 3.05, '$web blob container', ha='center', fontsize=11.5, weight='bold', color=blue)
ax.text(10.65, 2.5, 'index.html  (uploaded)', ha='center', fontsize=10, color=dark, family='monospace')
ax.text(10.65, 2.0, '404.html  (configured, not uploaded)', ha='center', fontsize=9, color=grey, family='monospace')
ax.text(10.65, 1.6, 'Created automatically when enabled', ha='center', fontsize=8.5, color=grey)

arrow(2.4, 2.95, 4.7, 2.95); ax.text(3.1, 3.12, 'HTTPS GET', ha='center', fontsize=9.5, color=dark)
arrow(4.7, 2.25, 2.4, 2.25, blue); ax.text(3.1, 1.95, 'HTML page', ha='center', fontsize=9.5, color=blue)
arrow(7.7, 2.5, 8.5, 2.5)
ax.text(7, 0.12, 'No VMs or web servers to manage: Azure serves files from $web directly (PaaS).',
        ha='center', fontsize=10, color=grey, style='italic')
plt.savefig('architecture.png', bbox_inches='tight', facecolor='white')
