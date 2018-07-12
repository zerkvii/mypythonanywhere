from flask import Blueprint, render_template, redirect, request

posts = Blueprint('posts', __name__)


@posts.route('/posts/videos')
def video_posts():
    return render_template('posts/video_posts.html', title='视频博客')


@posts.route('/posts/audios')
def audio_posts():
    return render_template('posts/audio_posts.html', title='音频博客')


@posts.route('/posts/photos')
def photo_posts():
    return render_template('posts/photo_posts.html', title='照片博客')


@posts.route('/posts/words')
def word_posts():
    return render_template('posts/word_posts.html', title='文字博客')
