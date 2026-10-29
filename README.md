# Web de Arte & Publicidad (Huelva)

Sitio estático en HTML, CSS y JavaScript, generado con un script de Python sin dependencias.
No usa frameworks, no carga recursos de terceros y no instala cookies.

## Estructura

```
contenido.py        Datos de la empresa y todos los textos (lo que se edita habitualmente)
build.py            Generador: crea dist/ con todas las páginas
assets/css/site.css Sistema visual (colores, tipografías, componentes)
assets/js/site.js   Menú y formulario
assets/fonts/       Lora y Carlito autoalojadas (licencia SIL OFL)
assets/img/         Logotipo oficial, iconos y imagen para redes sociales
netlify.toml        Comando de compilación, carpeta publicada y cabeceras
```

## Páginas

| URL | Página |
|---|---|
| `/` | Inicio |
| `/imprenta/` | Imprenta y producción gráfica |
| `/merchandising/` | Merchandising publicitario |
| `/rotulacion/` | Rótulos y decoración de fachadas |
| `/gran-formato/` | Impresión de gran formato |
| `/publicidad-exterior/` | Publicidad exterior: vallas y mupis |
| `/campanas/` | Campañas publicitarias y medios |
| `/marketing-creatividad/` | Marketing, estrategia y creatividad |
| `/mascotas-corporeos/` | Mascotas, corpóreos e imagen deportiva |
| `/proyectos/` | Proyectos (portfolio) |
| `/sobre-nosotros/` | Sobre nosotros |
| `/contacto/` | Contacto y presupuestos (+ `/contacto/gracias/`) |
| `/aviso-legal/`, `/privacidad/`, `/cookies/` | Textos legales (noindex) |
| `/404.html` | Página de error |

## Uso

```bash
python3 build.py             # genera dist/ (producción)
python3 build.py --preview   # genera preview/ con enlaces a index.html
cd dist && python3 -m http.server 8000   # verla en http://localhost:8000
```

## Publicar en Netlify (gratis)

1. Sube esta carpeta a un repositorio de GitHub (sin `dist/` ni `preview/`, ver `.gitignore`).
2. En Netlify: **Add new site > Import an existing project** y elige el repositorio.
   `netlify.toml` ya indica el comando (`python3 build.py`) y la carpeta (`dist`).
3. En **Site configuration > Environment variables** añade `SITE_URL` con el dominio definitivo.
4. En **Forms**, activa la detección de formularios. El formulario `presupuesto` aparecerá tras el primer despliegue.
   En **Forms > Form notifications** añade el correo que debe recibir las solicitudes.
5. Conecta el dominio en **Domain management** y comprueba que HTTPS queda activo.
6. Da de alta la web en Google Search Console y envía `https://TU-DOMINIO/sitemap.xml`.

Alternativa sin GitHub: arrastra la carpeta `dist/` a https://app.netlify.com/drop
(en ese caso, genera antes `dist/` con `SITE_URL=https://tu-dominio python3 build.py`).

## Antes de publicar en el dominio definitivo

En `contenido.py`:

- Completa `EMPRESA`: teléfono, WhatsApp, correo, dirección, horario, redes, datos legales.
  Cada dato que se rellena aparece automáticamente en contacto, pie, botones y datos estructurados.
- Cambia `SITE_URL` (o define la variable en Netlify).
- Revisa los avisos «Pendiente de confirmar» de cada servicio y ajusta los textos a la oferta real.
- Pon `BORRADOR = False` para ocultar todos los avisos amarillos.
- Haz revisar los textos legales por un profesional.

## Añadir fotografías reales

1. Copia las fotos a `assets/img/trabajos/` (JPG o WebP, 1600 px de ancho, menos de 300 KB).
2. Asígnalas a un hueco en `FOTOS` (las claves aparecen en cada servicio, campo `huecos`):
   ```python
   FOTOS = {"rotulos-1": {"src": "assets/img/trabajos/fachada.jpg", "alt": "Fachada de cafetería con rótulo azul", "w": 1600, "h": 1200, "pie": "Rótulo de fachada"}}
   ```
3. Para el portfolio, añade entradas a `PROYECTOS`. La portada mostrará automáticamente los tres primeros.

No publiques imágenes de stock ni generadas por IA como si fueran trabajos reales, ni escudos o marcas de terceros sin autorización.

## Formulario

Usa Netlify Forms: validación en el navegador, campo trampa contra spam y confirmación solo cuando
Netlify responde que lo ha recibido. Fuera de Netlify (o en local) el envío muestra un error, no un falso éxito.
El plan gratuito de Netlify incluye un número limitado de envíos al mes; consulta el límite vigente en su web.
No se necesita Supabase.

## Galerías de trabajos por servicio

Las fotos de trabajos reales se añaden en `TRABAJOS` dentro de `contenido.py`, agrupadas por servicio
(`imprenta`, `merchandising`, `rotulacion`, `gran-formato`, `publicidad-exterior`, `campanas`,
`marketing-creatividad`, `mascotas-corporeos`). Cada página de servicio muestra su galería con visor
ampliado, y la página Proyectos las reúne todas automáticamente.
