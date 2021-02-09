### Program that calculates total area of two rectangles
# Input: cooridnates of lower-left and upper-right corners of the rectangles.
# Output: area

def computeArea(A, B, C, D, E, F, G, H):
    w1 = C-A
    h1 = D-B
    A1 = w1*h1
    w2 = G-E
    h2 = H-F
    A2 = w2*h2
    
    At = A1 + A2
    
    if (G<=A) or (H<=B) or (C<=E) or (D<=F): # No overlap
        return At
    else:
        x1 = max(A,E)
        x2 = min(G,C)
        y1 = max(B,F)
        y2 = min(D,H)
        
        At-= abs(x2-x1)*abs(y2-y1)
       
    return At

print(computeArea(2,3,4,4,-2,3,4,6))
