def correctness(bobs_decisions, expert_decisions): 
    points = 0
    for i in range(0,len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            points += 1 
        elif bobs_decisions[i] == '?' or expert_decisions[i] == '?':
            points += 0.5  
    return points
