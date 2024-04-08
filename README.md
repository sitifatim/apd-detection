# Deteksi APD

## Problem Statement
Dalam industri konstruksi, manufaktur, dan laboratorium, penggunaan Alat Pelindung Diri (APD) sangat penting untuk menjaga keselamatan kerja. Sebuah sistem yang dapat mengenali penggunaan APD secara otomatis dapat membantu memastikan bahwa semua pekerja mematuhi standar keselamatan.

Berdasarkan penjelasan diatas, maka projek ini diperuntukan untuk membangun sistem AI yang dapat mengenali berbagai jenis APD pada pekerja dalam lingkungan kerja. 
Sistem diharapkan mampu mengidentifikasi kehadiran atau ketiadaan item APD spesifik seperti helm, masker, sarung tangan, kacamata pelindung, dan sepatu keselamatan.

## Dataset
Pemilihan dataset pada projek ini dipilih berdasarkan beberapa kriteria diantaranya:
* Gambar bervariasi dan tidak terbatas pada satu angle pengambilan gambar
* Gambar memiliki kualitas jelas

Adapun pada projek Deteksi APD ini, dataset yang digunakan merupakan dataset open source yang ada di Roboflow pada [link ini](https://universe.roboflow.com/computer-vision-8kpih/glasses-ppe).
Roboflow sendiri adalah sebuah perusahaan yang bergerak di bidang Computer Vision yang menyediakan berbagai macam dataset open source untuk mendukung para developer dalam mencari dataset. 

Dataset tersebut memiliki 5 kelas yang teranotasikan yaitu:
- Boots (sepatu boot)
- Glasses (kacamata)
- Gloves (sarung tangan)
- Helmet (helm pelindung)
- Vest (rompi)

Keseluruhan dataset, memiliki 638 data gambar yang dibagi menjadi 3 sub folder yaitu train, validation, dan test. Dari pembagian tersebut, data train memiliki data sebanyak 512 gambar, data validation memiliki data 96 sebanyak gambar, data test memiliki 30 data. Data train digunakan untuk mentraining model, data validation untuk memvalidasi hasil training model, dan data test digunakan untuk menguji model.

## Training Model
### Pemilihan Model
Model atau algoritma yang digunakan pada deteksi apd ini adalah menggunakan algoritma YOLO (You Only Look Once) versi 8 dari Ultralytics yang dapat diakses di link [berikut](https://github.com/ultralytics/ultralytics). 

### Proses Training
Proses training dilakukan dengan melatih dataset untuk mengenali object yang sudah dianotasikan pada gambar. Proses training deteksi apd ini dapat dilihat selengkapnya pada [link ini](Deteksi_APD.ipynb). 

### Hasil Training 
Hasil dari training dapat dilihat pada gambar berikut
![evaluasi](https://github.com/sitifatim/apd-detection/blob/main/models/predict1/confusion_matrix.png)

Dari gambar confusion matrix diatas dapat dilihat bahwa hanya sedikit dari gambar yang mismatch prediction. Adapun untuk evaluasi model, YOLO menggunakan mAP atau Mean Average Precision yang adalah metrik yang umum digunakan untuk mengevaluasi kinerja sistem deteksi objek dan hasilnya adalah sebagai berikut ![gambar](https://github.com/sitifatim/apd-detection/blob/main/assets/image.png)

### Evaluasi
Berikut merupakan evaluasi model yang dilakukan menggunakan data validasi
![gambar](https://github.com/sitifatim/apd-detection/blob/main/models/predict1/val_batch0_pred.jpg)

Sedangkan untuk evaluasi model menggunakan data test atau data yang belum terlihat model saat melakukan proses latih (training) adalah seperti berikut
![gambar](https://github.com/sitifatim/apd-detection/blob/main/assets/test.jpg)


## Integrasi Model
Integrasi model dilakukan menggunakan framework Flask, yaitu web framework dari Python. Input dari model dapat berupa gambar, video, dan rtsp (real time streaming protocol). Tampilan awal web adalah sebagai berikut dengan menginputkan gambar/video/rtsp
![index](https://github.com/sitifatim/apd-detection/blob/main/assets/1.png)

Sedangkan gambar berikut adalah hasil dari prediksi gambar dengan model menggunakan input gambar
![gambar](https://github.com/sitifatim/apd-detection/blob/main/assets/2.png)

Dari gambar diatas dapat dilihat bahwa selain model dapat memprediksi apd, namun juga dari sisi web mampu menampilkan apd yang terdeteksi sehingga membantu tracking lebih baik.

Untuk hasil dari inputan dengan video dapat dilihat pada gambar berikut
![hmb](https://github.com/sitifatim/apd-detection/blob/main/assets/4.png)
Namun sayangnya, hasil dari inputan video masih belum maksimal karena model gagal mendeteksi apd pada manusia yang ada di dalam video. Hal ini bisa terjadi dikarenakan beberapa hal diantaranya:
* Video diambil terlalu jauh sedangkan rata-rata dataset yang ada menggunakan angle dari depan, bukan dari cctv sehingga ini mempengaruhi model yang gagal mendeteksi dengan angle cctv
* Dataset yang digunakan untuk proses latih masih terlalu sedikit 

Apapun beberapa hal yang saya lakukan untuk mengatasi jeleknya hasil prediksi model yaitu:
* Menggunakan dua model, satu menggunakan model dari YOLOv8 pre trained untuk mendeteksi bentuk manusia terlebih dahulu, baru kemudian dari deteksi bentuk manusia, dideteksi lagi menggunakan model deteksi apd. Akan tetapi solusi ini tidak berjalan baik ketika digunakan pada video yang bentuk manusia nya terlalu jauh atau kecil. Namun, solusi ini masih dapat berjalan ketika objek manusia tidak terlalu kecil seperti di gambar berikut. Meskipun begitu, model apd masih gagal untuk mendeteksi meskipun sudah dibatasi untuk deteksi nya dari objek manusia saja. Hal ini terjadi kemungkinan karena model belum mengenali dataset dengan angle tersebut dan ada kemungkinan juga hasil objek manusia tidak memiliki kualitas yang jernih sehingga menyulitkan model apd untuk mendetkesi
![gmb](https://github.com/sitifatim/apd-detection/blob/main/assets/3.png)
* Training ulang dengan epoch yang berbeda





