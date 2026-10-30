# -*- coding: utf-8 -*-
"""
Generador estático de la web de Arte & Publicidad.

    python3 build.py              -> genera dist/ (producción: URLs limpias /servicio/)
    python3 build.py --preview    -> genera preview/ (enlaces a index.html, para verla sin servidor)

No necesita dependencias: solo Python 3.8+.
"""
import os, sys, json, shutil, html, datetime
import contenido as C

PREVIEW = "--preview" in sys.argv
OUT = "preview" if PREVIEW else "dist"
SITE = os.environ.get("SITE_URL", C.SITE_URL).rstrip("/")
E = C.EMPRESA
ANIO = datetime.date.today().year
HOY = datetime.date.today().isoformat()

def esc(t): return html.escape(t, quote=True)

# ---------------------------------------------------------------- rutas
class Ctx:
    def __init__(self, ruta, absoluto=False):
        self.ruta = ruta                      # "" (inicio), "imprenta", "contacto/gracias"
        self.prof = 0 if ruta == "" else ruta.count("/") + 1
        self.absoluto = absoluto and not PREVIEW
    def base(self):
        return "/" if self.absoluto else "../" * self.prof
    def a(self, destino):
        """Enlace relativo a otra página."""
        b = self.base()
        if destino == "":
            return (b or "./") + ("index.html" if PREVIEW else "")
        return b + destino + "/" + ("index.html" if PREVIEW else "")
    def recurso(self, p): return self.base() + p

def url_abs(ruta): return SITE + "/" + (ruta + "/" if ruta else "")

def enlazar(texto, ctx):
    for s in C.SERV:
        texto = texto.replace("{" + s + "}", ctx.a(s))
    return texto

def pendiente(txt):
    return f'<span class="pendiente">Pendiente: {esc(txt)}</span>' if C.BORRADOR else ""

def pendiente_bloque(titulo, txt):
    if not C.BORRADOR: return ""
    return f'<div class="pendiente-bloque" role="note"><strong>Pendiente de confirmar: {esc(titulo)}</strong>{esc(txt)}</div>'

CUR = ' aria-current="page"'
ICONO_FLECHA = '<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'


# ---------------------------------------------------------------- iconos de servicio (dibujo propio, trazo de 1,6)
_SVG = '<svg class="icono" viewBox="0 0 32 32" width="32" height="32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
ICONOS = {
 "imprenta": '<path d="M9 12V4h14v8"/><rect x="4" y="12" width="24" height="11" rx="2"/><path d="M9 19h14v9H9z"/><path d="M12 23h8M12 26h5"/><circle cx="24" cy="16" r="1" fill="currentColor"/>',
 "merchandising": '<rect x="5" y="12" width="22" height="16" rx="1.5"/><path d="M3 8h26v4H3zM16 8v20"/><path d="M16 8c-2-4-7-5-7-2s4 2 7 2c3 0 7 1 7-2s-5-2-7 2"/>',
 "rotulacion": '<path d="M4 13h24M5 13l1.5-7h19L27 13"/><path d="M6 13v15h20V13"/><rect x="9" y="17" width="6" height="11"/><rect x="18" y="17" width="5" height="5"/><path d="M10 9.5h12"/>',
 "gran-formato": '<rect x="3" y="5" width="26" height="15" rx="1"/><path d="M8 20l-3 8M24 20l3 8M16 20v8"/><path d="M7 15l5-5 4 4 3-3 5 5"/>',
 "publicidad-exterior": '<rect x="4" y="4" width="24" height="13" rx="1"/><path d="M16 17v11M11 28h10M9 9h9M9 12h14"/>',
 "campanas": '<path d="M5 13v6h4l11 6V7L9 13H5z"/><path d="M9 19l2 7h3l-1.5-5"/><path d="M24 12a5 5 0 0 1 0 8M26.5 9a9 9 0 0 1 0 14"/>',
 "marketing-creatividad": '<path d="M12 21c-2.5-2-4-4.5-4-8a8 8 0 0 1 16 0c0 3.5-1.5 6-4 8v3h-8z"/><path d="M12 27h8M14 30h4M16 10v6M13.5 13.5h5"/>',
 "diseno-web-redes": '<rect x="3" y="5" width="26" height="17" rx="1.5"/><path d="M11 28h10M16 22v6"/><path d="M8 17l4-4 3 3 5-6 4 5"/><circle cx="10" cy="10" r="1.3"/>',
 "mascotas-corporeos": '<circle cx="16" cy="17" r="10"/><path d="M8.5 10.5L7 4l6 3.5M23.5 10.5L25 4l-6 3.5"/><circle cx="12.5" cy="16" r="1.2" fill="currentColor"/><circle cx="19.5" cy="16" r="1.2" fill="currentColor"/><path d="M12.5 21c2 2 5 2 7 0"/>',
}
def icono(slug): return _SVG.format(ICONOS.get(slug, ""))

def ejemplos(slug, n=4):
    p = getattr(C, "PRODUCTOS", {}).get(slug, [])
    if not p: return ""
    sel = [p[0]] + [x[0].lower() + x[1:] for x in p[1:n]]
    return ", ".join(sel) + " y mucho más"

# ---------------------------------------------------------------- datos estructurados
def jsonld_organizacion():
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE + "/#empresa",
        "name": E["nombre"],
        "alternateName": E["marca"],
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo-ap-512.png",
        "areaServed": [{"@type": "City", "name": "Huelva"}, {"@type": "Country", "name": "España"}],
        "foundingDate": str(E["desde"]) if E.get("desde") else None,
        "knowsAbout": [s["nav"] for s in C.SERVICIOS],
    }
    org = {k: v for k, v in org.items() if v is not None}
    if E["telefono"]: org["telephone"] = "+34 " + E["telefono"]
    if E["email"]: org["email"] = E["email"]
    if E["redes"]: org["sameAs"] = list(E["redes"].values())
    if E["horario"]:
        dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        org["openingHoursSpecification"] = [{"@type": "OpeningHoursSpecification", "dayOfWeek": dias, "opens": a, "closes": c}
                                            for a, c in (("09:00", "14:00"), ("16:30", "20:00"))]
    if E["direccion"]:
        d = E["direccion"]
        org["@type"] = ["Organization", "LocalBusiness"]
        org["address"] = {"@type": "PostalAddress", "streetAddress": d["calle"], "postalCode": d["cp"],
                          "addressLocality": d["localidad"], "addressRegion": d["provincia"], "addressCountry": "ES"}
    return org

def jsonld_migas(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_abs(r)}
                                for i, (n, r) in enumerate(items)]}

def jsonld_servicio(s):
    return {"@context": "https://schema.org", "@type": "Service", "name": s["nav"], "serviceType": s["nav"],
            "description": s["seo_desc"], "provider": {"@id": SITE + "/#empresa"},
            "areaServed": {"@type": "Country", "name": "España"}, "url": url_abs(s["slug"])}

