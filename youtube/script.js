document.getElementById('uploadButton').addEventListener('click', function() {
    const videoInput = document.getElementById('videoInput');
    const videoPlayer = document.getElementById('videoPlayer');

    if (videoInput.files.length > 0) {
        const file = videoInput.files[0];
        const url = URL.createObjectURL(file);

        videoPlayer.src = url;
        videoPlayer.style.display = 'block';
        videoPlayer.play();
    } else {
        alert('Please select a video file to upload.');
    }
});