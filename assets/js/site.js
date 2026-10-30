/* Arte & Publicidad — interacción mínima, sin dependencias */
(function () {
  "use strict";
  var cab = document.querySelector(".cabecera");
  var menu = document.querySelector(".menu-movil");
  var desplegar = document.querySelector(".nav__desplegar");
  var panel = document.getElementById("panel-servicios");

  function cerrarPanel() {
    if (!panel) return;
    panel.hidden = true;
    desplegar.setAttribute("aria-expanded", "false");
  }

  if (menu && cab) {
    menu.addEventListener("click", function () {
      var abierto = cab.classList.toggle("abierta");
      menu.setAttribute("aria-expanded", abierto ? "true" : "false");
      menu.querySelector("span").textContent = abierto ? "Cerrar" : "Menú";
      if (!abierto) cerrarPanel();
    });
  }

  if (desplegar && panel) {
    desplegar.addEventListener("click", function (e) {
      e.stopPropagation();
      var abrir = panel.hidden;
      panel.hidden = !abrir;
      desplegar.setAttribute("aria-expanded", abrir ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width:960px)").matches) return;
      if (!panel.hidden && !panel.contains(e.target)) cerrarPanel();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !panel.hidden) { cerrarPanel(); desplegar.focus(); }
    });
  }

  /* ---------- Aparición suave al hacer scroll ---------- */
  var reducido = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reducido && "IntersectionObserver" in window) {
    var selector = "main h2, .entrada, .familia, .uso, .pasos li, .publico, .galeria__item, .destacado, " +
                   ".relacionados li, .aviso, .terminos > div, .proyecto, .cierre__rejilla, .datos, .formulario";
    var elementos = Array.prototype.filter.call(document.querySelectorAll(selector), function (el) {
      // Lo que ya se ve al cargar no se anima, para que la página no aparezca vacía
      return !el.closest(".portada") && el.getBoundingClientRect().top > window.innerHeight * 0.92;
    });
    if (elementos.length) {
      document.documentElement.classList.add("anim");
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("visible");
          obs.unobserve(e.target);
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      elementos.forEach(function (el) {
        // Escalonar elementos hermanos de una misma rejilla
        var hermanos = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
        if (el.matches(".familia, .uso, .pasos li, .galeria__item, .destacado, .relacionados li, .terminos > div, .proyecto")) {
          el.style.setProperty("--retraso", (Math.min(hermanos, 5) * 0.07) + "s");
        }
        el.classList.add("revelar");
        obs.observe(el);
      });
      // Red de seguridad: si algo no llega a activarse, se muestra igualmente
      window.addEventListener("load", function () {
        setTimeout(function () {
          elementos.forEach(function (el) {
            var r = el.getBoundingClientRect();
            if (r.top < window.innerHeight && r.bottom > 0) el.classList.add("visible");
          });
        }, 1200);
      });
    }
  }

  /* ---------- Visor de fotos de trabajos ---------- */
  var enlaces = document.querySelectorAll(".galeria__abrir");
  if (enlaces.length && typeof HTMLDialogElement === "function") {
    var visor = document.createElement("dialog");
    visor.className = "visor";
    visor.innerHTML = '<button type="button">Cerrar</button><img alt=""><p></p>';
    document.body.appendChild(visor);
    var vImg = visor.querySelector("img"), vPie = visor.querySelector("p");
    visor.querySelector("button").addEventListener("click", function () { visor.close(); });
    visor.addEventListener("click", function (e) { if (e.target === visor) visor.close(); });
    Array.prototype.forEach.call(enlaces, function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var img = a.querySelector("img"), cap = a.parentNode.querySelector("figcaption");
        vImg.src = a.getAttribute("href"); vImg.alt = img.alt;
        vPie.textContent = cap ? cap.textContent : "";
        visor.showModal();
      });
    });
  }

  /* ---------- Formulario de presupuesto ---------- */
  var form = document.getElementById("form-presupuesto");
  if (!form) return;

  // Preseleccionar el servicio si se llega desde una página de servicio (?servicio=slug)
  try {
    var s = new URLSearchParams(location.search).get("servicio");
    var sel = form.querySelector("#f-servicio");
    if (s && sel && sel.querySelector('option[value="' + s + '"]')) sel.value = s;
  } catch (err) { /* sin preselección */ }

  var estado = document.getElementById("form-estado");
  var mensajes = {
    nombre: "Escribe tu nombre.",
    email: "Escribe un correo electrónico válido, por ejemplo nombre@empresa.es.",
    telefono: "Revisa el teléfono: usa solo números, espacios o el prefijo +34.",
    servicio: "Elige el servicio que te interesa.",
    mensaje: "Cuéntanos en unas líneas qué necesitas (mínimo 20 caracteres).",
    privacidad: "Para enviar la solicitud tienes que aceptar la información sobre privacidad."
  };

  function validar(campo) {
    var err = document.getElementById("e-" + campo.name);
    var ok = campo.checkValidity();
    campo.setAttribute("aria-invalid", ok ? "false" : "true");
    if (err) err.textContent = ok ? "" : (mensajes[campo.name] || "Revisa este campo.");
    return ok;
  }

  var campos = form.querySelectorAll("input:not([type=hidden]), select, textarea");
  Array.prototype.forEach.call(campos, function (c) {
    if (c.name === "bot-field") return;
    c.addEventListener("blur", function () { if (c.value || c.type === "checkbox") validar(c); });
    c.addEventListener("input", function () { if (c.getAttribute("aria-invalid") === "true") validar(c); });
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    estado.className = "estado";
    estado.textContent = "";
    var primero = null;
    Array.prototype.forEach.call(campos, function (c) {
      if (c.name === "bot-field") return;
      if (!validar(c) && !primero) primero = c;
    });
    if (primero) { primero.focus(); return; }

    var boton = form.querySelector("button[type=submit]");
    boton.disabled = true;
    boton.textContent = "Enviando…";

    var datos = new URLSearchParams(new FormData(form)).toString();
    fetch(form.getAttribute("data-endpoint") || "/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: datos
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      form.reset();
      estado.className = "estado estado--ok";
      estado.textContent = "Solicitud enviada. Hemos recibido tu mensaje y te responderemos por correo o por teléfono.";
    }).catch(function () {
      estado.className = "estado estado--mal";
      estado.textContent = "No se ha podido enviar la solicitud. Tus datos siguen en el formulario: vuelve a intentarlo en unos minutos o usa los datos de contacto de esta página.";
    }).finally(function () {
      boton.disabled = false;
      boton.textContent = "Enviar solicitud";
      estado.focus();
    });
  });
})();
