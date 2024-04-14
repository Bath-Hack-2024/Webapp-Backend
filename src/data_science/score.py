import numpy as np
import math

def getCurrentScore(cloudCoverPercentage = None, fogCoverPercentage = None , moonPhase = None, moonVisible = None, dewPointSpread = None, wobble=None):
    """
    gets the current score for a location based on the conditions that impact the quality of astral photography

    Args:
        cloudCoverPercentage (float): cloud cover percentage
        fogCoverPercentage (float): fog cover percentage
        moonPhase (str): the current phase of the moon
        moonVisible (bool): is the onn visible
        dewPointSpread (float): the current dew point spread level
        wobble (float) : default = None. Atmospheric wobble

    Raises:
        TypeError: for cloud cover
        TypeError: for fog cover
        TypeError: tests moon phase
        TypeError: moon visibility 
        TypeError: dew point spread
        TypeError: Wobble error 

    Returns:
        int: score 
    """
    
    score = 100.0
    if moonVisible is not None:
        #deals with the moon. If it isn't visible, no impact, otherwise score decreases with the brightness (phase)
        if not moonVisible:
            pass
        else:
            if moonPhase=="New Moon":
                score *= 0.8
            elif moonPhase=="Waxing Crescent" or moonPhase=="Waning Crescent":
                score *= 0.65
            elif moonPhase=="First Quarter" or moonPhase=="Last Quarter":
                score *= 0.5
            elif moonPhase=="Waxing Gibbous" or moonPhase=="Waning Gibbous":
                score *= 0.35
            elif moonPhase=="Full Moon":
                score *= 0.2

    if cloudCoverPercentage is not None:
        #Accounts for cloud cover percentage - exponentially lower the higher the cloud cover
        score *= (10**(-0.01*cloudCoverPercentage))

    if fogCoverPercentage is not None:
        #Accounts for fog cover percentage - exponentially lower but not quite as quick as cloud cover with more fog
        score *= (10**(-0.005*fogCoverPercentage))
        
    if dewPointSpread is not None:
        #Accounts for Dew Point spread. Higher absolute values of dew point spread are better
        score *= (10**((0.00006*math.fabs(dewPointSpread))-0.006))
    
    #Wobble
    if wobble is not None:
        score *= np.min([1, 1.05-(0.01*wobble)])
    
    return score