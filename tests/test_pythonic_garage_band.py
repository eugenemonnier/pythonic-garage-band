from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band
from pythonic_garage_band.pythonic_garage_band import Musician

def test_version():
    assert __version__ == '0.1.0'

def test_band_name():
  july_talk = Band('July Talk')
  actual = july_talk.band_name
  expected = 'July alk'
  actual == expected

def test_musician_name():
  peter_dreimanis = Musician('July Talk', 'Peter Dreimanis')
  actual = peter_dreimanis.member_name
  expected = 'eter Dremanis'
  actual == expected

def test_members_list():
  leah_fey = Musician('July Talk', 'Leah Fey')
  actual = leah_fey.members
  expected = ['Peter Dremanis', 'Leah Faey']
  actual == expected

def test_play_solo():
  ian_docherty = Musician('July Talk', 'Ian Docherty')
  actual = ian_docherty.play_solo()
  print(actual)
  expected = 'Play a solo Peter.'
  actual == expected

# def test_band_members():
#   july_talk = Band('July Talk', ['Peter Dreimanis', 'Lead Fey', 'Ian Docherty', 'Josh Warburton', 'Danny Miles'])
#   actual = july_talk.members
#   expected = ['Peter Dreimanis', 'Lead Fey', 'Ian Docherty', 'Josh Warburton', 'Danny Miles']
#   actual == expected

