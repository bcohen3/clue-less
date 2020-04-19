from unittest import TestCase

from app.server.domain.deck import Deck
from app.server.domain.suspect_card import SuspectCard


class TestDeck(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = Deck()

    def test_gets_card_by_id(self):
        test_card = SuspectCard(0, 'Miss Scarlet')
        card_with_id_0 = self.deck.get_card_data_by_id(0)
        self.assertEqual(card_with_id_0.__dict__, test_card.__dict__)

    def test_chunk_produces_the_correct_number_of_chunks(self):
        number_of_chunks = 6
        shuffled_deck = self.deck.chunk_cards(number_of_chunks)
        self.assertEqual(number_of_chunks, len(shuffled_deck))

    def test_chunk_produces_the_correct_size_chunks(self):
        number_of_chunks = 6
        shuffled_deck = self.deck.chunk_cards(number_of_chunks)
        self.assertEqual(4, len(shuffled_deck[0]))
        self.assertEqual(4, len(shuffled_deck[1]))
        self.assertEqual(4, len(shuffled_deck[2]))
        self.assertEqual(3, len(shuffled_deck[3]))
        self.assertEqual(3, len(shuffled_deck[4]))
        self.assertEqual(3, len(shuffled_deck[5]))

    def test_shuffle_shuffles_cards_without_changing_cards_by_id(self):
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards_by_id, self.deck.cards)
