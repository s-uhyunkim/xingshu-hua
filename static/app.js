const canvas = document.getElementById("input");
const signaturePad = new SignaturePad(canvas);
const connectStrokeButton = document.getElementById("connect-strokes");

connectStrokeButton.addEventListener("click", async () => {
    const temp = signaturePad.toData();
    const response = await fetch("/signature-pad-data", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({array: temp}) // object?
    });

    if (!response.ok) {
        console.error("Failed to send signaturePad data:", response.status);
        return;
    }

    window.location.href = "/output";
});