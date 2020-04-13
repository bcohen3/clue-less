from flask import render_template, Blueprint, request
from app.forms.move_form import *
from app.domain.game_rules import GameRules

blueprint = Blueprint('pages', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = MoveForm(request.form)
    game_rules = GameRules()
    move = None

    if request.method == 'POST':
        print(form.data)

        if form.validate() is not True:
            print(form.errors)
            return render_template('pages/home.html', form=form)

        entered_move = form.data['move']
        print("Game rules for {}: {}".format(entered_move, game_rules.move(entered_move)))
        move = game_rules.move(entered_move)

    return render_template('pages/home.html', form=form, move=move)
