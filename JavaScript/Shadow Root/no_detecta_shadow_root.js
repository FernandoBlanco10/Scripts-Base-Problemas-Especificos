function findContieneInput(root) {
    if (root.querySelector) {
        const inputs = root.querySelectorAll('input[class="wrapper-input--content wrapper-input--input"]');
        console.log('Inputs: ' + inputs.length)
        if (inputs.length > 0) {
            return inputs[0];
        }

        const allElements = root.querySelectorAll('*');
        for (const el of allElements) {
            if (el.shadowRoot) {
                const found = findContieneInput(el.shadowRoot);
                if (found) return found;
            }
        }
    }
    return null;
}


function findInputParent(root = document) {
    if (root.querySelector) {
        const ewc_string = root.querySelectorAll('ewc-string[view-section-name="REFERENCIA[0]"]');

        if (ewc_string.length > 0) {
            console.log('Encontrados ' + ewc_string[0].id)
            return findContieneInput(ewc_string[0].shadowRoot)
        }

        const allElements = root.querySelectorAll('*');
        for (const el of allElements) {
            if (el.shadowRoot) {
                const found = findInputParent(el.shadowRoot);
                if (found) return found;
            }
        }
    }
    return null;
}

const input = findInputParent();

if (input) {
    input.value = '12345'; // Reemplaza con tu valor real
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    console.log("Input 'Contiene' encontrado y actualizado.");
} else {
    console.warn("No se encontró el input con placeholder 'Contiene'.");
}

 