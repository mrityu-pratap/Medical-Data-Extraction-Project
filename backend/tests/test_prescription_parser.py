from src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    
    Name: Marta Sharapova Date: 5/11/2022
    
    Address: 9 tennis court, new Russia, DC
    
    Prednisone 20 mg, Lialda 2.4 gram
    
    Directions:
    
    Prednisone, Take 5 mg every 3 days, Finish in 2.5 weeks and Lialda, take 2 pill everyday for 1 month
    
    Refill: 2 times
    '''
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_2_virat():
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
    '''
    return PrescriptionParser(document_text)

def test_get_name(doc_1_maria, doc_2_virat):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_field('patient_name') == 'Virat Kohli'

def test_get_address(doc_1_maria, doc_2_virat):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'

def test_get_medicines(doc_1_maria, doc_2_virat):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg, Lialda 2.4 gram'
    assert doc_2_virat.get_field('medicines') == 'Omeprazole 40 mg'

def test_get_directions(doc_1_maria, doc_2_virat):
    assert doc_1_maria.get_field('directions') == 'Prednisone, Take 5 mg every 3 days, Finish in 2.5 weeks and Lialda, take 2 pill everyday for 1 month'
    assert doc_2_virat.get_field('directions') == 'Use two tablets daily for three months'

def test_get_refill_times(doc_1_maria, doc_2_virat):
    assert doc_1_maria.get_field('refill_times') == '2'
    assert doc_2_virat.get_field('refill_times') == '3'

def test_parse(doc_1_maria, doc_2_virat):
    record_maria = doc_1_maria.parse()
    assert record_maria == {
        'patient_name': 'Marta Sharapova',
        'patient_address': '9 tennis court, new Russia, DC',
        'medicines': 'Prednisone 20 mg, Lialda 2.4 gram',
        'directions': 'Prednisone, Take 5 mg every 3 days, Finish in 2.5 weeks and Lialda, take 2 pill everyday for 1 month',
        'refill_times': '2'
    }
    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refill_times': '3'
    }
