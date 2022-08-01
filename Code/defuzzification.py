from fuzzification import outputsick_fuzzification

outputsick_fuzzification2 = outputsick_fuzzification()

class defuzzification:
    def __init__(self):
        pass
    
    def defuzzify(self, x):
        n = 300
        delta = 1. / n
        points = [0. + i * delta for i in range(4*n)]

        numerator = 0.
        denominator = 0.
        for point in points:
            s1 = outputsick_fuzzification2.outputsick_sick1(point)
            if s1 > x['outputsick_sick1']:
                s1 = x['outputsick_sick1']
            s2 = outputsick_fuzzification2.outputsick_sick2(point)
            if s2 > x['outputsick_sick2']:
                s2 = x['outputsick_sick2']
            s3 = outputsick_fuzzification2.outputsick_sick3(point)
            if s3 > x['outputsick_sick3']:
                s3 = x['outputsick_sick3']
            s4 = outputsick_fuzzification2.outputsick_sick4(point)
            if s4 > x['outputsick_sick4']:
                s4 = x['outputsick_sick4']
            sh = outputsick_fuzzification2.outputsick_healthy(point)
            if sh > x['outputsick_healthy']:
                sh = x['outputsick_healthy']

            res = max(s1, s2, s3, s4, sh)
            numerator += res * point * delta
            denominator += res * delta
        try:
            centerOfGravity = numerator / denominator
        except ZeroDivisionError:
            centerOfGravity = 0

        result = []

        if centerOfGravity < 1.78 :
            result.append('healthy')

        if 1 <= centerOfGravity <= 2.51:
            result.append('sick1')

        if 1.78 <= centerOfGravity < 3.25:
            result.append('sick2')

        if 1.5 <= centerOfGravity <= 4.5:
            result.append('sick3')

        if 3.25 <= centerOfGravity:
            result.append('sick4')

        result.append(str( round(centerOfGravity,3)))

        return " & ".join(result)

