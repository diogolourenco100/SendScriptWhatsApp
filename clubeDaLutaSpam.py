async function enviarScript(...scriptTexts) {
    const lines = scriptTexts.flatMap(text => text.split(/[\n\t]+/).map(line => line.trim()).filter(line => line));
    let main = document.querySelector("#main"),
        textarea = main?.querySelector(`div[contenteditable="true"]`);
    
    if (!textarea) throw new Error("Não há uma conversa aberta");

    for (const line of lines) {
        console.log("Enviando:", line);

        textarea.focus();
        setTimeout(() => {
            document.execCommand("insertText", false, line);
            textarea.dispatchEvent(new KeyboardEvent("keydown", { key: "Enter", bubbles: true }));
            textarea.dispatchEvent(new KeyboardEvent("keypress", { key: "Enter", bubbles: true }));
            textarea.dispatchEvent(new KeyboardEvent("keyup", { key: "Enter", bubbles: true }));
        }, 100);

        await new Promise(resolve => setTimeout(resolve, 300));

        let botaoEnviar = document.querySelector('[aria-label="Enviar"]');

        if (botaoEnviar) {
            botaoEnviar.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
        } else {
            console.warn("Botão de enviar não encontrado");
        }
        if (lines.indexOf(line) !== lines.length - 1) {
            await new Promise(resolve => setTimeout(resolve, 500));
        }
    }

    return lines.length;
}

enviarScript()
