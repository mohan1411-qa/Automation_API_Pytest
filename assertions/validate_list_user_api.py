def assert_list_user(respData):
    """Assertion methods
    Can be reused if same assertion to be used in other test cases
    """
    for data in respData:
        assert data['id'] is not None
        assert data['email'] is not None
        assert data['first_name'] is not None
        assert data['last_name'] is not None


def assert_specific_user_in_list_user(respData, user_id, email, first_name, last_name):
    flag = False
    for data in respData:
        print(data)
        if data['id'] == user_id and data['email'] == email and data[
            'first_name'] == first_name and \
                data['last_name'] == last_name:
            print(data)
            flag = True
        else:
            pass
    assert flag == True
