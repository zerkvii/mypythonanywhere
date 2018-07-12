from flask import Blueprint, render_template, redirect

categories = Blueprint('categories', __name__)


@categories.route('/categories/life')
def life():
    return render_template('categories/life.html', title='生活')


@categories.route('/categories/health')
def health():
    return render_template('categories/health.html', title='健康')


@categories.route('/categories/family')
def family():
    return render_template('categories/family.html', title='家庭')


@categories.route('/categories/manage')
def manage():
    return render_template('categories/manage.html', title='管理')


@categories.route('/categories/travel')
def travel():
    return render_template('categories/travel.html', title='旅行')


@categories.route('/categories/work')
def work():
    return render_template('categories/work.html', title='工作')
