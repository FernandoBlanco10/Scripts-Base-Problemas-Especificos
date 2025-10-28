# 🧩 Explorador de Elementos Anidados en Shadow DOM

## 📘 Descripción General

Este script en JavaScript está diseñado para **localizar y manipular elementos HTML dentro de estructuras complejas que utilizan Shadow DOM, incluso en escenarios donde la recursividad estándar no logra acceder a los niveles internos del Shadow DOM debido a restricciones o elementos no detectados en el árbol principal.**

En entornos donde los elementos están encapsulados (por ejemplo, componentes web personalizados o frameworks que usan Shadow DOM), los selectores estándar (`document.querySelector`) no siempre logran acceder a ellos directamente. 

El objetivo principal de este código es:
- **Recorrer recursivamente** los árboles DOM y Shadow DOM.
- **Buscar elementos específicos** según clases, etiquetas o atributos personalizados.
- **Realizar una acción** sobre el primer elemento coincidente (por ejemplo, modificar su valor, disparar eventos o registrar su información).

---

## ⚙️ Funcionamiento

El script se compone de dos funciones principales:

### 1. `findContieneInput(root)`
Busca un elemento `<input>` (o cualquier elemento configurable) dentro de un nodo raíz, incluyendo sus subnodos con **Shadow DOM**.

**Pasos principales:**
- Verifica si el nodo raíz puede ejecutar `querySelector`.
- Busca inputs con clases específicas (`wrapper-input--content wrapper-input--input`).
- Si no encuentra resultados, recorre todos los elementos del DOM.
- Si encuentra nodos con `shadowRoot`, **entra en ellos recursivamente** hasta hallar un elemento coincidente.

### 2. `findInputParent(root)`
Funciona como una búsqueda “padre” que primero localiza un contenedor o componente específico (por ejemplo, un `ewc-string` con ciertos atributos) y luego llama a `findContieneInput()` dentro de su `shadowRoot`.

**Pasos principales:**
- Localiza el componente principal (`ewc-string` en este caso).
- Si existe, accede a su `shadowRoot` y busca dentro de él el input objetivo.
- Si no lo encuentra, continúa explorando todos los subnodos y Shadow DOMs.

---

## 🧠 Ejemplo de Uso

En este ejemplo, el script busca un campo de texto dentro de un componente web y actualiza su valor:

```javascript
const input = findInputParent();

if (input) {
    input.value = '12345'; // Valor a ingresar
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    console.log("Elemento encontrado y actualizado correctamente.");
} else {
    console.warn("No se encontró el elemento buscado.");
}
```

---

## 🔍 Casos de Uso

Este tipo de script es útil en escenarios como:
- **Automatización de pruebas** o *web scraping* sobre aplicaciones con Shadow DOM.
- **Interacción automatizada** con formularios encapsulados en componentes web.
- **Extensiones de navegador** que necesiten leer o modificar campos ocultos dentro de componentes.
- **Depuración o análisis** de estructuras HTML complejas generadas dinámicamente.

---

## 🧩 Personalización

Puedes adaptar la búsqueda cambiando los selectores:

```javascript
// Ejemplo: buscar un botón en lugar de un input
const buttons = root.querySelectorAll('button[aria-label="Enviar"]');
```

O bien, modificar el tipo de evento que se dispara tras encontrar el elemento.

---

## ⚠️ Consideraciones

- El uso de `shadowRoot` requiere que el Shadow DOM no esté cerrado (`mode: 'open'`).
- En algunos contextos, modificar valores directamente puede requerir permisos adicionales (por ejemplo, en extensiones de navegador).
- Si la página actualiza dinámicamente el DOM, podría ser necesario ejecutar el script tras una demora o tras un evento específico.

---
