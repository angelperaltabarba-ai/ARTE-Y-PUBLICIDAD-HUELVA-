# -*- coding: utf-8 -*-
"""
CONTENIDO DE LA WEB — Arte & Publicidad (Huelva)

Este archivo concentra los datos de la empresa y los textos.
Para actualizar la web: edita este archivo y ejecuta `python3 build.py`.

REGLA: todo lo que vale None está PENDIENTE DE CONFIRMAR por la empresa.
Mientras BORRADOR = True, la web muestra avisos amarillos donde falta un dato.
Antes de publicar en el dominio definitivo, completa los datos y pon BORRADOR = False.
"""

BORRADOR = False

# Dominio definitivo (sin barra final). Se usa en canonical, sitemap y Open Graph.
# Se puede sobrescribir con la variable de entorno SITE_URL en Netlify.
SITE_URL = "https://arteypublicidadhuelva.netlify.app"  # PROVISIONAL: sustituir por el dominio real

EMPRESA = {
    "nombre": "Arte y Publicidad Huelva",
    "marca": "Arte & Publicidad",           # tal como aparece en el rótulo corporativo
    "zona": "Huelva",
    # --- Datos de contacto: PENDIENTES ---
    "telefono": "600 33 81 63",
    "whatsapp": "34600338163",
    "email": "arteypublicidad.huelva@gmail.com",
    "direccion": {"calle": "C/ Palos de la Frontera nº21 entreplanta nº1", "cp": "21003", "localidad": "Huelva", "provincia": "Huelva"},
    "horario": "Lunes a sábado, 09:00–14:00 y 16:30–20:00",
    "mapa_url": "https://www.google.com/maps/search/?api=1&query=Calle+Palos+de+la+Frontera+21+21003+Huelva",
    "redes": {"Instagram": "https://www.instagram.com/chemariquelme/"},
    # --- Datos legales: PENDIENTES ---
    "razon_social": "José Manuel Rodríguez Riquelme",
    "nif": "44200124N",
    "domicilio_social": "C/ Palos de la Frontera nº21 entreplanta nº1, 21003 Huelva",
    "registro": None,          # datos registrales, si los hay
    "desde": 2010,             # año de inicio de la empresa
    "experiencia": "más de 20 años",  # experiencia en el oficio
    "alcance": "toda España",
}

# Áreas que la propia empresa muestra en su rótulo corporativo
AREAS_ROTULO = ["publicidad", "impresión", "decoración", "eventos", "web", "redes sociales"]

