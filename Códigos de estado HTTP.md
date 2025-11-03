# 🌐 Guía completa de códigos de estado HTTP (1xx a 5xx)

Esta guía describe los códigos HTTP agrupados por clase, su significado, descripción y acciones recomendadas.

---

## 🟢 1xx — Información (Informational)

| Código | Significado | Descripción | Qué revisar / Acción |
|--------|------------|------------|---------------------|
| 100 | Continue | El servidor recibió los headers y el cliente debe continuar enviando el cuerpo de la solicitud. | Normalmente automático, no requiere acción. |
| 101 | Switching Protocols | El servidor acepta cambiar el protocolo según solicitud del cliente (ej. HTTP → WebSocket). | Verificar compatibilidad de protocolos. |
| 102 | Processing (WebDAV) | El servidor está procesando la solicitud, pero aún no hay respuesta final. | Esperar a que finalice el procesamiento. |

> ⚡ Raramente se ven en navegadores comunes, más útil en APIs o WebDAV.

---

## 🔵 2xx — Éxito (Successful)

| Código | Significado | Descripción | Acción recomendada |
|--------|------------|------------|------------------|
| 200 | OK | La solicitud fue exitosa. | Todo correcto, no se requiere acción. |
| 201 | Created | El recurso fue creado exitosamente (POST). | Confirmar ubicación del recurso y headers Location. |
| 202 | Accepted | La solicitud fue aceptada pero no completada. | Verificar procesamiento asincrónico o estado posterior. |
| 204 | No Content | La solicitud fue exitosa pero no hay contenido que devolver. | Normal para DELETE o PUT exitosos sin respuesta. |
| 206 | Partial Content | Respuesta parcial (rangos de archivos). | Usado para descargas parciales o streams. |

> ⚡ Más comunes: 200, 201, 204.

---

## 🟡 3xx — Redirección (Redirection)

| Código | Significado | Descripción | Acción recomendada |
|--------|------------|------------|------------------|
| 301 | Moved Permanently | El recurso se ha movido permanentemente a otra URL. | Actualizar enlaces y bookmarks. |
| 302 | Found | Redirección temporal. | Revisar si se debe actualizar cliente o mantener temporal. |
| 303 | See Other | Redirige para que el cliente use GET en otra URL. | Normal en respuestas de formularios. |
| 304 | Not Modified | El recurso no cambió desde la última solicitud (cache). | Usado para optimización de cache, no requiere acción. |
| 307 | Temporary Redirect | Redirección temporal manteniendo el método HTTP. | Verificar que cliente siga el método correcto. |
| 308 | Permanent Redirect | Redirección permanente manteniendo el método HTTP. | Actualizar cliente para usar nueva URL. |

> ⚡ Más comunes: 301, 302, 304.

---

## 🟠 4xx — Error del cliente (Client Error)

| Código | Significado | Descripción | Qué revisar / Solución |
|--------|------------|------------|----------------------|
| 400 | Bad Request | Solicitud incorrecta o mal formada. | Revisar sintaxis de URL, parámetros y headers. |
| 401 | Unauthorized | No autorizado, falta autenticación. | Verificar credenciales, tokens, headers de autorización. |
| 403 | Forbidden | El servidor entiende la solicitud pero niega acceso. | Revisar permisos de usuario o roles. |
| 404 | Not Found | Recurso solicitado no existe. | Revisar URL, endpoints y parámetros. |
| 405 | Method Not Allowed | Método HTTP no permitido. | Usar GET, POST, PUT, DELETE según lo soportado. |
| 408 | Request Timeout | Tiempo de espera de la solicitud agotado. | Revisar conectividad y tiempos de respuesta del servidor. |
| 409 | Conflict | Conflicto con el estado actual del recurso. | Revisar conflictos de edición o versiones. |
| 429 | Too Many Requests | Exceso de peticiones. | Respetar límites de API, usar retries o backoff. |

> ⚡ Más comunes: 400, 401, 403, 404, 429.

---

## 🔴 5xx — Error del servidor (Server Error)

| Código | Significado | Descripción | Qué revisar / Solución |
|--------|------------|------------|----------------------|
| 500 | Internal Server Error | Error interno del servidor. | Revisar logs del servidor, dependencias y configuración. |
| 501 | Not Implemented | El método o función no está implementada. | Revisar compatibilidad del API o método HTTP. |
| 502 | Bad Gateway | Gateway o proxy recibió respuesta inválida del upstream. | Revisar proxies, balanceadores y servicios conectados. |
| 503 | Service Unavailable | Servicio temporalmente fuera de servicio. | Verificar mantenimiento, alta carga o reiniciar servicio. |
| 504 | Gateway Timeout | Gateway no recibió respuesta a tiempo del upstream. | Revisar conectividad entre servidores y tiempos de espera. |
| 505 | HTTP Version Not Supported | La versión HTTP no es soportada. | Usar HTTP/1.1 o HTTP/2 según servidor. |
| 507 | Insufficient Storage | Espacio insuficiente en el servidor. | Liberar espacio o aumentar almacenamiento disponible. |
| 511 | Network Authentication Required | Requiere autenticación de red (ej. proxy). | Autenticarse correctamente en red o proxy. |

> ⚡ Más comunes: 500, 502, 503, 504.

---

## 🛠 Acciones generales de diagnóstico

1. Verificar **URL y sintaxis** de la solicitud.  
2. Confirmar **método HTTP correcto** (GET, POST, PUT, DELETE).  
3. Revisar **credenciales y autorización** en APIs protegidas.  
4. Comprobar **conectividad de red**: `ping`, `traceroute`, `nslookup`.  
5. Analizar **logs del servidor** para errores 5xx.  
6. Controlar **frecuencia de solicitudes** para evitar 429.  
7. Revisar **proxies, firewall o balanceadores** que puedan bloquear peticiones.  
8. Para 3xx, asegurarse de que el cliente siga correctamente las redirecciones.

---

> 💡 Nota: Los errores **4xx** suelen ser responsabilidad del cliente, los **5xx** del servidor, mientras que los 1xx, 2xx y 3xx son informativos o indican éxito/redirección.
