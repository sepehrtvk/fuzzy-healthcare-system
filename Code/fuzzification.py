class age_fuzzification:
    def __init__(self):
        pass

    def age_young(self,x):
        if x <= 29:
            return 1
        if 29 < x <= 38:
            return -0.111 * x + 4.222
        else :
            return 0

    def age_mild(self,x):
        if 33 < x < 38:
            return 0.2 * x - 6.600
        if x == 38:
            return 1
        if 38 < x < 45:
            return -0.143 * x + 6.429
        else :
            return 0

    def age_old(self,x):
        if 40 < x < 48:
            return 0.125 * x - 5.000
        if x == 48 : 
            return 1
        if 48 < x < 58:
            return -0.1 * x + 5.800
        else :
            return 0

    def age_veryold(self,x):
        if x <= 52:
            return 0
        if 52 < x < 60:
            return 0.125 * x - 6.500
        else :
            return 1
    
    def calc_fuzzy_age(self,age):
        return dict (
            young=self.age_young(age),
            mild=self.age_mild(age),
            old=self.age_old(age),
            very_old=self.age_veryold(age)
        )

class bloodPressure_fuzzification:
    def __init__(self):
        pass

    def bloodPressure_low(self,x):
        if 0 <= x < 111:
            return 1
        if 111 <= x <= 134:
            return -0.043 * x + 5.862
        else :
            return 0

    def bloodPressure_medium(self,x):
        if 127 <= x < 139:
            return 0.083 * x - 10.583
        if x == 139 :
            return 1
        if 139 <= x < 153:
            return -0.071 * x + 10.929
        else :
            return 0

    def bloodPressure_high(self,x):
        if 142 <= x < 157:
            return 0.067 * x - 9.467
        if x == 157 :
            return 1
        if 157 <= x < 172:
            return -0.067 * x + 11.467
        else :
            return 0

    def bloodPressure_veryhigh(self,x):
        if 0 <= x <= 154:
            return 0
        if 154 < x < 171:
            return 0.059 * x - 9.059
        else :
            return 1
    
    def calc_fuzzy_bloodPressure(self,bloodPressure):
        return dict (
            low=self.bloodPressure_low(bloodPressure),
            medium=self.bloodPressure_medium(bloodPressure),
            high=self.bloodPressure_high(bloodPressure),
            very_high=self.bloodPressure_veryhigh(bloodPressure)
        )

class bloodSugar_fuzzification:
    def __init__(self):
        pass

    def bloodSugar_veryhigh(self,x):
        if 120 <= x :
            return 1
        else:
            return 0
    
    def calc_fuzzy_bloodSugar(self,bloodSugar):
        return dict (
           true = self.bloodSugar_veryhigh(bloodSugar),
           false = self.bloodSugar_veryhigh(bloodSugar)
        )

class cholestrol_fuzzification:
    def __init__(self):
        pass

    def cholestrol_low(self,x):
        if 0 <= x < 151:
            return 1
        if 151 <= x < 197:
            return -0.022 * x + 4.283
        else :
            return 0

    def cholestrol_medium(self,x):
        if 188 <= x < 215:
            return 0.037 * x - 6.963
        if x == 215 :
            return 1
        if 215 <= x < 250:
            return -0.029 * x + 7.143
        else :
            return 0

    def cholestrol_high(self,x):
        if 217 <= x < 263:
            return 0.022 * x - 4.717
        if x == 263 :
            return 1
        if 263 <= x < 307:
            return -0.023 * x + 6.977
        else :
            return 0

    def cholestrol_veryhigh(self,x):
        if 0 <= x < 281:
            return 0
        if 281 <= x < 347:
            return 0.015 * x - 4.258
        else :
            return 1
    
    def calc_fuzzy_cholestrol(self,cholestrol):
        return dict (
            low=self.cholestrol_low(cholestrol),
            medium=self.cholestrol_medium(cholestrol),
            high=self.cholestrol_high(cholestrol),
            very_high=self.cholestrol_veryhigh(cholestrol)
        )

class heartRate_fuzzification:
    def __init__(self):
        pass

    def heartRate_low(self,x):
        if 0 <= x <= 100:
            return 1
        if 100 < x <= 141:
            return -0.024 * x + 3.439
        else :
            return 0

    def heartRate_medium(self,x):
        if 111 < x < 152:
            return 0.024 * x - 2.707
        if x == 152 :
            return 1
        if 152 <= x < 194:
            return -0.024 * x + 4.619
        else :
            return 0

    def heartRate_high(self,x):
        if 0 < x <= 152:
            return 0
        if 152 <= x < 210:
            return 0.017 * x - 2.621
        else :
            return 1

    def calc_fuzzy_heartRate(self,heartRate):
        return dict (
            low=self.heartRate_low(heartRate),
            medium=self.heartRate_medium(heartRate),
            high=self.heartRate_high(heartRate),
        )

