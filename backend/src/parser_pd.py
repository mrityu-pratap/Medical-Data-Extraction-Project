from backend.src.parser_generic import MedicalDocParser
import re
class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_phone_number(),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination(),
            'medical_problems': self.get_medical_problems()
        }

    def get_patient_name(self):
        pattern = "Patient Information(.*?)\(\d{3}\)"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            matches[0].strip()

            match = matches[0].replace('Birth Date\n', '').strip()
            pattern1 = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
            date_matches = re.findall(pattern1, match, flags=re.DOTALL)
            date = date_matches[0][0]
            name = match.replace(date, '').strip()
            return name

    def get_phone_number(self):
        pattern = "Patient Information(.*?)(\(\d{3}\).\d{3}\-\d{4})"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0][1]

    def get_hepatitis_b_vaccination(self):
        pattern = "vaccination\?.*(Yes|No)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()

    def get_medical_problems(self):
        pattern = "List any Medical Problems .*?:(.*)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()


if __name__ == '__main__':
    document_text = '''
    17/12/2020
    
    Patient Medical Record
    
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 .
    United States Height:
    190
    In Casc of Emergency
    7 ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    
    Genera! Medical History
    
    a
    
    a
    
    a ea A CE i a
    
    Chicken Pox (Varicella): Measies:
    
    IMMUNE IMMUNE
    
    Have you had the Hepatitis B vaccination?
    No
    
    List any Medical Problems (asthma, seizures, headaches):
    
    Migraine
    '''

    pdp = PatientDetailsParser(document_text)
    print(pdp.parse())