# ---------------------------------------------------------------- piezas comunes
def cabecera(ctx, actual):
    grupos = ""
    for gid, gnom in C.GRUPOS:
        items = "".join(
            f'<li><a href="{ctx.a(s["slug"])}"{CUR if actual == s["slug"] else ""}>{icono(s["slug"])}<span><strong>{esc(s["nav"])}</strong><span>{esc(s["resumen"])}</span></span></a></li>'
            for s in C.SERVICIOS if s["grupo"] == gid)
        grupos += f'<div class="panel__grupo"><h2>{esc(gnom)}</h2><ul>{items}</ul></div>'
    def li(dest, txt):
        cur = ' aria-current="page"' if actual == dest else ""
        return f'<li><a href="{ctx.a(dest)}"{cur}>{txt}</a></li>'
    return f'''<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="contenedor cabecera__barra">
    <a class="marca" href="{ctx.a("")}" aria-label="{esc(E["marca"])}, ir al inicio">
      <img src="{ctx.recurso("assets/img/logo-ap-96.png")}" width="40" height="40" alt="">
      <span><span class="marca__nombre">{esc(E["marca"])}</span><span class="marca__lugar">Huelva</span></span>
    </a>
    <button class="menu-movil" type="button" aria-expanded="false" aria-controls="nav-principal"><span>Menú</span></button>
    <nav class="nav" id="nav-principal" aria-label="Principal">
      <ul class="nav__lista">
        <li><button class="nav__desplegar" type="button" aria-expanded="false" aria-controls="panel-servicios">Servicios {ICONO_FLECHA}</button>
          <div class="panel" id="panel-servicios" hidden><div class="contenedor panel__rejilla">{grupos}</div></div>
        </li>
        {li("proyectos", "Proyectos")}
        {li("sobre-nosotros", "Sobre nosotros")}
        {li("contacto", "Contacto")}
      </ul>
      {tel_boton("nav__tel", esc(E["telefono"]) if E["telefono"] else None)}
      <a class="boton nav__boton" href="{ctx.a("contacto")}">Pedir presupuesto</a>
    </nav>
  </div>
</header>'''

def bloque_contacto_pie(ctx):
    filas = []
    if E["telefono"]: filas.append(f'<li><a href="tel:+34{E["telefono"].replace(" ", "")}">{esc(E["telefono"])}</a></li>')
    if E["email"]: filas.append(f'<li><a href="mailto:{E["email"]}">{esc(E["email"])}</a></li>')
    if E["direccion"]:
        d = E["direccion"]; filas.append(f'<li>{esc(d["calle"])}, {esc(d["cp"])} {esc(d["localidad"])}</li>')
    if not filas:
        filas.append(f'<li>{pendiente("teléfono, correo y dirección") or "Escríbenos desde el formulario de contacto."}</li>')
    filas.append(f'<li><a href="{ctx.a("contacto")}">Formulario de presupuesto</a></li>')
    for red, url in E["redes"].items():
        filas.append(f'<li><a href="{esc(url)}" rel="noopener">{esc(red)}: @{esc(url.rstrip("/").rsplit("/",1)[-1])}</a></li>')
    return "".join(filas)

def pie(ctx):
    mitad = len(C.SERVICIOS) // 2
    col = lambda lst: "".join(f'<li><a href="{ctx.a(s["slug"])}">{esc(s["nav"])}</a></li>' for s in lst)
    return f'''<footer class="pie">
  <div class="contenedor">
    <div class="pie__rejilla">
      <div>
        <div class="pie__marca"><img src="{ctx.recurso("assets/img/logo-ap-96.png")}" width="52" height="52" alt="Logotipo de Arte &amp; Publicidad"><b>{esc(E["marca"])}</b></div>
        <p>Publicidad, impresión, decoración, eventos, web y redes sociales. Desde Huelva, para toda España.</p>
      </div>
      <div><h2>Servicios</h2><ul>{col(C.SERVICIOS[:mitad])}</ul></div>
      <div><h2>&nbsp;<span class="visually-hidden">Más servicios</span></h2><ul>{col(C.SERVICIOS[mitad:])}</ul></div>
      <div><h2>Contacto</h2><ul>{bloque_contacto_pie(ctx)}</ul>
        <h2 style="margin-top:1.5rem">Empresa</h2><ul><li><a href="{ctx.a("proyectos")}">Proyectos</a></li><li><a href="{ctx.a("sobre-nosotros")}">Sobre nosotros</a></li></ul></div>
    </div>
    <div class="pie__legal">
      <span>© {ANIO} {esc(E["nombre"])} · Web creada por Ángel Peralta Barba</span>
      <span><a href="{ctx.a("aviso-legal")}">Aviso legal</a> &nbsp; <a href="{ctx.a("privacidad")}">Privacidad</a> &nbsp; <a href="{ctx.a("cookies")}">Cookies</a></span>
    </div>
  </div>
</footer>'''

def barra_movil(ctx, actual):
    if actual == "contacto": return ""
    extra = ""
    if E["whatsapp"]:
        extra = wa_boton("boton boton--borde", actual)
    elif E["telefono"]:
        extra = f'<a class="boton boton--borde" href="tel:+34{E["telefono"].replace(" ", "")}">Llamar</a>'
    servicio = f'?servicio={actual}' if actual in C.SERV else ""
    return f'<div class="barra-movil">{extra}<a class="boton" href="{ctx.a("contacto")}{servicio}">Pedir presupuesto</a></div>'

from urllib.parse import quote
def wa_url(servicio=None):
    msg = "Hola, quería información" + (f" sobre {C.SERV[servicio]['nav'].lower()}" if servicio in C.SERV else "") + "."
    return f"https://wa.me/{E['whatsapp']}?text={quote(msg)}"

def wa_boton(clase, servicio=None, texto="WhatsApp"):
    if not E["whatsapp"]: return ""
    return f'<a class="{clase}" href="{wa_url(servicio)}" rel="noopener">{texto}</a>'

def tel_boton(clase, texto=None):
    if not E["telefono"]: return ""
    return f'<a class="{clase}" href="tel:+34{E["telefono"].replace(" ", "")}">{texto or "Llamar al " + esc(E["telefono"])}</a>'

def cierre(ctx, titulo="¿Tienes un proyecto en mente?", texto="Cuéntanos qué necesitas y te preparamos una propuesta.", servicio=None):
    q = f"?servicio={servicio}" if servicio else ""
    return f'''<section class="cierre sobre-azul" aria-labelledby="cierre-t">
  <div class="contenedor cierre__rejilla">
    <div><h2 id="cierre-t">{titulo}</h2><p>{texto}</p></div>
    <div class="acciones" style="margin:0">{wa_boton("boton boton--borde", servicio, "Escribir por WhatsApp")}{tel_boton("boton boton--borde")}<a class="boton boton--claro" href="{ctx.a("contacto")}{q}">Pedir presupuesto</a></div>
  </div>
</section>'''

