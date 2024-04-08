  document.getElementById('selectOptionPhoto').addEventListener('change', function() {
    const selectedValue = this.value;
    
    const uploadField = document.getElementById('uploadField');
    const cameraField = document.getElementById('cameraField');
    
    if (selectedValue === '1') {
      uploadField.style.display = 'block';
      cameraField.style.display = 'none';
    } else if (selectedValue === '2') {
      uploadField.style.display = 'none';
      cameraField.style.display = 'block';
      
      setupCamera();
    } else {
      uploadField.style.display = 'none';
      cameraField.style.display = 'none';
    }
  });
  
  function handleImageUpload() {
    const input = document.getElementById('imageUpload');
    const file = input.files[0];

    const formData = new FormData();
    formData.append('imageData', file);
    formData.append('filename', 'capture');
    // Kirim ke backend
    fetch('/save_image_upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.message);
    
    // Lakukan sesuatu dengan file yang diupload, contohnya dapat diolah atau dikirim ke server
    // console.log('File uploaded:', file);
      const imageUrl = data.imageUrl;

      const canvass = document.getElementById('canvasUpload');
      const context = canvass.getContext('2d');

      const image = new Image();
      image.onload = function(){
        context.drawImage(image, 0, 0, 300, 400);
        canvass.style.display = 'block';
      };
      image.src = imageUrl;
  })
  .catch(error => {
    console.error('Error:', error);
  });
  // document.getElementById('uploadField').style.display = 'none';
  }
  
  function setupCamera() {
    const video = document.getElementById('cameraView');
    
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        video.srcObject = stream;
      })
      .catch(error => {
        console.error('Error accessing camera:', error);
      });
  }
  
  function captureFromCamera() {
 // Mencegah perilaku default dari tombol
  
  const video = document.getElementById('cameraView');
  const canvas = document.getElementById('canvasCamera');
  const context = canvas.getContext('2d');
  
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  // Ambil data gambar dari canvas untuk digunakan atau disimpan
  const imgData = canvas.toDataURL('image/jpeg');
  console.log('Captured Image Data:', imgData);
  
  // Kirim gambar yang diambil dari kamera ke server Flask
  fetch('/save_image_capture', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      imageData: imgData,
      filename: 'capture' // Nama file yang diinginkan
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
  })
  .catch(error => {
    console.error('Error:', error);
  });

  video.pause()
    // Mematikan perangkat kamera
  const stream = video.srcObject;
  const tracks = stream.getTracks();
  tracks.forEach(track => {
    track.stop();
  });

  captureFromCamera.style.display = 'none'
  const captureButton = document.getElementById('captureButton');
  captureButton.style.display = 'none';

  const img = new Image();
  img.src = canvas.toDataURL('image/jpeg');
  document.body.appendChild(img);
}

  