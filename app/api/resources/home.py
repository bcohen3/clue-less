from flask import render_template, Blueprint, request
from app.forms.move_form import *
from app.domain.game_runner import GameRunner

blueprint = Blueprint('pages', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = MoveForm(request.form)
    game_runner = GameRunner()
    entered_move = None

    if request.method == 'POST':
        print(form.data)

        if form.validate() is not True:
            print(form.errors)
            return render_template('pages/home.html', form=form)

        entered_move = form.data['move']
        game_runner.test_method()

    return render_template('pages/home.html', form=form, move=entered_move)