def pagina(ctx, actual, titulo, desc, cuerpo, jsonld=(), robots="index,follow", og_tipo="website", canonical=True):
    canon = url_abs(ctx.ruta)
    canon_tag = f'<link rel="canonical" href="{canon}">' if canonical else ""
    scripts = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    r = ctx.recurso
    doc = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
{canon_tag}
<meta property="og:type" content="{og_tipo}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{esc(E["nombre"])}">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-arte-publicidad.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Arte &amp; Publicidad: publicidad, impresión, decoración, eventos, web y redes sociales">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F4D95">
<link rel="icon" href="{r("assets/img/logo-ap-32.png")}" sizes="32x32" type="image/png">
<link rel="icon" href="{r("assets/img/logo-ap-192.png")}" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="{r("assets/img/logo-ap-180.png")}">
<link rel="preload" href="{r("assets/fonts/Lora-Variable.woff")}" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{r("assets/fonts/Carlito-Regular.woff")}" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{r("assets/css/site.css")}">
{scripts}
</head>
<body>
{cabecera(ctx, actual)}
<main id="contenido">
{cuerpo}
</main>
{pie(ctx)}
{barra_movil(ctx, actual)}
<script src="{r("assets/js/site.js")}" defer></script>
</body>
</html>
'''
    return doc


import base64, re as _re
def _datauri(ruta, mime):
    with open(ruta, "rb") as f: return f"data:{mime};base64," + base64.b64encode(f.read()).decode()
def autocontenido(doc):
    """Versión local: mete CSS, JS, fuentes e imágenes dentro de cada HTML para que funcione con doble clic."""
    css = open("assets/css/site.css", encoding="utf-8").read()
    css = _re.sub(r'url\("\.\./fonts/([^"]+)"\)', lambda m: 'url("' + _datauri("assets/fonts/" + m.group(1), "font/woff") + '")', css)
    js = open("assets/js/site.js", encoding="utf-8").read()
    doc = _re.sub(r'<link rel="preload"[^>]*>\n?', "", doc)
    doc = _re.sub(r'<link rel="stylesheet" href="[^"]*site\.css">', lambda m: "<style>" + css + "</style>", doc)
    doc = _re.sub(r'<script src="[^"]*site\.js" defer></script>', lambda m: "<script>" + js + "</script>", doc)
    doc = _re.sub(r'(src|href)="(?:\.\./)*assets/img/([^"]+\.png)"', lambda m: m.group(1) + '="' + _datauri("assets/img/" + m.group(2), "image/png") + '"', doc)
    return doc

def guardar(ruta_archivo, doc):
    if PREVIEW: doc = autocontenido(doc)
    p = os.path.join(OUT, ruta_archivo)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(doc)

def migas(ctx, items):
    lis = "".join(
        (f'<li><a href="{ctx.a(r)}">{esc(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{esc(n)}</li>')
        for i, (n, r) in enumerate(items))
    return f'<nav class="migas contenedor" aria-label="Estás en"><ol>{lis}</ol></nav>'

# ---------------------------------------------------------------- reparto de fotos (sin repeticiones)
def clave(f): return f["src"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
DEST = {k for _, k in getattr(C, "DESTACADOS", [])}
PORT = set(getattr(C, "PORTADAS", {}).values())

def foto_portada(slug):
    k = getattr(C, "PORTADAS", {}).get(slug)
    return next((f for f in C.TRABAJOS.get(slug, []) if clave(f) == k), None)

def fotos_galeria(slug):
    return [f for f in C.TRABAJOS.get(slug, []) if clave(f) not in DEST | PORT]

def comprobar_repetidas():
    usadas = [clave(f) for v in C.TRABAJOS.values() for f in v] + \
             [clave(f) for v in getattr(C, "PROYECTOS_EXTRA", {}).values() for f in v] + \
             ([clave(C.FOTO_SOBRE)] if getattr(C, "FOTO_SOBRE", None) else [])
    dup = {k for k in usadas if usadas.count(k) > 1}
    assert not dup, f"Fotos repetidas: {sorted(dup)}"
    assert not (DEST & PORT), f"Foto destacada y de portada a la vez: {sorted(DEST & PORT)}"
    assert len(DEST) == len(getattr(C, "DESTACADOS", [])), "Foto destacada repetida"
    for slug, k in getattr(C, "PORTADAS", {}).items():
        assert k in {clave(f) for f in C.TRABAJOS.get(slug, [])}, f"La portada {k} no pertenece a {slug}"
    todas = set(usadas)
    falta = (DEST | PORT) - todas
    assert not falta, f"Fotos destacadas o de portada que no existen: {sorted(falta)}"

def item_galeria(f, ctx):
    cli = f'<span class="galeria__cliente">{esc(f["cliente"])}</span>' if f.get("cliente") else ""
    clase = ' galeria__item--completa' if f.get("completa") else ""
    return f'<figure class="galeria__item{clase}"><a href="{ctx.recurso(f["src"])}" class="galeria__abrir" aria-label="Ampliar: {esc(f["pie"])}"><img src="{ctx.recurso(f["src"])}" alt="{esc(f["alt"])}" width="{f["w"]}" height="{f["h"]}" loading="lazy" decoding="async"></a><figcaption>{esc(f["pie"])}{cli}</figcaption></figure>'

def galeria(s, ctx, fotos=None):
    fotos = fotos_galeria(s["slug"]) if fotos is None else fotos
    if not fotos:
        return "<p>Aquí mostraremos ejemplos reales de este servicio.</p>" + huecos(s["huecos"], ctx)
    items = [item_galeria(f, ctx) for f in fotos]
    return f'<p>Algunos trabajos reales de este servicio. Pulsa una foto para verla en grande.</p><div class="galeria galeria--{min(len(fotos),3)}">' + "".join(items) + "</div>"

def huecos(lista, ctx):
    out = []
    for clave, desc in lista:
        foto = C.FOTOS.get(clave)
        if foto:
            out.append(f'<figure class="hueco"><img src="{ctx.recurso(foto["src"])}" alt="{esc(foto["alt"])}" width="{foto["w"]}" height="{foto["h"]}" loading="lazy" decoding="async"><figcaption>{esc(foto.get("pie", ""))}</figcaption></figure>')
        else:
            out.append(f'<figure class="hueco"><div class="hueco__marco" role="img" aria-label="Espacio reservado para una fotografía real">Espacio reservado para una fotografía real</div><figcaption>{esc(desc)}</figcaption></figure>')
    return '<div class="huecos">' + "".join(out) + "</div>"

# ---------------------------------------------------------------- páginas de servicio
def pagina_servicio(s):
    ctx = Ctx(s["slug"])
    L = lambda t: enlazar(t, ctx)
    partes = [migas(ctx, [("Inicio", ""), (s["nav"], s["slug"])])]
    aparte = "".join(f"<p>{a}</p>" for a in s["aparte"])
    partes.append(f'''<section class="cabeza sobre-azul">
  <div class="contenedor cabeza__rejilla">
    <div><h1>{esc(s["h1"])}</h1><p class="entrada">{esc(s["entrada"])}</p>
      <div class="acciones"><a class="boton boton--claro" href="{ctx.a("contacto")}?servicio={s["slug"]}">Pedir presupuesto</a></div></div>
    <div class="cabeza__aparte">{aparte}</div>
  </div>
