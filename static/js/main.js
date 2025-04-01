
document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const videoFile = document.getElementById("video").files[0];

    // Show Lottie animation
    document.getElementById("loading").style.display = "block";

    // 👉 Start waveform animation (play)
    if (window.surfer) {
        try {
            window.surfer.play();
            setTimeout(() => {
    if (window.surfer && window.surfer.isPlaying()) {
        window.surfer.pause();
    }
}, 8000); // Stops after 8 seconds

        } catch (err) {
            console.warn("WaveSurfer play failed:", err);
        }
    }

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.path) {
            showToast("✅ Video uploaded successfully!", "success");
            setTimeout(() => {
                window.location.href = `/process/${videoFile.name}`;
            }, 500);
        } else {
            showToast("❌ Upload failed!", "error");
        }
    })
    .catch(err => {
        console.error(err);
        showToast("⚠️ Error occurred during upload", "error");
    });
});

document.getElementById("video").addEventListener("change", function () {
    const file = this.files[0];
    const preview = document.getElementById("preview");
    const waveform = document.getElementById("waveform");

    if (file) {
        const url = URL.createObjectURL(file);
        preview.src = url;
        preview.classList.remove("hidden");

        // WaveSurfer Init
        waveform.classList.remove("hidden");
        if (window.surfer) window.surfer.destroy();

        window.surfer = WaveSurfer.create({
            container: '#waveform',
            waveColor: '#3b82f6',
            progressColor: '#2563eb',
            height: 100,
            responsive: true,
        });
        window.surfer.setPlaybackRate(10);

        window.surfer.load(url);
    } else {
        preview.src = "";
        preview.classList.add("hidden");
        waveform.classList.add("hidden");
    }
});



// ✅ Alpine.js-compatible toast helper
function showToast(message, type = 'success') {
    window.dispatchEvent(new CustomEvent('toast', {
        detail: { message, type }
    }));
}
