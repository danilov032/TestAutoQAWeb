# assert abs(-42) == 42, "Всем пизда, нам пизда!!!"
#
# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
#
# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")


def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


# test_input_text(8, 11)
# test_input_text(11, 11)
# test_input_text(11, 15)

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


def test_substring(full_string, substring):
# ваша реализация, напишите assert и сообщение об ошибке
    assert str(substring) in str(full_string), f"expected {substring} to be substring of {full_string}"

# test_substring("fulltext", "substring")
test_substring(1, 1)
test_substring("some_text", "some")



