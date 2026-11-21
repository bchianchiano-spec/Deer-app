# Wraps the artifact page (src/sit-window.html) in a full HTML document for GitHub Pages.
import pathlib
src=pathlib.Path(__file__).parent/"src"/"sit-window.html"
body=src.read_text()
head='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-192.png"><link rel="icon" href="icon.svg">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="theme-color" content="#1d2a22">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
'''
(pathlib.Path(__file__).parent/"index.html").write_text(head+body+"\n</body></html>\n")
