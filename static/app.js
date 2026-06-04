const canvas = document.getElementById("input");
const signaturePad = new SignaturePad(canvas);

const connectStrokes = document.getElementById("connect-strokes");
connectStrokes.addEventListener("click", async () => {
    const response = await fetch("/strokes", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ strokes : signaturePad.toData() })
    });

    if (!response.ok)
        console.error(response.status);

    window.location.href = "/output";
});

const reorderStrokes = document.getElementById("reorder-strokes");
reorderStrokes.addEventListener("click", async () => {
    const response = await fetch("/reorders", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ strokes : signaturePad.toData() })
    });

    if (!response.ok)
        console.error(response.status);

    window.location.href = "/output";
});
