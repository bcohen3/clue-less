from unittest import TestCase

from app.server.domain.deck import Deck
from app.server.domain.envelope import Envelope
from app.server.domain.game_runner import GameRunner
from app.server.domain.player import Player
from app.server.domain.room_card import RoomCard
from app.server.domain.suggestion import Suggestion
from app.server.domain.suspect_card import SuspectCard
from app.server.domain.weapon_card import WeaponCard


class TestGameRunner(TestCase):
    @classmethod
    def setUpClass(cls):
        deck = Deck()
        envelope = Envelope()
        player_zero = Player(0, 0, 0, [SuspectCard(0, 'Miss Scarlet')])
        player_one = Player(1, 1, 1, [WeaponCard(8, 'lead pipe')])
        player_two = Player(2, 2, 2, [RoomCard(19, 'library')])
        cls.player_list = [player_zero, player_one, player_two]
        cls.game_runner = GameRunner(deck, envelope, cls.player_list, 3)

    def test_sets_the_first_player_as_the_current_player_when_game_starts(self):
        self.assertEqual(0, self.game_runner.current_player.id)

    def test_shows_card_when_players_holding_one_suggested_card(self):
        suspect_card = SuspectCard(1, 'Mrs. White')
        weapon_card = WeaponCard(8, 'lead pipe')
        room_card = RoomCard(18, 'study')
        suggestion = Suggestion(suspect_card, weapon_card, room_card)
        card_held_by_player = self.game_runner.check_suggestion(suggestion)

        self.assertEqual(weapon_card.id, card_held_by_player.id)

    def test_shows_card_when_players_holding_multiple_suggested_card(self):
        suspect_card = SuspectCard(1, 'Mrs. White')
        weapon_card = WeaponCard(8, 'lead pipe')
        room_card = RoomCard(19, 'library')
        suggestion = Suggestion(suspect_card, weapon_card, room_card)
        card_held_by_player = self.game_runner.check_suggestion(suggestion)

        self.assertEqual(weapon_card.id, card_held_by_player.id)

    def test_no_player_holding_any_suggested_card(self):
        suspect_card = SuspectCard(1, 'Mrs. White')
        weapon_card = WeaponCard(9, 'rope')
        room_card = RoomCard(18, 'study')
        suggestion = Suggestion(suspect_card, weapon_card, room_card)
        card_held_by_player = self.game_runner.check_suggestion(suggestion)

        self.assertIsNone(card_held_by_player)

    def test_shows_card_when_current_player_only_one_holding_suggested_card(self):
        suspect_card = SuspectCard(0, 'Miss Scarlet')
        weapon_card = WeaponCard(9, 'rope')
        room_card = RoomCard(18, 'study')
        suggestion = Suggestion(suspect_card, weapon_card, room_card)
        card_held_by_player = self.game_runner.check_suggestion(suggestion)

        self.assertEqual(0, card_held_by_player.id)

    def test_ends_game_when_correct_accusation_made(self):
        suspect_card = SuspectCard(0, 'Miss Scarlet')
        weapon_card = WeaponCard(9, 'rope')
        room_card = RoomCard(18, 'study')
        accusation = Suggestion(suspect_card, weapon_card, room_card, True)

        self.game_runner.envelope.suspect_card = suspect_card
        self.game_runner.envelope.weapon_card = weapon_card
        self.game_runner.envelope.room_card = room_card

        is_accusation_correct = self.game_runner.check_accusation(accusation)

        self.assertTrue(is_accusation_correct)
        self.assertTrue(self.game_runner.current_player.is_winner)

    def test_player_loses_when_incorrect_accusation_made(self):
        self.game_runner.current_player.is_winner = False
        suspect_card_accusation = SuspectCard(0, 'Miss Scarlet')
        weapon_card = WeaponCard(9, 'rope')
        room_card = RoomCard(18, 'study')
        accusation = Suggestion(suspect_card_accusation, weapon_card, room_card, True)

        suspect_card_envelope = SuspectCard(1, 'Mrs. White')
        self.game_runner.envelope.suspect_card = suspect_card_envelope
        self.game_runner.envelope.weapon_card = weapon_card
        self.game_runner.envelope.room_card = room_card

        is_accusation_correct = self.game_runner.check_accusation(accusation)

        self.assertFalse(is_accusation_correct)
        self.assertTrue(self.game_runner.current_player.is_loser)

    # TODO check moves player correctly
    # def test_updates_current_player_after_move(self):
    #     self.fail()

    # TODO check moves weapon correctly

    def test_updates_current_player_when_no_players_lost(self):
        self.game_runner.current_player = self.player_list[0]
        self.player_list[1].is_loser = False
        self.game_runner.update_current_player()

        new_current_player = self.game_runner.current_player
        self.assertEqual(1, new_current_player.id)

    def test_updates_current_player_when_next_player_lost(self):
        self.game_runner.current_player = self.player_list[0]
        self.player_list[1].is_loser = True
        self.game_runner.update_current_player()

        new_current_player = self.game_runner.current_player
        self.assertEqual(2, new_current_player.id)
