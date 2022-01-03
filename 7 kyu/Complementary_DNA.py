def DNA_strand(dna):
    lis = list(dna)
    lisa = []
    for x in range(0,len(lis)):
        if lis[x] == 'A':
            print(lis[x])
            lisa.append('T')
        elif lis[x] == 'T':
            lisa.append('A')
        elif lis[x] == 'C':
            lisa.append('G')
        elif lis[x] == 'G':
            lisa.append('C')
    return ''.join(lisa)
  
  """
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
  """