</section>''')
    fp = foto_portada(s["slug"])
    if fp:
        partes[-1] = partes[-1].replace('<section class="cabeza sobre-azul">', '<section class="cabeza cabeza--con-foto sobre-azul">', 1)
        partes.append(f'''<figure class="foto-servicio contenedor"><img src="{ctx.recurso(fp["src"])}" alt="{esc(fp["alt"])}" width="{fp["w"]}" height="{fp["h"]}" fetchpriority="high"><figcaption>{esc(fp["pie"])}</figcaption></figure>''')
    necesidad = "".join(f"<p>{L(p)}</p>" for p in s["necesidad"])
    partes.append(f'''<section class="seccion"><div class="contenedor dos">
  <div><h2>{esc(s["necesidad_h2"])}</h2></div><div>{necesidad}</div>
</div></section>''')

    prods = getattr(C, "PRODUCTOS", {}).get(s["slug"], [])
    if prods:
        lis = "".join(f"<li>{esc(p)}</li>" for p in prods)
        partes.append(f'''<section class="seccion seccion--suave"><div class="contenedor">
  <div class="cabecera-productos">{icono(s["slug"])}<h2>Qué hacemos en {esc(s["nav"][0].lower() + s["nav"][1:])}</h2></div>
  <ul class="productos">{lis}</ul>
  <p class="productos__nota">¿Buscas algo que no está en la lista? <a href="{ctx.a("contacto")}?servicio={s["slug"]}">Pregúntanos</a>: si se puede imprimir, rotular o fabricar, te lo preparamos.</p>
</div></section>''')

    if s.get("terminos"):
        dl = "".join(f"<div><dt>{esc(t)}</dt><dd>{L(d)}</dd></div>" for t, d in s["terminos"])
        partes.append(f'<section class="seccion seccion--suave"><div class="contenedor"><h2>Los soportes, explicados</h2><dl class="terminos">{dl}</dl>'
                      + (f'<div class="aviso" style="background:#fff"><h3>{esc(s["aviso"][0])}</h3><p>{esc(s["aviso"][1])}</p></div>' if s.get("aviso") else "")
                      + '</div></section>')

    if s.get("canales"):
        cs = "".join(f'<div class="uso"><h3>{esc(t)}</h3><p>{L(d)}</p></div>' for t, d in s["canales"])
        partes.append(f'<section class="seccion seccion--suave"><div class="contenedor"><h2>Medios con los que se puede plantear</h2><div class="usos usos--{len(s["canales"])}">{cs}</div></div></section>')

    if s.get("pasos"):
        ps = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in s["pasos"])
        partes.append(f'<section class="seccion"><div class="contenedor"><h2>{esc(s["pasos_h2"])}</h2><ol class="pasos">{ps}</ol></div></section>')

    if s.get("usos"):
        us = "".join(f'<div class="uso"><h3>{esc(t)}</h3><p>{L(d)}</p></div>' for t, d in s["usos"])
        fondo = "" if s.get("canales") or s.get("terminos") else ""
        partes.append(f'<section class="seccion{fondo}"><div class="contenedor"><h2>{esc(s["usos_h2"])}</h2><div class="usos usos--{len(s["usos"])}">{us}</div>'
                      + pendiente_bloque("oferta concreta", s["confirmar"]) + '</div></section>')

    if s.get("catalogo"):
        partes.append(f'''<section class="seccion seccion--suave"><div class="contenedor dos">
  <div><h2>Catálogo de productos</h2></div>
  <div><p>Estamos organizando el catálogo de artículos por familias para que puedas consultarlo aquí. Mientras tanto, cuéntanos qué tipo de producto buscas y te enseñaremos las opciones disponibles.</p>
  <p><a href="{ctx.a("contacto")}?servicio=merchandising">Consultar artículos disponibles</a></p>
  {pendiente_bloque("catálogo", "Enviar familias de productos, fotos y descripciones para publicar el catálogo (sin tienda online).")}</div>
</div></section>''')

    if s.get("aviso") and not s.get("terminos"):
        partes.append(f'<section class="seccion" style="padding-top:0"><div class="contenedor"><div class="aviso" style="margin-top:0"><h3>{esc(s["aviso"][0])}</h3><p>{esc(s["aviso"][1])}</p></div>' + ("" if s.get("usos") else pendiente_bloque("oferta concreta", s["confirmar"])) + '</div></section>')

    pub = "".join(f"<li>{esc(p)}</li>" for p in s["publico"])
    partes.append(f'''<section class="seccion" style="padding-top:{"0" if s.get("aviso") and not s.get("terminos") else "var(--s5)"}"><div class="contenedor">
  <h2>Trabajos realizados</h2>
  {galeria(s, ctx)}
</div></section>''')
    partes.append(f'''<section class="seccion seccion--suave"><div class="contenedor dos">
  <div><h2>A quién puede interesar</h2></div>
  <div><ul class="publico">{pub}</ul></div>
</div></section>''')
    rel = "".join(f'<li><a href="{ctx.a(r)}"><strong>{esc(C.SERV[r]["nav"])}</strong><span>{esc(C.SERV[r]["resumen"])}</span></a></li>' for r in s["relacionados"])
    partes.append(f'<section class="seccion"><div class="contenedor"><h2>Servicios relacionados</h2><ul class="relacionados">{rel}</ul></div></section>')
    partes.append(cierre(ctx, f"Hablemos de tu proyecto", "Te respondemos con una propuesta adaptada a lo que necesitas.", s["slug"]))

    doc = pagina(ctx, s["slug"], s["seo_titulo"], s["seo_desc"], "\n".join(partes),
                 jsonld=[jsonld_migas([("Inicio", ""), (s["nav"], s["slug"])]), jsonld_servicio(s)])
    guardar(f'{s["slug"]}/index.html', doc)

# ---------------------------------------------------------------- inicio
def pagina_inicio():
    ctx = Ctx("")
    fams = ""
    for gid, gnom in C.GRUPOS:
        items = "".join(f'<li><a href="{ctx.a(s["slug"])}"><span class="familia__titulo">{icono(s["slug"])}<strong>{esc(s["nav"])}</strong></span><span class="familia__texto">{esc(ejemplos(s["slug"]) or s["resumen"])}</span></a></li>'
                        for s in C.SERVICIOS if s["grupo"] == gid)
        fams += f'<div class="familia"><h3>{esc(gnom)}</h3><ul>{items}</ul></div>'
    proyectos = ""
    if C.PROYECTOS:
        proyectos = f'<section class="seccion"><div class="contenedor"><h2>Trabajos recientes</h2>{lista_proyectos(ctx, C.PROYECTOS[:3])}<p style="margin-top:2rem"><a href="{ctx.a("proyectos")}">Ver todos los proyectos</a></p></div></section>'
    elif C.BORRADOR and not C.TRABAJOS:
        proyectos = f'<section class="seccion" style="padding-block:0 var(--s5)"><div class="contenedor">{pendiente_bloque("trabajos destacados", "Esta sección aparecerá en la portada en cuanto haya fotografías de trabajos reales autorizados (ver PROYECTOS en contenido.py).")}</div></section>'
    destacados = ""
    fotos = {f["src"].rsplit("/", 1)[-1][:-4]: f for v in C.TRABAJOS.values() for f in v}
    items = []
    for i, (serv, clave) in enumerate(getattr(C, "DESTACADOS", [])):
        f = fotos.get(clave)
        if not f: continue
        items.append(f'''<li class="destacado{" destacado--grande" if i == 0 else ""}"><a href="{ctx.a(serv)}">
  <span class="destacado__foto"><img src="{ctx.recurso(f["src"])}" alt="{esc(f["alt"])}" width="{f["w"]}" height="{f["h"]}" loading="lazy" decoding="async"></span>
  <span class="destacado__texto"><strong>{esc(f["pie"])}</strong><span>{esc(C.SERV[serv]["nav"])}</span></span></a></li>''')
    if items:
        destacados = f'''<section class="seccion seccion--trabajos" aria-labelledby="trabajos-t"><div class="contenedor">
  <div class="cabecera-seccion"><h2 id="trabajos-t">Trabajos realizados</h2><a href="{ctx.a("proyectos")}">Ver todos los proyectos</a></div>
  <ul class="destacados">{"".join(items)}</ul>
