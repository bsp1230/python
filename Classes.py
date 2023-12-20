class Match:
  def __init__(this, score, overs):
    this.score = score
    this.overs = overs 
  def players(this,p1,p2):
    print('Batsman',p1)
    print('Bowler',p2)

match = Match(450,36.2);

print('Score',match.score)
print('Overs',match.overs)
match.players('surya','vinay');

#del match.overs
#print('Overs',match.overs)