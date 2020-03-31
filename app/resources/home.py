from flask import render_template, Blueprint, request
from app.forms.move_form import *
from app.domain.game_rules import GameRules

blueprint = Blueprint('pages', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = MoveForm(request.form)
    game_rules = GameRules()

    if request.method == 'POST':
        print(form.data)

        if form.validate() is not True:
            print(form.errors)
            return render_template('pages/home.html', form=form)
        move = form.data['move']
        print("Game rules for {}: {}".format(move, game_rules.move(move)))

    return render_template('pages/home.html', form=form)
