def to_rna(dna_strand):
    nueva_lista=""
    for i in dna_strand:
        if i == "G":
            i="C"
        elif i =="C":
            i="G" 
        elif i =="T":
            i="A"  
        elif i=="A" :
            i="U" 
        nueva_lista=nueva_lista + i 
    return nueva_lista        
    pass

    
