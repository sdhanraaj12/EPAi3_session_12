from decimal import Decimal
from session_9 import *

fake = Faker()

Profile = namedtuple('Profile', fake.profile().keys())
named_tuples = [
    Profile('AA', 'GH', '200-000-222', 'Texas', (Decimal('-46.204908'), Decimal('-168.530504')), 'O+', 'www.ddd.com',
            'GP', 'KS', 'M', 'qqq', 's@dys.com', date(1968, 1, 25)),
    Profile('LC', 'GCB', '000-000-000', 'Austin', (Decimal('75.9842075'), Decimal('-17.257017')), 'B+', 'www.www.www',
            'WD', 'JB', 'F', 'AAA', 'sdg', date(1931, 10, 25)),
    Profile('GG', 'DFG', '000-111-000', 'AX', (Decimal('-43.994425'), Decimal('107.105065')), 'O-', 'sss', 'IS', 'AC',
            'F', 'SSS', 'GHF', date(1993, 3, 20)),
    Profile('LS', 'DD', '000-222-333', 'DS', (Decimal('-6.979771'), Decimal('-51.459563')), 'O+', 'www', 'DG', 'CD',
            'F', 'SDF', 'DFT', date(1981, 3, 28)),
    Profile('CE', 'BL', '000-333-444', 'SW', (Decimal('-7.1557865'), Decimal('142.414900')), 'A+', 'ert', 'MR', 'BS',
            'M', 'SWQ', 'dfr', date(1934, 11, 12))
]


# Test cases for question 1


def test_q1_1_number_of_profiles():
    assert len(init_profiles_using_namedtuple(100)) == 100, "Test 100 profiles"


def test_q1_2_average_age():
    assert average_age_nt(named_tuples)[1] == 59.2, "Test the average age "


def test_q1_3_oldest_person():
    assert oldest_person_nt(named_tuples)[1] == 89, "Test the oldest age "


def test_q1_4_average_coordinates():
    assert average_coordinates_nt(named_tuples)[1] == (
        Decimal('-5.6701366'), Decimal('2.4545762')), "Test the average coordinate "


def test_q1_5_max_blood_group():
    assert max_blood_group_nt(named_tuples)[1] == 'O+', "Test the maximum blood type "


# Test cases for question 2

fk_profile_dict = named_tuple_dict(named_tuples)


def test_q2_1_average_age():
    assert average_age_dc(fk_profile_dict)[1] == 59.2, "PLease check the average age in dictionary"


def test_q2_2_oldest_person():
    assert oldest_person_dc(fk_profile_dict)[1] == 89, "PLease check the average age in dictionary"


def test_q2_3_average_coordinates():
    assert average_coordinates_dc(fk_profile_dict)[1] == (
        Decimal('-5.6701366'), Decimal('2.4545762')), "PLease check the avg coordinate in dictionary"


def test_q2_4_max_blood_group():
    assert max_blood_group_dc(fk_profile_dict)[1] == 'O+', "Please check the max blood in dictionary"


def test_q2_5_fastest():
    fk_profile_nt = init_profiles_using_namedtuple(10000)
    fk_profile_dict = named_tuple_dict(fk_profile_nt)
    assert time_nt(fk_profile_nt, 100) < time_dc(fk_profile_dict,
                                                 100), "Dict cannot be faster than named tuple!!! "


# Test cases for question 2
N = 100
st_val = stock_market(N)


def test_q3_1_num_profiles_generated():
    assert len(stock_market(100)[0]) == 100, 'Not enough profiles'


def test_q3_2_doc_string():
    assert stock_market.__doc__ is not None, 'Please provide a doc string'


def test_q3_3_annotations():
    assert stock_market.__annotations__ is not None, 'Please provide appropriate annotations'


def test_q3_4_unique_symbol():
    symbols = len(set([x.symbol for x in st_val[0]]))
    assert symbols == N, 'Duplicate Symbols found'


def test_q3_5_return_named():
    assert type(st_val[0][0]) != tuple, 'Check the function'


def test_q3_6_normalized_weigh():
    wts_sum = sum([x.company_weight for x in st_val[0]])
    assert wts_sum >= 0.9, 'Normalize the weights'


def test_q3_7_high_low():
    assert st_val[2] >= st_val[3], 'How can highest be less than lowest'


def test_q3_8_all_high_low():
    high = [x.high for x in st_val[0]]
    open_ = [x.open for x in st_val[0]]
    diff = [(high[i] - open_[i]) for i in range(len(high))]
    for x in diff:
        assert x >= 0, 'Check the Program'


def test_q3_9_docstring_namedtuple():
    assert st_val[0][1].__doc__ is not None, 'No docstring for the tuple'


def test_q3_10_docstring():
    assert symbol.__doc__ is not None, 'Doc string missing'
