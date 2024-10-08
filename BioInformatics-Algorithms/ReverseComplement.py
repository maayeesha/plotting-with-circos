    # Input:  A DNA string Pattern
    # Output: The reverse complement of Pattern
    def ReverseComplement(Pattern):   
        # your code here
        Pattern = Reverse(Pattern)
        Pattern = Complement(Pattern)
        return Pattern

    # Copy your Reverse() function here.
    def Reverse(Pattern):
        rev = ""
        for i in range(len(Pattern)-1,-1,-1):
            rev += Pattern[i]
        return rev

    # Copy your Complement() function here.
    def Complement(Pattern):
        # your code here
        comp = ""
        for i in Pattern:
            if i == 'A':
                comp += 'T'
            elif i == 'T':
                comp += 'A'
            elif i == 'C':
                comp += 'G'
            else:
                comp += 'C'
        return comp
