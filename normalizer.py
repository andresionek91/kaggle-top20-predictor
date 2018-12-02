# defining the min and max scores for normalization
MIN_SCORE, MAX_SCORE = -8.054542604814351, 5.494637181092647

def normalize(score):
    """
    Normalize to get values between 0 and 1000
    """
    return int((score - MIN_SCORE) / (MAX_SCORE - MIN_SCORE) * 1000)
