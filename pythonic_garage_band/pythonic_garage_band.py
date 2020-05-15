class Band:
  def __init__(self, band_name):
    self.band_name = band_name
    self.members = []

  def play_solo(self):
    play_a_solo = str()
    for name in self.members:
      play_a_solo += f'Play a solo {name}. '
    return play_a_solo

class Musician(Band):
  def __init__(self, band_name, member_name):
    super().__init__(band_name)
    self.member_name = member_name
    self.members.append(member_name)
  

  def get_instrument(self, instrument):
    print(f'{self.member_name} picks up their {instrument}')