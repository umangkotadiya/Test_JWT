import requests

# Base URL of your API
BASE_URL = 'http://127.0.0.1:8000/'

# Obtain JWT token
def get_token():
    url = f'{BASE_URL}accounts/login/'
    data = {
        'username': 'harsh',
        'password': 'harsh123'
    }
    response = requests.post(url, data=data)
    print("response---------------->", response.json()["access"])
    return response.json()['access']

# Test CRUD operations for Hospital
def test_hospital_crud():
    token = get_token()
    print("token", token)
    headers = {'Authorization': f'Bearer {token}'}

    # Create a hospital
    create_url = f'{BASE_URL}hospitals/'
    hospital_data = {
        'name': 'Test Hospital',
        'address': '123 Test St',
        'phone': '1234567890',
        'email': 'test@hospital.com',
        'website': 'http://www.testhospital.com'
    }
    create_response = requests.post(create_url, json=hospital_data, headers=headers)
    print('Create Hospital:', create_response.json())

    # Read hospitals
    read_url = f'{BASE_URL}hospitals/'
    read_response = requests.get(read_url, headers=headers)
    print('Read Hospitals:', read_response.json())

    # Update a hospital
    hospital_id = create_response.json()['id']
    update_url = f'{BASE_URL}hospitals/{hospital_id}/'
    update_data = {
        'name': 'Updated Test Hospital',
        'address': '123 Updated St',
    }
    update_response = requests.put(update_url, json=update_data, headers=headers)
    print('Update Hospital:', update_response.json())

    # Delete a hospital
    delete_response = requests.delete(update_url, headers=headers)
    print('Delete Hospital:', delete_response.status_code)

if __name__ == '__main__':
    test_hospital_crud()
