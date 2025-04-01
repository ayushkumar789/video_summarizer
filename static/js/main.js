document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const videoFile = document.getElementById("video").files[0];

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.path) {
            const filename = videoFile.name;
            // Redirect to /process/<filename> after upload
            window.location.href = `/process/${filename}`;
        } else {
            alert("Upload failed!");
        }
    })
    .catch(err => {
        console.error(err);
        alert("An error occurred!");
    });
});
