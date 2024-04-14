import numpy
from scipy.interpolate import interp1d

def timeline(times):
    '''
    This function takes in a list of times and returns the number of points and the index of the time 30 mins before the latest datapoint.
    INPUTS:
    times: List of times in seconds since epoch
    OUTPUTS:
    numPoints: Number of points in the list
    timeInd: Index of the time 30 mins before the latest datapoint
    '''
    timeBefore = times[len(times)-1]-(60*30)
    timesDiff = numpy.array([])
    #Find the closest time in the list to 30 mins before latest datapoint
    for i in range(len(times)):
        #print(numpy.absolute(times[i] - timeBefore))
        timesDiff = numpy.append(timesDiff, [numpy.absolute(times[i] - timeBefore)])
    #print(len(timesDiff))
    timeInd = numpy.argmin(timesDiff)
    timeStart = times[timeInd]
    if numpy.absolute((timeBefore - timeStart)/60) > 5:
        print("Data too old or too young for accurate prediction, wait longer or shorter.")
        return None
        raise ValueError
    numPoints = len(times) - timeInd
    return [numPoints, timeInd]

def gradientalOne(pressureData, numPoints, times, timeInd):
    '''
    This function takes in a list of pressure data and returns the gradients of the pressure data and the corresponding times.
    INPUTS:
    pressureData: List of pressure data
    numPoints: Number of points in the list
    times: List of times in seconds since epoch
    timeInd: Index of the time 30 mins before the latest datapoint
    OUTPUTS:
    gradients: List of gradients of the pressure data
    timeArray: List of times corresponding to the gradients
    '''
    match numPoints:
        case numPoints if numPoints >= 10:
            timeArray = numpy.linspace(times[timeInd], times[len(times)-1], 100)
            pressureDataCut = pressureData[timeInd:len(pressureData)]
            interp_func = interp1d(times[timeInd:len(times)], pressureDataCut)
            newPressure = interp_func(timeArray)
            gradients = []
            for i in range(0, len(newPressure)-5, 5):
                gradient = (newPressure[i+5] - newPressure[i]) / 5
                gradients.append(gradient)
            return [gradients, timeArray]
        case numPoints if numPoints < 10:
            print('Not enough values for an accurate prediction')
            raise ValueError('Fuck you')

def gradientalTwo(gradients):
    '''
    Function that finds if any of the gradients are anomalous
    INPUTS:
    gradients
    OUTPUTS:
    Average gradient across all'''
    twoGrad = numpy.diff(gradients)

    ind = ([twoGrad.index(x) for x in twoGrad if x>10])
    if ind != None:
        for i in ind:
            gradients[i-1:i] = None
    average = numpy.average(gradients)
    return average

def get_futurecast(time, pressure):
    [numPoints, timeInd] = timeline(time)
    [gradOne, timeArray] = gradientalOne(pressure, numPoints, time, timeInd)
    gradAvg = gradientalTwo(gradOne)

    return gradAvg