</div></section>'''
    publico = "".join(f"<li>{p}</li>" for p in ["Empresas", "Comercios", "Asociaciones", "Entidades deportivas", "Organizaciones e instituciones", "Particulares"])
    cuerpo = f'''<section class="portada sobre-azul" aria-labelledby="portada-t">
  <div class="contenedor portada__texto">
    <h1 id="portada-t">Imprenta, rotulación, diseño y publicidad desde Huelva para toda España</h1>
    <p class="entrada">Con {E["experiencia"]} de experiencia y como empresa desde {E["desde"]}, pensamos la idea, producimos las piezas y coordinamos la campaña: de una tarjeta de visita a una valla publicitaria, pasando por la fachada de tu negocio, tu web o la mascota de tu club.</p>
    <div class="acciones">
      <a class="boton boton--claro" href="{ctx.a("contacto")}">Pedir presupuesto</a>
      <a class="boton boton--borde" href="#servicios">Ver servicios</a>
    </div>
  </div>
  <p class="portada__firma" aria-hidden="true"><span>Arte</span> <span>&amp;</span> <span>Publicidad</span></p>
</section>

<section class="seccion" id="servicios" aria-labelledby="servicios-t">
  <div class="contenedor">
    <h2 id="servicios-t">Qué hacemos</h2>
    <p class="entrada">Imprenta, decoración de negocios, diseño, rotulación, publicidad exterior, redes sociales, webs, creatividad y estrategia publicitaria. Cada servicio se puede encargar por separado o combinar en un mismo proyecto.</p>
    <div class="familias">{fams}</div>
  </div>
</section>

{destacados}

<section class="seccion seccion--suave" aria-labelledby="modo-t">
  <div class="contenedor">
    <div class="dos">
      <div><h2 id="modo-t">De la idea a la calle, sin cambiar de interlocutor</h2></div>
      <div><p>Muchas empresas encargan el diseño a una persona, la impresión a otra y la campaña a una tercera. El resultado suele notarse: colores que no coinciden, mensajes distintos y piezas que no parecen de la misma marca.</p>
      <p>Nosotros reunimos la creatividad, la producción gráfica y la comunicación publicitaria. Así, el cartel, el rótulo, el anuncio y el merchandising salen de la misma idea y se reconocen como parte de lo mismo.</p></div>
    </div>
    <ol class="pasos">
      <li><h3>Idea</h3><p>Entendemos qué necesitas comunicar y a quién, y lo convertimos en un mensaje y un estilo visual.</p></li>
      <li><h3>Producción</h3><p>Lo llevamos a cada soporte: impresión, gran formato, rotulación, merchandising o corpóreos.</p></li>
      <li><h3>Difusión</h3><p>Si el proyecto lo pide, lo extendemos a prensa, radio, televisión, exterior, web y redes sociales.</p></li>
    </ol>
  </div>
</section>

{proyectos}

<section class="seccion" aria-labelledby="clientes-t">
  <div class="contenedor dos">
    <div><h2 id="clientes-t">Para quién trabajamos</h2></div>
    <div>
      <p>Trabajamos con quien necesita comunicar algo y hacerlo bien, sea cual sea su tamaño: desde el comercio que estrena fachada hasta la entidad que organiza un evento o el club que quiere renovar su imagen.</p>
      <ul class="publico">{publico}</ul>
      <p style="margin-top:1.5rem">Estamos en Huelva y trabajamos con clientes de toda España.</p>
    </div>
  </div>
</section>

{cierre(ctx, "Cuéntanos qué necesitas", "Una pieza suelta o una campaña completa: te preparamos una propuesta a medida.")}'''
    doc = pagina(ctx, "", "Arte y Publicidad Huelva | Imprenta, rotulación, diseño y publicidad desde 2010",
                 "Empresa de publicidad en Huelva desde 2010: imprenta, rotulación y decoración de negocios, diseño, webs, redes sociales, publicidad exterior y campañas para toda España.",
                 cuerpo, jsonld=[jsonld_organizacion(), {"@context": "https://schema.org", "@type": "WebSite", "name": E["nombre"], "url": SITE + "/", "inLanguage": "es-ES", "publisher": {"@id": SITE + "/#empresa"}}])
    guardar("index.html", doc)

# ---------------------------------------------------------------- proyectos
def lista_proyectos(ctx, lista):
    out = []
    for p in lista:
        f = p["foto"]
        cli = f'<p class="servicio">Cliente: {esc(p["cliente"])}</p>' if p.get("cliente") else ""
        out.append(f'''<article class="proyecto"><img src="{ctx.recurso(f["src"])}" alt="{esc(f["alt"])}" width="{f["w"]}" height="{f["h"]}" loading="lazy" decoding="async">
