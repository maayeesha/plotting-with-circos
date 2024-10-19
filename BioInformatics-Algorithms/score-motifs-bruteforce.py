# Copy your Consensus(Motifs) function here.

# Copy your Count(Motifs) function here.

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    score = 0
    k = len(Motifs[0])
    t = len(Motifs)
    consensus = Consensus(Motifs,k,t)
    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score
# Insert your Count(Motifs) function here.

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs,k,t):
    ans = []
    profile = Profile(Motifs,k,t)
    for j in range(k):
        mx = 0
        con_symbol = ''
        for symbol in "ACGT":
            if profile[symbol][j]>mx:
                mx = profile[symbol][j]
                con_symbol = symbol
        ans.append(con_symbol)
    return ''.join(ans)
            
    
    
def Profile(Motifs,k,t):
    profile = {}
    profile = Count(Motifs,k,t)
    
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] /= t
    return profile

def Count(Motifs,k,t):
    count = {} # initializing the count dictionary
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
   
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
                
        
    return count
    
