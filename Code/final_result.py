import fuzzification
import inference
import defuzzification


chest_pain_fuzzification = fuzzification.chest_pain_fuzzification()
bloodPressure_fuzzification = fuzzification.bloodPressure_fuzzification()
cholestrol_fuzzification = fuzzification.cholestrol_fuzzification()
bloodSugar_fuzzification = fuzzification.bloodSugar_fuzzification()
ECG_fuzzification  = fuzzification.ECG_fuzzification()
heartRate_fuzzification = fuzzification.heartRate_fuzzification()
exercise_fuzzification = fuzzification.exercise_fuzzification()
oldPeak_fuzzification = fuzzification.oldPeak_fuzzification()
thallium_fuzzification = fuzzification.thallium_fuzzification()
sex_fuzzification = fuzzification.sex_fuzzification()
age_fuzzification = fuzzification.age_fuzzification()

inferenceLogic = inference.inference()

defuzzificationLogic = defuzzification.defuzzification()

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        fuzzy_chest_pain = chest_pain_fuzzification.calc_fuzzy_chest_pain(
            int(input_dict['chest_pain']))
        fuzzy_blood_pressure = bloodPressure_fuzzification.calc_fuzzy_bloodPressure(
            int(input_dict['blood_pressure']))
        fuzzy_cholesterol = cholestrol_fuzzification.calc_fuzzy_cholestrol(
            int(input_dict['cholestrol']))
        fuzzy_blood_sugar = bloodSugar_fuzzification.calc_fuzzy_bloodSugar(
            int(input_dict['blood_sugar']))
        fuzzy_ECG = ECG_fuzzification.calc_fuzzy_ECG(
            float(input_dict['ecg']))
        fuzzy_maximum_heart_rate = heartRate_fuzzification.calc_fuzzy_heartRate(
            int(input_dict['heart_rate']))
        fuzzy_exercise = exercise_fuzzification.calc_fuzzy_exercise(
            int(input_dict['exercise']))
        fuzzy_old_peak = oldPeak_fuzzification.calc_fuzzy_oldPeak(
            float(input_dict['old_peak']))
        fuzzy_thallium = thallium_fuzzification.calc_fuzzy_thallium(
            int(input_dict['thallium_scan']))
        fuzzy_sex = sex_fuzzification.calc_fuzzy_sex(
            int(input_dict['sex']))
        fuzzy_age = age_fuzzification.calc_fuzzy_age(
            int(input_dict['age']))

        fuzzy_sick = inferenceLogic.inference(fuzzy_chest_pain, fuzzy_blood_pressure, fuzzy_cholesterol,
                                         fuzzy_blood_sugar, fuzzy_ECG, fuzzy_maximum_heart_rate, fuzzy_exercise, fuzzy_old_peak, fuzzy_thallium, fuzzy_sex, fuzzy_age)
        return defuzzificationLogic.defuzzify(fuzzy_sick)