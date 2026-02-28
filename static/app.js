const canvas = document.getElementById("input");
const signaturePad = new SignaturePad(canvas);
const connectStrokeButton = document.getElementById("connect-strokes");

connectStrokeButton.addEventListener("click", async () => {
    const response = await fetch("/signature-pad-data", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({signature_pad: signaturePad.toData()})
    });

    if (!response.ok)
        console.error("Failed to send signaturePad data:", response.status);

    window.location.href = "/output";
});