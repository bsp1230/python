class Match:
  def __init__(this, score, overs):
    this.score = score
    this.overs = overs
  def players(this,p1,p2):
    print('Batsman',p1)
    print('Bowler',p2)

class Stats(Match):  
  def __init__(this,score, overs,wickets,extras):
    super().__init__(score,overs)
    this.wickets = wickets
    this.extras = extras
  def details(this):
    print('Wickets',this.wickets)
    print('Extras',this.extras)

stats = Stats(450,20,7,21)

print('Score',stats.score)
print('Overs',stats.overs)
stats.players('Surya','Kiran');
stats.details()

