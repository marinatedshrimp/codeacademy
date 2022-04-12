from sqlalchemy import false, true


class Geometry:
    def __init__(self):
        pass

    def distance(a1, a2, b1, b2):
        return ((b1 - a1) ** 2 + (b2 - a2) ** 2) ** 0.5

    def middle(a1, a2, b1, b2):
        return f"({(a1 + a2) / 2}, {(b1 + b2) / 2})"
    
    def triPer(a1, a2, b1, b2, c1, c2):
        return (((b1 - a1) ** 2 + (b2 - a2) ** 2) ** 0.5) + (((c1 - b1) ** 2 + (c2 - b2) ** 2) ** 0.5) + (((a1 - c1) ** 2 + (a2 - c2) ** 2) ** 0.5)

    def triIso(a1, a2, b1, b2, c1, c2): 
        if ((b1 - a1) ** 2 + (b2 - a2) ** 2) ** 0.5 == ((c1 - b1) ** 2 + (c2 - b2) ** 2) ** 0.5:
            return true
        elif ((b1 - a1) ** 2 + (b2 - a2) ** 2) ** 0.5 == ((a1 - c1) ** 2 + (a2 - c2) ** 2) ** 0.5:
            return true
        elif ((c1 - b1) ** 2 + (c2 - b2) ** 2) ** 0.5 == ((a1 - c1) ** 2 + (a2 - c2) ** 2) ** 0.5:
            return true
        else:
            return false
    
    