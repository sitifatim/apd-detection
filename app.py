from flask import Flask, render_template, jsonify, request, Response, redirect, url_for
import requests
import os

import cv2
from helper import *

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_image_upload', methods=['POST'])
def save_upload_image():
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename != '':
            filename = 'image.jpg'
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('image_detection'))
    return jsonify({'error': 'Tidak ada file yang diunggah'})

@app.route('/image_detection')
def image_detection():
    return render_template("image.html")

@app.route('/image_frame')
def image_frame():
    return Response(image_detect(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/input_video')
def input_video():
    return render_template('input_video.html')

@app.route('/save_video_upload', methods=['POST'])
def save_upload_video():
    if 'video' in request.files:
        video_file = request.files['video']
        if video_file.filename != '':
            filename = 'video.mp4'
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            video_file.save(video_path)
            return redirect(url_for('video_detection'))
    return jsonify({'error': 'Tidak ada file yang diunggah'})

@app.route('/video_detection')
def video_detection():
    return render_template("video.html")

@app.route('/video_frame')
def video_frame():
    return Response(video_detect(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/input_rtsp')
def input_rtsp():
    return render_template('input_video.html')


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)