class ECG_fuzzification:
    def __init__(self):
        pass

    def ECG_normal(self,x):
        if -0.5 <= x <= 0:
            return 1
        if 0 < x <= 0.4:
            return -2.500 * x + 1.000
        else :
            return 0

    def ECG_abnormal(self,x):
        if 0.2 <= x <= 1:
            return 1.250 * x - 0.250
        if 1 < x <= 1.8:
            return -1.250 * x + 2.250
        else :
            return 0

    def ECG_hypertrophy(self,x):
        if x <= 1.4:
            return 0
        if 1.4 < x <= 1.9:
            return 2.000 * x - 2.800
        else :
            return 1

    def calc_fuzzy_ECG(self,ECG):
        return dict (
            normal=self.ECG_normal(ECG),
            abnormal=self.ECG_abnormal(ECG),
            hypertrophy=self.ECG_hypertrophy(ECG),
        )

class oldPeak_fuzzification:
    def __init__(self):
        pass

    def oldPeak_low(self,x):
        if 0 <= x <= 1:
            return 1
        if 1 < x < 2:
            return -1.000 * x + 2.000
        else :
            return 0

    def oldPeak_risk(self,x):
        if 1.5 <= x < 2.8:
            return 0.769 * x - 1.154
        if x == 2.8 :
            return 1
        if 2.8 < x <= 4.2:
            return -0.714 * x + 3.000
        else :
            return 0

    def oldPeak_terrible(self,x):
        if 0 < x <= 2.5:
            return 0
        if 2.5 < x < 4:
            return 0.667 * x - 1.667
        else :
            return 1

    def calc_fuzzy_oldPeak(self,oldPeak):
        return dict (
            low=self.oldPeak_low(oldPeak),
            risk=self.oldPeak_risk(oldPeak),
            terrible=self.oldPeak_terrible(oldPeak),
        )

class outputsick_fuzzification:
    def __init__(self):
        pass

    def outputsick_sick3(self,x):
        if 0 <= x <= 0.25:
            return 1
        if 0.25 < x < 1:
            return -1.333 * x + 1.333
        else :
            return 0

    def outputsick_sick1(self,x):
        if 0 <= x <= 1:
            return x 
        if 1 < x <= 2:
            return -1.000 * x + 2.000
        else :
            return 0

    def outputsick_sick2(self,x):
        if 1 <= x <= 2:
            return 1.000 * x - 1.000
        if 2 < x <= 3:
            return -1.000 * x + 3.000
        else :
            return 0

    def outputsick_healthy(self,x):
        if 2 <= x <= 3:
            return 1.000 * x - 2
        if 3 < x < 4:
            return -1.000 * x + 4.000
        else :
            return 0

    def outputsick_sick4(self,x):
        if 0 <= x <= 3:
            return 0
        if 3 < x < 3.75:
            return 1.333 * x - 4.000
        else :
            return 1
    
class chest_pain_fuzzification:
    def __init__(self):
        pass

    def typical_angina(self,x):
        if x == 1 :
            return 1
        else:
            return  0
    def atypical_angina(self,x):
        if x == 2 :
            return 1
        else:
            return  0
    def non_anginal_pain(self,x):
        if x == 3 :
            return 1
        else:
            return  0
    def asymptomatic(self,x):
        if x == 4 :
            return 1
        else:
            return  0

    def calc_fuzzy_chest_pain(self,num):
        return dict(
            typical_anginal= self.typical_angina(num),
            atypical_anginal=self.atypical_angina(num),
            non_aginal_pain=self.non_anginal_pain(num),
            asymptomatic = self.asymptomatic(num)
        )
            
class exercise_fuzzification:
    def __init__(self):
        pass
    def true(self,x):
        if x == 1:
            return 1
        else: 
            return 0
    def false(self,x):
        if x == 0:
            return 1
        else: 
            return 0
    def calc_fuzzy_exercise(self,num):
        return dict(
            true=self.true(num),
            false=self.false(num)
        )

class thallium_fuzzification:
    def __init__(self):
        pass
    def normal(self,x):
        if x == 3 :
            return 1
        else: 
            return 0
    def medium(self,x):
        if x == 6 :
            return 1
        else: 
            return 0
    def high(self,x):
        if x == 7 :
            return 1
        else: 
            return 0
    def calc_fuzzy_thallium(self,num):
       return dict(
           normal = self.normal(num),
           medium = self.medium(num),
           high = self.high(num)
       )

class sex_fuzzification:
    def __init__(self):
        pass
    def male(self,x):
        if x == 0:
            return 1
        else: 
            return 0
    def female(self,x):
        if x == 1:
            return 1
        else: 
            return 0
    def calc_fuzzy_sex(self,num):
        return dict(
            male=self.male(num),
            female=self.female(num)
        )

