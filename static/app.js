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

const mergeStrokes = document.getElementById("merge-strokes");
mergeStrokes.addEventListener("click", async () => {
    const response = await fetch("/merges", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ strokes : signaturePad.toData() })
    });

    if (!response.ok)
        console.error(response.status);

    window.location.href = "/output";
});
