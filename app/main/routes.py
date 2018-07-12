from flask import Blueprint, render_template
from app.models import Post, User

main = Blueprint('main', __name__)

posts = [{"title": "第一篇",
          "content": "https://blog.gaprogman.com/wp-content/uploads/2013/09/zard19.jpg",
          "type": "相册",
          "date": "2018-7-12",
          "keyword": "zard", "user_id": 1},
         {"title": "第二篇",
          "content": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531389289424&di=7527d4df1e9fa096f800ef" +
                     "832a4598e9&imgtype=jpg&src=http%3A%2F%2Fimg3.imgtn.bdimg.com%2Fit%2Fu%3D1218481218%2C2272454391%26fm%3D214%26gp%3D0.jpg",
          "type": "相册",
          "date": "2018-7-12",
          "keyword": "wands",
          "user_id": 2},
         {"title": "第三篇",
          "content": "https://static.zerochan.net/Slam.Dunk.full.1108363.jpg",
          "type": "相册",
          "date": "2018-7-12",
          "keyword": "wands",
          "user_id": 2}
         ]


@main.route('/')
@main.route('/index')
def index():
    headline=Post.query.all()[0]
    entries = posts[1:3]
    return render_template('main/home.html', title='主页', headline=headline, entries=entries)


@main.route('/about')
def about():
    return render_template('main/about.html', title='关于')


@main.route('/contact')
def contact():
    return render_template('main/contact.html', title='联系')