# TRABAJOS REALES POR SERVICIO (galería dentro de cada página de servicio)
# Clave = slug del servicio. Cada foto: archivo en assets/img/trabajos/, texto alternativo y pie.
# "cliente" solo si hay permiso para mostrar el nombre.
# Ejemplo:
# TRABAJOS = {"rotulacion": [{"src": "assets/img/trabajos/rotulo-cafeteria.jpg", "w": 1600, "h": 1200,
#     "alt": "Fachada de cafetería con rótulo azul y blanco", "pie": "Rótulo de fachada para una cafetería", "cliente": None}]}
TRABAJOS = {
 "rotulacion": [
  {
   "src": "assets/img/trabajos/rotulacion-01.jpg",
   "w": 1600,
   "h": 1200,
   "pie": "Fachada rotulada para una ferretería",
   "alt": "Fachada de ferretería con rótulo rojo y amarillo y vinilos en el escaparate",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-05.jpg",
   "w": 1600,
   "h": 1200,
   "pie": "Rótulo de fachada para un restaurante",
   "alt": "Fachada de restaurante con rótulo y toldo sobre la terraza",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-03.jpg",
   "w": 1600,
   "h": 1175,
   "pie": "Fachada y banderola para una agencia de viajes",
   "alt": "Fachada de agencia de viajes con gráfica azul a gran tamaño y banderola",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-06.jpg",
   "w": 1600,
   "h": 900,
   "pie": "Rótulo de fachada para un pub",
   "alt": "Rótulo con letras corpóreas en la fachada de un pub",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-07.jpg",
   "w": 960,
   "h": 538,
   "pie": "Rótulo de fachada para una floristería",
   "alt": "Fachada de floristería con rótulo en relieve",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-04.jpg",
   "w": 900,
   "h": 532,
   "pie": "Rótulo luminoso de banderola para un bar gourmet",
   "alt": "Rótulo de banderola negro con letras doradas",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-02.jpg",
   "w": 612,
   "h": 960,
   "pie": "Vinilo de gran tamaño para una tienda de telefonía",
   "alt": "Puerta de tienda de telefonía cubierta con vinilo publicitario",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-08.jpg",
   "w": 960,
   "h": 720,
   "pie": "Decoración gráfica para una cafetería",
   "alt": "Gráfica decorativa con letras grandes en una cafetería",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-13.jpg",
   "w": 960,
   "h": 753,
   "pie": "Decoración interior para una tienda de calzado deportivo",
   "alt": "Interior de tienda deportiva con paredes rotuladas",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-09.jpg",
   "w": 1600,
   "h": 1052,
   "pie": "Rotulación de furgoneta para una empresa de pinturas",
   "alt": "Furgoneta blanca rotulada con logotipo azul",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-10.jpg",
   "w": 1024,
   "h": 768,
   "pie": "Rotulación integral de furgoneta",
   "alt": "Furgoneta oscura rotulada con imagen de marca",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-11.jpg",
   "w": 1600,
   "h": 1200,
   "pie": "Rotulación de vehículo de servicio técnico",
   "alt": "Furgoneta blanca rotulada en rojo con teléfono y servicios",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/rotulacion-12.jpg",
   "w": 960,
   "h": 720,
   "pie": "Rotulación de camión con mascota de marca",
   "alt": "Camión rotulado con un personaje ilustrado",
   "completa": False,
   "cliente": None
  }
 ],
 "imprenta": [
  {
   "src": "assets/img/trabajos/imprenta-01.jpg",
   "w": 1600,
   "h": 1113,
   "pie": "Tarjetas de visita para un taller mecánico",
   "alt": "Tarjeta de visita con logotipo de taller mecánico",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/imprenta-02.jpg",
   "w": 1500,
   "h": 1125,
   "pie": "Díptico para un restaurante",
   "alt": "Díptico impreso con la marca de un restaurante",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/imprenta-03.jpg",
   "w": 1600,
   "h": 1040,
   "pie": "Cuaderno corporativo personalizado",
   "alt": "Cuaderno de espiral con portada personalizada",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/imprenta-04.jpg",
   "w": 1600,
   "h": 1113,
   "pie": "Papelería corporativa para un despacho",
   "alt": "Tarjeta y papelería con identidad corporativa",
   "completa": False,
   "cliente": None
  }
 ],
 "merchandising": [
  {
   "src": "assets/img/trabajos/merchandising-01.jpg",
   "w": 1600,
   "h": 1600,
   "pie": "Abanicos personalizados para una clínica dental",
   "alt": "Abanico blanco con logotipo azul",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/merchandising-02.jpg",
   "w": 1600,
   "h": 1600,
   "pie": "Mochila de cuerdas para una peña flamenca",
   "alt": "Mochila negra con nombre impreso en blanco",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/merchandising-03.jpg",
   "w": 730,
   "h": 1095,
   "pie": "Gorra bordada",
   "alt": "Gorra granate con texto bordado",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/merchandising-04.jpg",
   "w": 567,
   "h": 455,
   "pie": "Polo bordado con escudo",
   "alt": "Polo azul marino con escudo bordado",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/merchandising-06.jpg",
   "w": 1053,
   "h": 473,
   "pie": "Parasol de coche personalizado",
   "alt": "Parasol plateado con logotipos impresos",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/merchandising-05.jpg",
   "w": 1435,
   "h": 487,
   "pie": "Mascarillas personalizadas",
   "alt": "Tres mascarillas con diseños personalizados",
   "completa": True,
   "cliente": None
  }
 ],
 "gran-formato": [
  {
   "src": "assets/img/trabajos/gran-formato-01.jpg",
   "w": 960,
   "h": 720,
   "pie": "Lona publicitaria en fachada",
   "alt": "Lona de gran tamaño colgada en la fachada de un edificio",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/gran-formato-02.jpg",
   "w": 1599,
   "h": 1200,
   "pie": "Vallado de obra decorado con ilustración",
   "alt": "Vallado metálico cubierto con una lona ilustrada",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/gran-formato-03.jpg",
   "w": 1600,
   "h": 1173,
   "pie": "Lonas para casetas de feria",
   "alt": "Lona impresa anunciando lonas para casetas",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/gran-formato-04.jpg",
   "w": 960,
   "h": 540,
   "pie": "Mural impreso para un interior",
   "alt": "Mural fotográfico de paisaje en una pared",
   "completa": False,
   "cliente": None
  }
 ],
 "publicidad-exterior": [
  {
   "src": "assets/img/trabajos/publicidad-exterior-01.jpg",
   "w": 1280,
   "h": 960,
   "pie": "Valla publicitaria inmobiliaria",
   "alt": "Valla publicitaria en un solar con anuncio de viviendas",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/publicidad-exterior-02.jpg",
   "w": 960,
   "h": 540,
   "pie": "Valla de obra para una promoción de viviendas",
   "alt": "Valla publicitaria en un terreno con la imagen de una promoción",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/publicidad-exterior-03.jpg",
   "w": 1068,
   "h": 632,
   "pie": "Valla publicitaria en solar",
   "alt": "Valla de gran formato con anuncio de viviendas",
   "completa": False,
   "cliente": None
  }
 ],
 "marketing-creatividad": [
  {
   "src": "assets/img/trabajos/marketing-creatividad-01.jpg",
   "w": 572,
   "h": 572,
   "pie": "Logotipo para una tienda de moda",
   "alt": "Logotipo circular negro con letras rosas y verdes",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/marketing-creatividad-02.jpg",
   "w": 1600,
   "h": 1561,
   "pie": "Identidad para una asociación sociocultural y deportiva",
   "alt": "Logotipo con figuras de colores y letras verdes",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/marketing-creatividad-03.jpg",
   "w": 1600,
   "h": 900,
   "pie": "Diseño web para una marca de mascarillas",
   "alt": "Maqueta de página web en ordenador, tableta y móvil",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/marketing-creatividad-04.jpg",
   "w": 1600,
   "h": 900,
   "pie": "Identidad corporativa aplicada a papelería",
   "alt": "Papelería con un monograma en relieve",
   "completa": False,
   "cliente": None
  }
 ],
 "mascotas-corporeos": [
  {
   "src": "assets/img/trabajos/mascotas-corporeos-01.jpg",
   "w": 960,
   "h": 540,
   "pie": "Mascota para una empresa de desatascos",
   "alt": "Ilustración de un fontanero sonriente con herramientas",
   "completa": False,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/mascotas-corporeos-02.jpg",
   "w": 500,
   "h": 500,
   "pie": "Personaje para una asociación de carnaval",
   "alt": "Ilustración de un camaleón azul sobre un lápiz",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/mascotas-corporeos-03.jpg",
   "w": 720,
   "h": 960,
   "pie": "Figura corpórea en taller",
   "alt": "Figura de gato de gran tamaño en el taller",
   "completa": True,
   "cliente": None
  },
  {
   "src": "assets/img/trabajos/mascotas-corporeos-04.jpg",
   "w": 539,
   "h": 960,
   "pie": "Figura corpórea en proceso de pintura",
   "alt": "Figura de gato sin terminar en el taller",
   "completa": True,
   "cliente": None
  }
 ]
}