<h3>{esc(p["titulo"])}</h3><p class="servicio"><a href="{ctx.a(p["servicio"])}">{esc(C.SERV[p["servicio"]]["nav"])}</a></p>{cli}<p>{esc(p["descripcion"])}</p></article>''')
    return '<div class="proyectos">' + "".join(out) + "</div>"

def pagina_proyectos():
    ctx = Ctx("proyectos")
    if C.TRABAJOS:
        bloques = []
        extra = getattr(C, "PROYECTOS_EXTRA", {})
        for s in C.SERVICIOS:
            fx = extra.get(s["slug"], [])
            n = len(fotos_galeria(s["slug"]))
            enlace = f'<a href="{ctx.a(s["slug"])}">Ver {n} trabajos más en {esc(s["nav"].lower())}</a>' if n else ""
            if fx:
                bloques.append(f'<section class="bloque-proyectos"><h2>{esc(s["nav"])}</h2><div class="galeria galeria--{min(len(fx),3)}">{"".join(item_galeria(f, ctx) for f in fx)}</div><p class="bloque-proyectos__mas">{enlace}</p></section>')
        contenido = "<p class=\"entrada\">Una selección de trabajos que no aparecen en las páginas de cada servicio. Pulsa una foto para verla en grande.</p>" + "".join(bloques) if bloques else ""
        if not bloques:
            contenido = '<ul class="relacionados">' + "".join(f'<li><a href="{ctx.a(s["slug"])}"><strong>{esc(s["nav"])}</strong><span>{len(C.TRABAJOS.get(s["slug"], []))} trabajos</span></a></li>' for s in C.SERVICIOS if C.TRABAJOS.get(s["slug"])) + "</ul>"
    elif C.PROYECTOS:
        contenido = lista_proyectos(ctx, C.PROYECTOS)
    else:
        contenido = f'''<div class="vacio">
  <h2 style="font-size:var(--t-2)">Estamos preparando la selección de trabajos</h2>
  <p>Pronto publicaremos aquí proyectos reales de imprenta, rotulación, gran formato, campañas y mascotas corporativas, siempre con permiso de nuestros clientes.</p>
  <p style="margin:0">Si quieres ver ejemplos de un tipo de trabajo concreto, <a href="{ctx.a("contacto")}">pídenoslos en el formulario</a> y te los enseñaremos.</p>
</div>
{pendiente_bloque("fotografías", "Enviar fotografías de trabajos reales, con el servicio realizado y, solo si hay autorización, el nombre del cliente. Formato recomendado: JPG de al menos 1600 px de ancho.")}
<h2 style="margin-top:var(--s5)">Así se verán los proyectos</h2>
{huecos([("p-1", "Proyecto: fotografía + servicio + breve descripción"), ("p-2", "Proyecto: fotografía + servicio + breve descripción"), ("p-3", "Proyecto: fotografía + servicio + breve descripción")], ctx)}'''
    cuerpo = f'''{migas(ctx, [("Inicio", ""), ("Proyectos", "proyectos")])}
<section class="cabeza sobre-azul"><div class="contenedor"><h1>Proyectos y trabajos realizados</h1>
<p class="entrada">Una muestra de lo que hacemos para empresas, comercios, asociaciones y entidades deportivas.</p></div></section>
<section class="seccion"><div class="contenedor">{contenido}</div></section>
{cierre(ctx)}'''
    guardar("proyectos/index.html", pagina(ctx, "proyectos", "Proyectos y trabajos realizados | Arte y Publicidad Huelva",
            "Trabajos reales de imprenta, rotulación, gran formato, publicidad exterior, campañas y mascotas corporativas realizados por Arte y Publicidad en Huelva.",
            cuerpo, jsonld=[jsonld_migas([("Inicio", ""), ("Proyectos", "proyectos")])]))

# ---------------------------------------------------------------- sobre nosotros
def pagina_sobre():
    ctx = Ctx("sobre-nosotros")
    areas = "".join(f"<li>{a.capitalize()}</li>" for a in C.AREAS_ROTULO)
    fs = getattr(C, "FOTO_SOBRE", None)
    cuerpo = f'''{migas(ctx, [("Inicio", ""), ("Sobre nosotros", "sobre-nosotros")])}
<section class="cabeza{" cabeza--con-foto" if fs else ""} sobre-azul"><div class="contenedor"><h1>Sobre Arte &amp; Publicidad</h1>
<p class="entrada">{E["experiencia"].capitalize()} de experiencia en el sector y empresa desde {E["desde"]}. Desde Huelva, para clientes de toda España.</p></div></section>
{f'<figure class="foto-servicio contenedor"><img src="{ctx.recurso(fs["src"])}" alt="{esc(fs["alt"])}" width="{fs["w"]}" height="{fs["h"]}" fetchpriority="high"><figcaption>{esc(fs["pie"])}</figcaption></figure>' if fs else ""}
<section class="seccion"><div class="contenedor dos">
  <div><h2>Qué somos</h2></div>
  <div>
    <p>Arte &amp; Publicidad trabaja en publicidad, impresión, decoración, eventos, web y redes sociales. Ayudamos a empresas, comercios, asociaciones, entidades deportivas y organizaciones a comunicar lo que hacen, desde una pieza impresa hasta una campaña en varios medios.</p>
    <p>Llevamos {E["experiencia"]} en el oficio y trabajamos como empresa desde {E["desde"]}. En este tiempo hemos rotulado fachadas y vehículos, impreso todo tipo de material y creado campañas, logotipos y mascotas para clientes de Huelva y del resto de España.</p>
    <ul class="publico">{areas}</ul>
  </div>
</div></section>
<section class="seccion seccion--suave"><div class="contenedor">
  <h2>Cómo trabajamos</h2>
  <div class="usos usos--3">
    <div class="uso"><h3>Una idea, muchos soportes</h3><p>Pensamos cada encargo como parte de tu comunicación completa, para que lo que hacemos encaje con lo que ya tienes.</p></div>
    <div class="uso"><h3>Lenguaje claro</h3><p>Te explicamos qué conviene en cada caso y por qué, sin tecnicismos y sin prometer resultados que nadie puede garantizar.</p></div>
    <div class="uso"><h3>Pensado para el lugar donde se verá</h3><p>Un rótulo, una valla o un folleto se diseñan según la distancia, el espacio y el momento en que los verá tu público.</p></div>
  </div>
</div></section>
<section class="seccion"><div class="contenedor dos">
  <div><h2>Dónde estamos</h2></div>
  <div><p>Estamos en Huelva y trabajamos con clientes de toda España.</p>
  {f"<p>{esc(E['direccion']['calle'])}, {esc(E['direccion']['cp'])} {esc(E['direccion']['localidad'])}</p>" if E["direccion"] else pendiente("dirección del local o indicación de si se atiende con cita previa")}
  <p style="margin-top:1rem"><a href="{ctx.a("contacto")}">Ver formas de contacto</a></p></div>
