<?php
/*
 * Formulario de presupuesto de Arte & Publicidad (hosting con PHP: Piensa Solutions, Hostinger…)
 * Envía la solicitud por correo. No guarda datos en el servidor.
 */
$DESTINO   = 'arteypublicidad.huelva@gmail.com';
$REMITENTE = 'web@arteypublicidadhuelva.es';   // dirección del propio dominio (muchos hostings lo exigen)
$GRACIAS   = '/contacto/gracias/';
$VUELTA    = '/contacto/';

$ajax = isset($_SERVER['HTTP_X_REQUESTED_WITH']);
function responder($ok, $msg, $ajax, $GRACIAS, $VUELTA) {
    if ($ajax) {
        http_response_code($ok ? 200 : 400);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['ok' => $ok, 'mensaje' => $msg]);
    } else {
        header('Location: ' . ($ok ? $GRACIAS : $VUELTA . '?error=1'), true, 303);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: ' . $VUELTA, true, 303); exit; }

// Trampa anti-spam: los robots rellenan este campo oculto
if (!empty($_POST['bot-field'])) responder(true, 'ok', $ajax, $GRACIAS, $VUELTA);

function limpio($k, $max) {
    $v = isset($_POST[$k]) ? trim((string)$_POST[$k]) : '';
    $v = str_replace(["\r", "\0"], '', $v);
    return mb_substr($v, 0, $max, 'UTF-8');
}
$nombre   = str_replace("\n", ' ', limpio('nombre', 100));
$empresa  = str_replace("\n", ' ', limpio('empresa', 120));
$email    = str_replace("\n", '', limpio('email', 150));
$telefono = str_replace("\n", '', limpio('telefono', 20));
$servicio = str_replace("\n", '', limpio('servicio', 60));
$mensaje  = limpio('mensaje', 3000);
$SERVICIOS = [
    'imprenta' => 'Imprenta y producción gráfica',
    'merchandising' => 'Merchandising publicitario',
    'rotulacion' => 'Rotulación y decoración de negocios',
    'gran-formato' => 'Impresión de gran formato',
    'publicidad-exterior' => 'Publicidad exterior: vallas y mupis',
    'campanas' => 'Campañas publicitarias y medios',
    'marketing-creatividad' => 'Creatividad y estrategia publicitaria',
    'diseno-web-redes' => 'Diseño, webs y redes sociales',
    'mascotas-corporeos' => 'Mascotas, corpóreos e imagen deportiva',
    'varios' => 'Varios servicios o campaña completa',
    'otro' => 'Otro / aún no lo sé',
];
if (isset($SERVICIOS[$servicio])) $servicio = $SERVICIOS[$servicio];
$acepta   = !empty($_POST['privacidad']);

if ($nombre === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || $servicio === ''
    || mb_strlen($mensaje, 'UTF-8') < 20 || !$acepta
    || ($telefono !== '' && !preg_match('/^[+0-9 ()\-]{9,20}$/', $telefono))) {
    responder(false, 'Faltan datos o no son válidos.', $ajax, $GRACIAS, $VUELTA);
}

$asunto = 'Solicitud de presupuesto web: ' . $servicio . ' - ' . $nombre;
$cuerpo = "Nueva solicitud desde arteypublicidadhuelva.es\n\n"
        . "Nombre: $nombre\n"
        . ($empresa  !== '' ? "Empresa: $empresa\n" : '')
        . "Correo: $email\n"
        . ($telefono !== '' ? "Teléfono: $telefono\n" : '')
        . "Servicio: $servicio\n\n"
        . "Proyecto:\n$mensaje\n\n"
        . "Ha aceptado la información sobre privacidad.\n"
        . "Fecha: " . date('d/m/Y H:i') . "\n";

$cabeceras  = "From: Web Arte y Publicidad <$REMITENTE>\r\n";
$cabeceras .= "Reply-To: $email\r\n";
$cabeceras .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
$asuntoCod  = '=?UTF-8?B?' . base64_encode($asunto) . '?=';

$ok = @mail($DESTINO, $asuntoCod, $cuerpo, $cabeceras, '-f' . $REMITENTE);
if (!$ok) $ok = @mail($DESTINO, $asuntoCod, $cuerpo, $cabeceras);   // algunos hostings no aceptan -f
responder($ok, $ok ? 'Enviado' : 'No se ha podido enviar.', $ajax, $GRACIAS, $VUELTA);
