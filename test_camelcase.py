from unittest import TestCase

from camelcase import camelcase, removeSpecialCharacters


class TestCamelCase(TestCase):
    def test_with_one_word(self):
        sentence = 'oneword'
        result = camelcase(sentence)
        self.assertEqual(result, sentence)

    def test_with_two_words(self):
        sentence = 'two words'
        result = camelcase(sentence)
        self.assertEqual(result, 'twoWords')

    def test_first_number(self):
        sentence = '2 words'
        result = camelcase(sentence)
        self.assertEqual(result, '2Words')

    def test_lots_of_words(self):
        sentence = 'a thousand words is only worth one picture'
        result = camelcase(sentence)
        self.assertEqual(result, 'aThousandWordsIsOnlyWorthOnePicture')

    def test_empty_string(self):
        sentence = ''
        result = camelcase(sentence)
        self.assertEqual(result, '')


    def test_string_with_leading_spaces(self):
        sentence = '      can can si you can'
        result = camelcase(sentence)
        self.assertEqual(result, 'canCanSiYouCan')

    def test_string_with_emoji(self):
        sentence = 'can 🐒 si you can'
        result = camelcase(sentence)
        self.assertEqual(result, 'can🐒SiYouCan')

    def test_string_with_mix_of_capatilizatoin(self):
      sentence = 'cAn cAn Si yoU can'
      result = camelcase(sentence)
      self.assertEqual(result, 'canCanSiYouCan')

    def test_remove_special_characters(self):
      sentence = 'cAn c˚¬∑åƒ🐳🐳🐳An Si yoU can'
      result = removeSpecialCharacters(sentence)
      self.assertEqual(result, 'cAncAnSiyoUcan')