</div></section>
{cierre(ctx)}'''
    guardar("sobre-nosotros/index.html", pagina(ctx, "sobre-nosotros", "Sobre nosotros | Arte y Publicidad Huelva",
            "Arte y Publicidad es una empresa de Huelva que une creatividad, producción gráfica y comunicación publicitaria para empresas, comercios, asociaciones y clubes.",
            cuerpo, jsonld=[jsonld_migas([("Inicio", ""), ("Sobre nosotros", "sobre-nosotros")])]))

# ---------------------------------------------------------------- contacto
def pagina_contacto():
    ctx = Ctx("contacto")
    opciones = "".join(f'<option value="{s["slug"]}">{esc(s["nav"])}</option>' for s in C.SERVICIOS)
    datos = []
    if E["telefono"]: datos.append(f'<li><span>Teléfono</span><a href="tel:+34{E["telefono"].replace(" ", "")}">{esc(E["telefono"])}</a></li>')
    else: datos.append(f'<li><span>Teléfono</span>{pendiente("número de teléfono")}</li>')
    if E["whatsapp"]: datos.append(f'<li><span>WhatsApp</span><a href="{wa_url()}" rel="noopener">{esc(E["telefono"])}</a> · Escribir por WhatsApp</li>')
    else: datos.append(f'<li><span>WhatsApp</span>{pendiente("número oficial (si se usa)")}</li>')
    if E["email"]: datos.append(f'<li><span>Correo electrónico</span><a href="mailto:{E["email"]}">{esc(E["email"])}</a></li>')
    else: datos.append(f'<li><span>Correo electrónico</span>{pendiente("correo de contacto")}</li>')
    if E["direccion"]:
        d = E["direccion"]; mapa = f' · <a href="{E["mapa_url"]}" rel="noopener">Ver en el mapa</a>' if E["mapa_url"] else ""
        datos.append(f'<li><span>Dirección</span><b>{esc(d["calle"])}, {esc(d["cp"])} {esc(d["localidad"])}</b>{mapa}</li>')
    else: datos.append(f'<li><span>Dirección</span>{pendiente("dirección o «solo con cita»")}</li>')
    if E["horario"]: datos.append(f'<li><span>Horario de atención</span><b>{esc(E["horario"])}</b></li>')
    else: datos.append(f'<li><span>Horario</span>{pendiente("horario de atención")}</li>')
    datos_html = "".join(datos) if C.BORRADOR or any([E["telefono"], E["email"], E["direccion"]]) else ""
    cuerpo = f'''{migas(ctx, [("Inicio", ""), ("Contacto", "contacto")])}
<section class="cabeza sobre-azul"><div class="contenedor"><h1>Contacto y presupuestos</h1>
<p class="entrada">Cuéntanos tu proyecto con tus propias palabras. No hace falta que sepas el nombre técnico de lo que necesitas.</p></div></section>
<section class="seccion"><div class="contenedor contacto">
  <div>
    <h2>Habla con nosotros</h2>
    <p>Respondemos a cada solicitud con una propuesta adaptada. Si tienes fotos del espacio, bocetos o ejemplos que te gusten, menciónalo en el mensaje y te diremos cómo enviárnoslos.</p>
    <ul class="datos">{datos_html}</ul>
  </div>
  <div>
    <h2>Solicitar presupuesto</h2>
    <form class="formulario" id="form-presupuesto" name="presupuesto" method="POST" action="{ctx.a("contacto/gracias")}" data-netlify="true" netlify-honeypot="bot-field" data-endpoint="{ctx.recurso("") or "./"}" novalidate>
      <input type="hidden" name="form-name" value="presupuesto">
      <p class="trampa" aria-hidden="true"><label>No rellenar este campo <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
      <div class="dos-campos">
        <div class="campo"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" type="text" autocomplete="name" required maxlength="100" aria-describedby="e-nombre"><span class="error" id="e-nombre" aria-live="polite"></span></div>
        <div class="campo"><label for="f-empresa">Empresa o entidad <span class="opcional">(opcional)</span></label><input id="f-empresa" name="empresa" type="text" autocomplete="organization" maxlength="120"></div>
      </div>
      <div class="dos-campos">
        <div class="campo"><label for="f-email">Correo electrónico</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="150" aria-describedby="e-email"><span class="error" id="e-email" aria-live="polite"></span></div>
        <div class="campo"><label for="f-telefono">Teléfono <span class="opcional">(opcional)</span></label><input id="f-telefono" name="telefono" type="tel" autocomplete="tel" pattern="[+0-9 ()\\-]{{9,20}}" maxlength="20" aria-describedby="e-telefono"><span class="error" id="e-telefono" aria-live="polite"></span></div>
      </div>
      <div class="campo"><label for="f-servicio">Servicio que te interesa</label>
        <select id="f-servicio" name="servicio" required aria-describedby="e-servicio"><option value="">Elige una opción</option>{opciones}<option value="varios">Varios servicios o una campaña completa</option><option value="otro">Otro / aún no lo sé</option></select>
        <span class="error" id="e-servicio" aria-live="polite"></span></div>
      <div class="campo"><label for="f-mensaje">Describe tu proyecto</label>
        <textarea id="f-mensaje" name="mensaje" required minlength="20" maxlength="3000" aria-describedby="e-mensaje f-ayuda" placeholder=""></textarea>
        <span class="nota-form" id="f-ayuda">Qué necesitas, para cuándo y, si lo sabes, cantidades o medidas aproximadas.</span>
        <span class="error" id="e-mensaje" aria-live="polite"></span></div>
      <div class="campo"><label class="casilla"><input type="checkbox" name="privacidad" value="aceptada" required aria-describedby="e-privacidad"><span>He leído la <a href="{ctx.a("privacidad")}">información sobre privacidad</a> y acepto que se usen mis datos para responder a esta solicitud.</span></label>
        <span class="error" id="e-privacidad" aria-live="polite"></span></div>
      <div><button class="boton" type="submit">Enviar solicitud</button></div>
      <div class="estado" id="form-estado" role="status" tabindex="-1"></div>
      <p class="nota-form">Solo usamos estos datos para contestarte. No te añadiremos a ninguna lista de envíos comerciales.</p>
    </form>
  </div>
</div></section>'''
    guardar("contacto/index.html", pagina(ctx, "contacto", "Contacto y presupuestos | Arte y Publicidad Huelva",
            "Pide presupuesto a Arte y Publicidad en Huelva para imprenta, merchandising, rótulos, gran formato, publicidad exterior, campañas o mascotas corporativas.",
            cuerpo, jsonld=[jsonld_migas([("Inicio", ""), ("Contacto", "contacto")])]))
    # Página de confirmación (envío sin JavaScript)
    ctx2 = Ctx("contacto/gracias")
    cuerpo2 = f'''<section class="cabeza sobre-azul"><div class="contenedor"><h1>Solicitud enviada</h1>
<p class="entrada">Hemos recibido tu mensaje y te responderemos por correo o por teléfono.</p>
<div class="acciones"><a class="boton boton--claro" href="{ctx2.a("")}">Volver al inicio</a></div></div></section>'''
    guardar("contacto/gracias/index.html", pagina(ctx2, "contacto", "Solicitud enviada | Arte y Publicidad Huelva",
            "Confirmación de envío del formulario de presupuesto.", cuerpo2, robots="noindex,follow"))

# ---------------------------------------------------------------- legales
def P(campo, texto):
    v = E.get(campo)
    return esc(v) if v else (pendiente(texto) or "[dato pendiente]")

def pagina_legal(ruta, titulo, h1, cuerpo_legal, desc):
    ctx = Ctx(ruta)
    cuerpo = f'''{migas(ctx, [("Inicio", ""), (h1, ruta)])}
