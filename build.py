"""Baut index.html (vollständiges HTML-Dokument für GitHub Pages) aus ../CBRM_Pruefungstrainer.html."""
from pathlib import Path

here = Path(__file__).resolve().parent
src = (here.parent / "CBRM_Pruefungstrainer.html").read_text(encoding="utf-8")
cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
page = (
    '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Lernseite zu Computer Based River Modelling (BOKU): Stoff, Rechner, Quiz.">\n'
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(here / "index.html").write_text(page, encoding="utf-8")
print("index.html geschrieben,", len(page), "Zeichen")