# (Antiguo) Fotografías reales: clave del hueco -> {"src": "assets/img/trabajos/archivo.jpg", "alt": "...", "w": 1600, "h": 1200}
# Mientras un hueco no tenga foto, se muestra un marco reservado claramente identificado.
FOTOS = {}

# Proyectos del portfolio (solo trabajos reales y con autorización para publicarlos).
# Ejemplo:
# {"titulo": "Rótulo de fachada para una cafetería", "servicio": "rotulacion",
#  "descripcion": "Diseño y producción del rótulo principal y vinilos del escaparate.",
#  "cliente": None,  # nombre solo con autorización expresa
#  "foto": {"src": "assets/img/trabajos/cafeteria.jpg", "alt": "Fachada de cafetería con rótulo azul", "w": 1600, "h": 1200}}
PROYECTOS = []

GRUPOS = [
    ("produccion", "Producción gráfica"),
    ("espacios", "Espacios y exterior"),
    ("comunicacion", "Comunicación y creatividad"),
]

SERVICIOS = [
    {
        "slug": "imprenta",
        "grupo": "produccion",
        "nav": "Imprenta y producción gráfica",
        "resumen": "Material impreso para empresas, comercios, asociaciones y eventos.",
        "seo_titulo": "Imprenta y producción gráfica en Huelva | Arte y Publicidad",
        "seo_desc": "Material publicitario impreso para empresas, comercios, asociaciones y eventos en Huelva. Preparamos cada pieza para el uso que va a tener. Pide presupuesto.",
        "intencion": "imprenta en Huelva / material publicitario impreso",
        "h1": "Imprenta y producción gráfica",
        "entrada": "Folletos, carteles, papelería y piezas para eventos. Partimos de tu idea o de tu diseño y lo convertimos en material impreso listo para usar.",
        "aparte": ["<strong>Para</strong> empresas, comercios, asociaciones, entidades y organizadores de eventos.",
                   "<strong>Cuéntanos</strong> qué pieza necesitas, cuántas unidades y para cuándo."],
        "necesidad_h2": "Cada pieza impresa tiene un trabajo que hacer",
        "necesidad": [
            "Un folleto se lee en la mano y con calma; un cartel tiene que entenderse a varios metros; una tarjeta de visita se guarda en la cartera. La misma idea no funciona igual en todos los formatos.",
            "Producción gráfica es eso: preparar cada pieza para el sitio y el momento en que se va a ver, y mantener la coherencia con el resto de tu imagen. Si ya tienes el diseño, lo revisamos para imprimirlo; si no, lo creamos contigo.",
        ],
        "usos_h2": "Qué podemos imprimir para ti",
        "usos": [
            ("Papelería corporativa", "Tarjetas, sobres, carpetas y documentos con la identidad de tu empresa, coherentes entre sí."),
            ("Folletos y catálogos", "Para presentar productos, servicios o una programación, en mano o en el mostrador."),
            ("Cartelería", "Carteles para promociones, actividades y eventos, pensados para leerse de un vistazo."),
            ("Material para el punto de venta", "Piezas que acompañan al producto en tienda: precios, ofertas, expositores gráficos."),
            ("Material para eventos y entidades", "Programas, acreditaciones y piezas impresas para asociaciones, jornadas y celebraciones."),
        ],
        "confirmar": "Confirmar con la empresa la lista exacta de productos impresos que ofrece (los anteriores son ejemplos habituales de una imprenta).",
        "publico": ["Empresas", "Comercios", "Asociaciones", "Entidades deportivas", "Organizadores de eventos", "Particulares"],
        "huecos": [("imprenta-1", "Fotografía de material impreso real (folletos, papelería o carteles)"),
                   ("imprenta-2", "Detalle de una pieza impresa para un cliente, con autorización")],
        "relacionados": ["gran-formato", "merchandising", "marketing-creatividad"],
    },
    {
        "slug": "merchandising",
        "grupo": "produccion",
        "nav": "Merchandising publicitario",
        "resumen": "Artículos personalizados con tu marca para empresas, campañas y eventos.",
        "seo_titulo": "Merchandising publicitario personalizado en Huelva | Arte y Publicidad",
        "seo_desc": "Artículos promocionales personalizados para empresas, campañas, asociaciones, eventos y clubes deportivos. Elegimos contigo el objeto adecuado para tu público.",
        "intencion": "merchandising publicitario en Huelva / artículos promocionales personalizados",
        "h1": "Merchandising publicitario",
        "entrada": "Objetos con tu marca que la gente usa, guarda y enseña. Para empresas, campañas, asociaciones, eventos y entidades deportivas.",
        "aparte": ["<strong>Para</strong> regalos de empresa, ferias, campañas, clubes y celebraciones.",
                   "<strong>Cuéntanos</strong> a quién va dirigido, cuántas unidades y qué presupuesto manejas."],
        "necesidad_h2": "Un buen regalo promocional se sigue usando",
        "necesidad": [
            "Un artículo promocional funciona cuando tiene sentido para quien lo recibe. Una bolsa que se reutiliza o una prenda que se pone en cada partido pasa por muchas más manos que un folleto.",
            "Por eso empezamos por el público y la ocasión, y después elegimos el objeto y la forma de aplicar la marca: que se reconozca sin resultar invasiva y que encaje con el resto de tu campaña.",
        ],
        "usos_h2": "Para qué se usa el merchandising",
        "usos": [
            ("Regalos de empresa", "Detalles para clientes, proveedores o plantilla, con una presentación cuidada."),
            ("Ferias y eventos", "Artículos para repartir en un stand, una jornada o una inauguración."),
            ("Campañas publicitarias", "Objetos que prolongan una campaña y la llevan a la vida diaria de tu público."),
            ("Asociaciones y clubes", "Material identificativo para socios, voluntarios, aficionados y equipos."),
        ],
        "catalogo": True,
        "confirmar": "Confirmar con la empresa las familias de productos de merchandising que trabaja para completar el catálogo.",
        "publico": ["Empresas y marcas", "Campañas", "Asociaciones", "Clubes y entidades deportivas", "Eventos"],
        "huecos": [("merch-1", "Fotografía de artículos personalizados reales"),
                   ("merch-2", "Merchandising de un evento o entidad, con autorización")],
        "relacionados": ["imprenta", "mascotas-corporeos", "campanas"],
    },
    {
        "slug": "rotulacion",
        "grupo": "espacios",
        "nav": "Rotulación y decoración de negocios",
        "resumen": "Rótulos, fachadas, escaparates, interiores y vehículos.",
        "seo_titulo": "Rotulación comercial y rótulos para negocios en Huelva | Arte y Publicidad",
        "seo_desc": "Rótulos comerciales, decoración de fachadas y gráfica para escaparates y locales en Huelva. Diseñamos la imagen exterior de tu negocio para que se identifique de lejos.",
        "intencion": "rotulación comercial en Huelva / rótulos para negocios",
        "h1": "Rotulación y decoración de negocios",
        "entrada": "La fachada es lo primero que ve un cliente, muchas veces desde la otra acera o desde el coche. Diseñamos rótulos y gráfica para que tu negocio se identifique de lejos y se recuerde de cerca.",
        "aparte": ["<strong>Para</strong> comercios, hostelería, oficinas, clínicas, talleres y nuevas aperturas.",
                   "<strong>Cuéntanos</strong> dónde está el local y, si puedes, envíanos una foto de la fachada."],
        "necesidad_h2": "Tu fachada habla antes que tú",
        "necesidad": [
            "Un rótulo tiene que resolver tres cosas a la vez: que se lea a distancia, que diga claramente qué es el negocio y que se parezca a tu marca. Cuando falla una, el cliente pasa de largo.",
            "Trabajamos la imagen exterior como parte de tu identidad: el mismo color, la misma tipografía y el mismo tono que en tu papelería, tus redes o tu carta. Así el local refuerza la marca en lugar de contradecirla.",
        ],
        "usos_h2": "Dónde aplicamos la gráfica",
        "usos": [
            ("Rótulos de fachada", "El elemento principal de identificación del negocio, adaptado a la fachada y a la calle."),
            ("Escaparates y cristaleras", "Gráfica aplicada sobre el vidrio para informar, decorar o anunciar promociones."),
            ("Decoración de locales", "Elementos gráficos en paredes y espacios interiores que trasladan tu marca al local."),
            ("Identificación de espacios", "Indicaciones y elementos visuales para que los clientes se orienten dentro del establecimiento."),
            ("Rotulación de vehículos", "Furgonetas, coches y camiones rotulados con tu marca y tus datos de contacto: publicidad que se mueve por toda la provincia."),
            ("Aperturas y reformas", "Imagen exterior provisional o definitiva para anunciar que algo nuevo está en marcha."),
        ],
        "confirmar": "Confirmar si la empresa realiza la instalación de rótulos y qué tipos de rótulo fabrica o produce.",
        "aviso": ("Sobre la instalación", "Si necesitas que el rótulo o la gráfica queden colocados en el local, indícalo al pedir presupuesto y te explicaremos cómo se resuelve en tu caso. Algunos rótulos pueden requerir permisos municipales; conviene consultarlo con tu ayuntamiento antes de encargarlos."),
        "publico": ["Comercios", "Hostelería", "Oficinas y despachos", "Clínicas y centros", "Talleres", "Nuevas aperturas"],
        "huecos": [("rotulos-1", "Fotografía de una fachada rotulada (trabajo real autorizado)"),
                   ("rotulos-2", "Escaparate o interior decorado (trabajo real autorizado)"),
                   ("rotulos-3", "Antes y después de un local, si se dispone de ambas fotos")],
        "relacionados": ["gran-formato", "imprenta", "marketing-creatividad"],
    },
    {
        "slug": "gran-formato",
        "grupo": "produccion",
        "nav": "Impresión de gran formato",
        "resumen": "Piezas de gran tamaño para campañas, eventos, comercios y exteriores.",
        "seo_titulo": "Impresión de gran formato en Huelva | Arte y Publicidad",
        "seo_desc": "Impresión de gran formato para campañas, eventos, comercios, stands y espacios exteriores en Huelva. Preparamos el diseño para que funcione a distancia.",
        "intencion": "impresión de gran formato en Huelva",
        "h1": "Impresión de gran formato",
        "entrada": "Piezas impresas de gran tamaño para campañas, eventos, comercios y espacios exteriores, pensadas para verse a distancia y causar impacto.",
        "aparte": ["<strong>Para</strong> eventos, ferias, comercios, obras, instalaciones deportivas y campañas.",
                   "<strong>Cuéntanos</strong> las medidas del espacio y dónde irá colocada la pieza."],
        "necesidad_h2": "En grande, los errores también se ven más",
        "necesidad": [
            "Un diseño que funciona en una pantalla puede perderse a diez metros. En gran formato importan la distancia de lectura, el tamaño del texto, la resolución de las imágenes y el lugar donde se coloca la pieza.",
            "Por eso adaptamos cada diseño a sus medidas reales y al punto desde el que se va a ver. Si no tienes el archivo preparado, te ayudamos a crearlo.",
        ],
        "usos_h2": "Aplicaciones habituales",
        "usos": [
            ("Eventos y escenarios", "Fondos, photocalls y gráfica para presentaciones, galas, jornadas y celebraciones."),
            ("Ferias y stands", "Piezas que convierten un espacio vacío en un punto de encuentro con tu marca."),
            ("Comercios y obras", "Cartelería grande para fachadas, vallados y locales en obras o reforma."),
            ("Instalaciones deportivas", "Gráfica para campos, pabellones y eventos de clubes y asociaciones."),
            ("Publicidad exterior", "Piezas para vallas y otros soportes. Lo explicamos en <a href=\"{publicidad-exterior}\">publicidad exterior</a>."),
        ],
        "confirmar": "Confirmar con la empresa formatos, materiales y tamaños disponibles en gran formato.",
        "publico": ["Organizadores de eventos", "Empresas", "Comercios", "Clubes deportivos", "Asociaciones", "Instituciones"],
        "huecos": [("gran-1", "Fotografía de una pieza de gran formato instalada"),
                   ("gran-2", "Photocall o gráfica de evento real, con autorización")],
        "relacionados": ["publicidad-exterior", "rotulacion", "imprenta"],
    },
    {
        "slug": "publicidad-exterior",
        "grupo": "espacios",
        "nav": "Publicidad exterior: vallas y mupis",
        "resumen": "Creatividad y producción de piezas para vallas, mupis y otros soportes.",
        "seo_titulo": "Publicidad exterior en Huelva: vallas y mupis | Arte y Publicidad",
        "seo_desc": "Creatividad y producción de piezas para vallas publicitarias, mupis y otros soportes exteriores en Huelva. Te explicamos la diferencia entre producir y contratar el espacio.",
        "intencion": "publicidad exterior en Huelva / vallas publicitarias / mupis",
        "h1": "Publicidad exterior: vallas y mupis",
        "entrada": "Mensajes que se leen en pocos segundos, a pie de calle o desde la carretera. Te ayudamos a plantear la creatividad y a producir las piezas para vallas, mupis y otros soportes exteriores.",
        "aparte": ["<strong>Para</strong> lanzamientos, aperturas, temporadas, campañas institucionales y eventos.",
                   "<strong>Cuéntanos</strong> si ya tienes el soporte contratado o si estás empezando a plantear la campaña."],
        "necesidad_h2": "Pocos segundos para decirlo todo",
        "necesidad": [
            "Quien ve una valla suele ir conduciendo; quien pasa junto a un mupi va caminando. En los dos casos hay muy poco tiempo, así que el mensaje tiene que ser corto, la imagen potente y la marca fácil de reconocer.",
            "La publicidad exterior funciona especialmente bien para dar a conocer algo nuevo, anunciar una fecha o mantener una marca presente en una zona concreta. Y combina muy bien con otros medios de la misma campaña.",
        ],
        "terminos": [
            ("Valla publicitaria", "Soporte de gran tamaño situado normalmente junto a carreteras, accesos a la ciudad o grandes avenidas. Se ve desde lejos y en movimiento, por lo que pide mensajes muy breves."),
            ("Mupi", "Panel vertical de mobiliario urbano, habitualmente iluminado, que se encuentra en aceras y paradas. Está a la altura del peatón y permite algo más de detalle que una valla."),
            ("Otros soportes exteriores", "Lonas, carteles en fachadas, vallados de obra y elementos para eventos al aire libre, con necesidades de producción propias."),
        ],
        "aviso": ("Producir la pieza no es lo mismo que contratar el espacio",
                  "Los soportes de publicidad exterior pertenecen a empresas exhibidoras o a administraciones, que los alquilan por periodos. Una cosa es diseñar y producir la pieza; otra, reservar el soporte donde se coloca. Cuando nos pidas presupuesto, indícanos si ya tienes el espacio o si necesitas orientación para encontrarlo, y te explicaremos qué parte del proceso podemos asumir."),
        "confirmar": "Confirmar si la empresa gestiona la contratación de soportes o dispone de algún soporte propio. Hasta entonces no se afirma ninguna de las dos cosas.",
        "usos_h2": "Cuándo tiene sentido",
        "usos": [
            ("Lanzamientos y aperturas", "Para que una zona entera sepa que abres, cambias o lanzas algo."),
            ("Temporadas y fechas", "Rebajas, campañas de verano, matrículas, fiestas locales o eventos con fecha."),
            ("Campañas institucionales", "Mensajes de asociaciones, entidades y administraciones dirigidos a toda la población."),
            ("Presencia continuada", "Mantener una marca visible en los recorridos habituales de su público."),
        ],
        "publico": ["Empresas", "Comercios y cadenas", "Instituciones", "Asociaciones", "Organizadores de eventos"],
        "huecos": [("exterior-1", "Fotografía de una valla o mupi con una campaña real autorizada")],
        "relacionados": ["campanas", "gran-formato", "marketing-creatividad"],
    },
    {
        "slug": "campanas",
        "grupo": "comunicacion",
        "nav": "Campañas publicitarias y medios",
        "resumen": "Campañas coordinadas en prensa, radio, televisión, exterior y otros soportes.",
        "seo_titulo": "Campañas publicitarias en prensa, radio y televisión | Arte y Publicidad Huelva",
        "seo_desc": "Planteamos campañas publicitarias coordinadas en prensa, radio, televisión, publicidad exterior y soportes gráficos. Una misma idea adaptada al lenguaje de cada medio.",
        "intencion": "campañas publicitarias para empresas en Huelva / agencia de publicidad",
        "h1": "Campañas publicitarias y medios",
        "entrada": "Una misma idea adaptada a cada medio: el anuncio de prensa, la cuña de radio, la pieza de televisión y la valla cuentan lo mismo, cada uno con su lenguaje.",
        "aparte": ["<strong>Para</strong> empresas, instituciones, asociaciones y eventos que quieren llegar a mucha gente.",
                   "<strong>Cuéntanos</strong> qué quieres conseguir, a quién y en qué fechas."],
        "necesidad_h2": "Una campaña es más que la suma de sus anuncios",
        "necesidad": [
            "Cuando cada pieza se encarga por separado, el resultado suele ser una colección de anuncios que no se parecen entre sí. Quien los ve no los relaciona y el mensaje se diluye.",
            "Coordinar la campaña significa partir de un objetivo y una idea central, decidir qué medios tienen sentido para tu público y producir cada pieza para que se reconozca como parte del mismo mensaje.",
        ],
        "canales": [
            ("Prensa", "Anuncios para periódicos y revistas, en papel o en sus ediciones digitales. Permiten más texto y llegan a lectores con interés por lo local."),
            ("Radio", "Cuñas y menciones. Funcionan con un mensaje claro, una voz reconocible y repetición."),
            ("Televisión", "Piezas audiovisuales para emisión, donde imagen, sonido y ritmo trabajan juntos."),
            ("Publicidad exterior", "Vallas, mupis y otros soportes en la calle. Ver <a href=\"{publicidad-exterior}\">publicidad exterior</a>."),
            ("Soportes gráficos y promocionales", "Cartelería, folletos, <a href=\"{merchandising}\">merchandising</a> y material para el punto de venta."),
            ("Web y redes sociales", "Adaptación de la campaña a los canales digitales de tu marca."),
        ],
        "pasos_h2": "Cómo se construye una campaña",
        "pasos": [
            ("Objetivo y público", "Qué quieres conseguir, con quién quieres hablar y en qué plazo."),
            ("Idea central", "El mensaje y el concepto creativo que van a sostener todas las piezas."),
            ("Selección de medios", "Qué canales encajan con tu público y tu presupuesto, y en qué orden usarlos."),
            ("Producción de piezas", "Cada anuncio adaptado a su medio, manteniendo una misma identidad."),
        ],
        "aviso": ("Sobre medios y tarifas", "Los espacios, fechas y tarifas dependen de cada medio de comunicación y se concretan en cada propuesta. No publicamos audiencias ni resultados genéricos: cada campaña se plantea según su objetivo."),
        "confirmar": "Confirmar con qué medios trabaja la empresa y si gestiona la compra de espacios publicitarios.",
        "publico": ["Empresas", "Instituciones", "Asociaciones", "Eventos y festivales", "Entidades deportivas"],
        "huecos": [("campana-1", "Composición de piezas de una campaña real (prensa, exterior, redes), con autorización")],
        "relacionados": ["marketing-creatividad", "publicidad-exterior", "mascotas-corporeos"],
    },
    {
        "slug": "marketing-creatividad",
        "grupo": "comunicacion",
        "nav": "Creatividad y estrategia publicitaria",
        "resumen": "Ideas de campaña, estrategia de comunicación y conceptos creativos.",
        "seo_titulo": "Marketing, estrategia y creatividad publicitaria en Huelva | Arte y Publicidad",
        "seo_desc": "Convertimos una necesidad comercial en un mensaje claro y una propuesta visual coherente: estrategia, ideas de campaña, identidad, web, redes sociales y eventos.",
        "intencion": "marketing y creatividad publicitaria en Huelva / estrategia de comunicación",
        "h1": "Creatividad y estrategias publicitarias",
        "entrada": "Antes de diseñar una pieza hay que saber qué tiene que conseguir. Te ayudamos a convertir una necesidad comercial en un mensaje claro y en una propuesta visual coherente.",
        "aparte": ["<strong>Para</strong> marcas que empiezan, negocios que quieren renovarse y entidades con un mensaje que transmitir.",
                   "<strong>Cuéntanos</strong> el problema, no solo la pieza: «necesito más clientes en verano» nos dice más que «necesito un cartel»."],
        "necesidad_h2": "Primero el mensaje, después el soporte",
        "necesidad": [
            "Una campaña eficaz necesita coherencia entre cuatro cosas: el mensaje, el público, los canales y las piezas. Si una de ellas va por libre, el conjunto pierde fuerza.",
            "Ninguna estrategia puede garantizar un resultado de ventas. Lo que sí se puede hacer es que todo lo que comunica tu marca trabaje en la misma dirección y hable a las personas adecuadas.",
        ],
        "pasos_h2": "Del encargo a la propuesta",
        "pasos": [
            ("Escuchar la necesidad", "Qué ocurre en tu negocio o entidad y qué quieres cambiar."),
            ("Definir público y mensaje", "A quién te diriges y qué tiene que entender, sentir o hacer."),
            ("Desarrollar el concepto", "La idea creativa y el estilo visual que darán forma al mensaje."),
            ("Adaptarlo a cada soporte", "Del cartel a las redes sociales, cada pieza con su formato y su lenguaje."),
        ],
        "usos_h2": "En qué te podemos ayudar",
        "usos": [
            ("Ideas y conceptos de campaña", "El hilo conductor que hace que todas tus piezas se reconozcan como una sola campaña."),
            ("Estrategia de comunicación", "Qué decir, a quién, por qué canales y en qué momento."),
            ("Propuestas visuales e identidad", "Estilo gráfico para marcas, entidades y organizaciones, aplicable a todos sus soportes."),
            ("Web y redes sociales", "Presencia digital coherente con el resto de tu comunicación."),
            ("Eventos", "Comunicación y material gráfico para presentaciones, jornadas y celebraciones."),
        ],
        "confirmar": "Confirmar el alcance de los servicios de web, redes sociales y eventos que aparecen en el rótulo corporativo.",
        "publico": ["Marcas nuevas", "Negocios que se renuevan", "Asociaciones", "Entidades deportivas", "Instituciones"],
        "huecos": [("marketing-1", "Propuesta visual o identidad desarrollada para un cliente, con autorización")],
        "relacionados": ["campanas", "mascotas-corporeos", "imprenta"],
    },
    {
        "slug": "diseno-web-redes",
        "grupo": "comunicacion",
        "nav": "Diseño, webs y redes sociales",
        "resumen": "Logotipos, identidad visual, páginas web y contenido para redes.",
        "seo_titulo": "Diseño gráfico, páginas web y redes sociales | Arte y Publicidad Huelva",
        "seo_desc": "Diseño de logotipos e identidad visual, páginas web para empresas y contenido para redes sociales, con la misma imagen que tus rótulos e impresos.",
        "intencion": "diseño gráfico en Huelva / diseño web para empresas / redes sociales",
        "h1": "Diseño, webs y redes sociales",
        "entrada": "Tu logotipo, tu web y tus redes son lo primero que muchos clientes ven de ti. Los diseñamos para que digan lo mismo que tu fachada, tus impresos y tus campañas.",
        "aparte": ["<strong>Para</strong> negocios que empiezan, marcas que se renuevan y empresas sin presencia en internet.",
                   "<strong>Cuéntanos</strong> qué tienes ya (logotipo, web, perfiles) y qué te gustaría cambiar."],
        "necesidad_h2": "Una sola imagen, en papel y en pantalla",
        "necesidad": [
            "Cuando el logotipo de la tarjeta no se parece al de la web, o las redes usan otros colores que el rótulo, el cliente tarda más en reconocerte. La coherencia transmite seriedad.",
            "Como también producimos tus impresos, rótulos y campañas, el diseño se piensa desde el principio para funcionar en todos esos soportes, del perfil de Instagram a la fachada.",
        ],
        "usos_h2": "Qué diseñamos",
        "usos": [
            ("Logotipos e identidad visual", "El símbolo, los colores y las tipografías de tu marca, con sus normas de uso."),
            ("Diseño gráfico", "Carteles, folletos, anuncios y cualquier pieza que necesite una buena maqueta."),
            ("Páginas web", "Webs para empresas y comercios, pensadas para que el cliente te encuentre y te contacte."),
            ("Redes sociales", "Diseño de publicaciones y contenido con la imagen de tu marca."),
        ],
        "confirmar": "Confirmar qué incluye la gestión de redes sociales (diseño de publicaciones, publicación, campañas de pago).",
        "publico": ["Negocios nuevos", "Comercios", "Empresas", "Asociaciones", "Clubes deportivos"],
        "huecos": [("diseno-1", "Logotipo o web diseñada para un cliente")],
        "relacionados": ["marketing-creatividad", "imprenta", "rotulacion"],
    },
    {
        "slug": "mascotas-corporeos",
        "grupo": "comunicacion",
        "nav": "Mascotas, corpóreos e imagen deportiva",
        "resumen": "Personajes de marca y elementos visuales para equipos y asociaciones.",
        "seo_titulo": "Mascotas corporativas, corpóreos e imagen para clubes | Arte y Publicidad Huelva",
        "seo_desc": "Diseño de mascotas corporativas y personajes de marca, elementos corpóreos e imagen visual para equipos de fútbol, asociaciones, entidades y eventos.",
        "intencion": "mascotas corporativas / corpóreos para equipos de fútbol / imagen deportiva",
        "h1": "Mascotas, corpóreos e imagen deportiva",
        "entrada": "Un personaje se recuerda antes que un logotipo. Creamos mascotas y personajes de marca, y elementos visuales y corpóreos para equipos, asociaciones y eventos.",
        "aparte": ["<strong>Para</strong> marcas, clubes de fútbol y otros deportes, asociaciones y eventos.",
                   "<strong>Cuéntanos</strong> quién es tu público y dónde quieres ver al personaje o al corpóreo."],
        "necesidad_h2": "Una cara para tu marca",
        "necesidad": [
            "Las mascotas y los personajes de marca refuerzan la identidad, se recuerdan con facilidad y conectan con públicos muy distintos, de los más pequeños a la afición de toda la vida.",
            "Un buen personaje se piensa para usarse en muchos sitios: en una camiseta, en un cartel, en redes sociales, en un evento o en volumen. Por eso lo diseñamos pensando desde el principio en todas sus aplicaciones.",
        ],
        "usos_h2": "Tres formas de dar presencia a tu marca",
        "usos": [
            ("Mascotas corporativas", "Personajes con personalidad propia para empresas, marcas, asociaciones y campañas."),
            ("Elementos corpóreos", "Letras, escudos o figuras en volumen para sedes, campos, pabellones, stands y eventos."),
            ("Imagen para clubes y entidades", "Recursos gráficos de temporada, material para partidos y eventos, y comunicación para la afición."),
            ("Recursos para campañas y eventos", "Ilustraciones y elementos identificativos que acompañan al personaje en cada pieza."),
        ],
        "aviso": ("Escudos y marcas de terceros", "Solo trabajamos con escudos, nombres y marcas de clubes o entidades que nos encargan el trabajo o que tienen autorización para usarlos."),
        "confirmar": "Confirmar técnicas y materiales de los corpóreos (tamaños, uso interior o exterior) y si se fabrican o se encargan.",
        "publico": ["Equipos de fútbol", "Clubes de otros deportes", "Asociaciones", "Marcas y empresas", "Eventos"],
        "huecos": [("mascota-1", "Mascota o personaje creado por la empresa (trabajo real autorizado)"),
                   ("corporeo-1", "Elemento corpóreo para un club o entidad, con autorización")],
        "relacionados": ["merchandising", "marketing-creatividad", "gran-formato"],
    },
]

# Logotipo de tienda y diseño web pasan a "Diseño, webs y redes sociales"
_mc = TRABAJOS["marketing-creatividad"]
TRABAJOS["diseno-web-redes"] = [f for f in _mc if f["src"].endswith(("-01.jpg", "-03.jpg"))]
TRABAJOS["marketing-creatividad"] = [f for f in _mc if not f["src"].endswith(("-01.jpg", "-03.jpg"))]

# Trabajos destacados en la página de inicio: (servicio, archivo). El primero sale en grande.
DESTACADOS = [
    ("rotulacion", "rotulacion-05"),
    ("rotulacion", "rotulacion-09"),
    ("publicidad-exterior", "publicidad-exterior-01"),
    ("gran-formato", "gran-formato-01"),
    ("imprenta", "imprenta-01"),
    ("mascotas-corporeos", "mascotas-corporeos-01"),
]

SERV = {s["slug"]: s for s in SERVICIOS}
