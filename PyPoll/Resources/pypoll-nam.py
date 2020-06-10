voterid, candidate_name

candidate_vote = {
  "Khan": 10,
  "Nam": 5,
  "Thao": 20
}

candidate_vote = {:}
for row in csvinput:
    voteID = row[0]
    candidate = row[2]
    if (candidate_vote[candidate] != null):
      candidate_vote[candidate] += 1
    else:
      candidate_vote[candidate] = 1

    
        
total_vote = sum(candidate_vote.values())
total_candidate = len(candidate_vote)
percentage_vote = {:}
max_vote = 0
candidate_with_max_vote = ""
for c in candidate_vote:
  percentage_vote[c] = candidate_vote[c] / total_vote
  if (candidate_vote[c] > max_vote):
    max_vote = candidate_vote[c]
    candiate_with_max_vote = c