<section class="seccion"><div class="contenedor legal"><h1>{esc(h1)}</h1>
{pendiente_bloque("revisión legal", "Estos textos son una estructura de partida. Deben completarse con los datos reales del titular y revisarse por un profesional antes de publicar la web.")}
{cuerpo_legal(ctx)}
<p style="margin-top:2rem;color:var(--gris)">Última actualización: {HOY}</p></div></section>'''
    guardar(f"{ruta}/index.html", pagina(ctx, ruta, titulo, desc, cuerpo, robots="noindex,follow"))

def legal_aviso(ctx):
    return f'''<h2>Titular del sitio web</h2>
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<ul><li>Denominación: {P("razon_social", "razón social o nombre del titular")}</li>
<li>Nombre comercial: {esc(E["nombre"])}</li>
<li>NIF/CIF: {P("nif", "NIF/CIF")}</li>
<li>Domicilio: {P("domicilio_social", "domicilio social")}</li>
<li>Correo electrónico: {P("email", "correo electrónico")}</li>
{f'<li>Datos registrales: {esc(E["registro"])}</li>' if E["registro"] else ""}</ul>
<h2>Objeto</h2><p>Este sitio web informa sobre los servicios de {esc(E["nombre"])} y permite solicitar información o presupuestos.</p>
<h2>Propiedad intelectual</h2><p>Los textos, el diseño y los elementos gráficos de esta web, incluido el logotipo, pertenecen a su titular o se usan con autorización. Las imágenes de trabajos realizados se publican con permiso de los clientes correspondientes.</p>
<h2>Responsabilidad</h2><p>El titular procura que la información publicada sea correcta y esté actualizada, pero no se responsabiliza de los errores u omisiones que pudieran existir ni del uso que se haga de ella. Los presupuestos y condiciones de cada servicio se concretan de forma individual.</p>
<h2>Enlaces externos</h2><p>Esta web puede incluir enlaces a sitios de terceros sobre cuyos contenidos el titular no tiene control.</p>'''

def legal_privacidad(ctx):
    return f'''<h2>Responsable del tratamiento</h2>
<ul><li>Responsable: {P("razon_social", "razón social o nombre del titular")}</li><li>NIF/CIF: {P("nif", "NIF/CIF")}</li>
<li>Domicilio: {P("domicilio_social", "domicilio social")}</li><li>Contacto: {P("email", "correo electrónico para asuntos de privacidad")}</li></ul>
<h2>Qué datos recogemos</h2><p>A través del <a href="{ctx.a("contacto")}">formulario de presupuesto</a> recogemos tu nombre, tu correo electrónico, el servicio que te interesa y la descripción de tu proyecto. La empresa y el teléfono son opcionales.</p>
<h2>Para qué los usamos</h2><p>Únicamente para responder a tu solicitud y, en su caso, preparar y gestionar el presupuesto. No usamos estos datos para enviar comunicaciones comerciales.</p>
<h2>Base legal</h2><p>La aplicación, a petición tuya, de medidas precontractuales (artículo 6.1.b del Reglamento General de Protección de Datos) y tu consentimiento al enviar el formulario.</p>
<h2>Cuánto tiempo los conservamos</h2><p>El tiempo necesario para responder a tu solicitud. Si se convierte en un encargo, durante la relación comercial y, después, durante los plazos que exija la ley.</p>
<h2>Con quién se comparten</h2><p>Los mensajes del formulario se procesan mediante el servicio de formularios del proveedor de alojamiento de la web (Netlify, Inc.), que actúa como encargado del tratamiento y puede almacenar los datos fuera del Espacio Económico Europeo con las garantías previstas en la normativa. No se ceden datos a otros terceros salvo obligación legal.</p>
{pendiente_bloque("proveedor", "Confirmar el proveedor final de alojamiento y formularios y revisar sus condiciones de tratamiento de datos.")}
<h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo al contacto indicado arriba. También puedes presentar una reclamación ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">aepd.es</a>).</p>'''

def legal_cookies(ctx):
    return '''<h2>Qué cookies usa esta web</h2>
<p>En su configuración actual, este sitio web no instala cookies de analítica, de publicidad ni de seguimiento, y no carga tipografías ni scripts de terceros. Por ese motivo no muestra un aviso de consentimiento.</p>
<h2>Si esto cambia</h2>
<p>Si en el futuro se añaden herramientas de analítica, mapas incrustados, vídeos de terceros u otros servicios que instalen cookies no necesarias, esta política se actualizará y se pedirá tu consentimiento antes de activarlas.</p>
<h2>Cómo gestionar las cookies</h2>
<p>Puedes consultar y borrar las cookies desde la configuración de tu navegador.</p>'''

# ---------------------------------------------------------------- 404
def pagina_404():
    ctx = Ctx("", absoluto=True)
    ctx.ruta = "404"
    servicios = "".join(f'<li><a href="{ctx.a(s["slug"])}"><strong>{esc(s["nav"])}</strong><span>{esc(s["resumen"])}</span></a></li>' for s in C.SERVICIOS)
    cuerpo = f'''<section class="cabeza sobre-azul"><div class="contenedor"><h1>Esta página no existe</h1>
<p class="entrada">Puede que la dirección esté mal escrita o que la página haya cambiado de sitio. Desde aquí puedes llegar a cualquier servicio.</p>
<div class="acciones"><a class="boton boton--claro" href="{ctx.a("")}">Ir al inicio</a><a class="boton boton--borde" href="{ctx.a("contacto")}">Contactar</a></div></div></section>
<section class="seccion"><div class="contenedor"><h2>Nuestros servicios</h2><ul class="relacionados">{servicios}</ul></div></section>'''
    doc = pagina(ctx, "", "Página no encontrada | Arte y Publicidad Huelva", "La página que buscas no existe.", cuerpo, robots="noindex,follow", canonical=False)
    guardar("404.html", doc)

# ---------------------------------------------------------------- sitemap, robots, netlify
def extras():
    rutas = [""] + [s["slug"] for s in C.SERVICIOS] + ["proyectos", "sobre-nosotros", "contacto"]
    urls = "".join(f"<url><loc>{url_abs(r)}</loc><lastmod>{HOY}</lastmod></url>" for r in rutas)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /contacto/gracias/\n\nSitemap: {SITE}/sitemap.xml\n")

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree("assets", os.path.join(OUT, "assets"))
    comprobar_repetidas()
    pagina_inicio()
    for s in C.SERVICIOS: pagina_servicio(s)
    pagina_proyectos(); pagina_sobre(); pagina_contacto()
    pagina_legal("aviso-legal", "Aviso legal | Arte y Publicidad Huelva", "Aviso legal", legal_aviso, "Aviso legal del sitio web de Arte y Publicidad Huelva.")
    pagina_legal("privacidad", "Política de privacidad | Arte y Publicidad Huelva", "Política de privacidad", legal_privacidad, "Información sobre el tratamiento de datos personales en la web de Arte y Publicidad Huelva.")
    pagina_legal("cookies", "Política de cookies | Arte y Publicidad Huelva", "Política de cookies", legal_cookies, "Información sobre el uso de cookies en la web de Arte y Publicidad Huelva.")
    pagina_404(); extras()
    n = sum(len([f for f in fs if f.endswith(".html")]) for _, _, fs in os.walk(OUT))
    print(f"OK: {n} páginas HTML en {OUT}/  (SITE_URL={SITE}, BORRADOR={C.BORRADOR}, PREVIEW={PREVIEW})")

if __name__ == "__main__":
    main()
