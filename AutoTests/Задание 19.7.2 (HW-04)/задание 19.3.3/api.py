import json
import requests


status = 'available'
BASEURL = 'petfriends.skillfactory.ru/'
# headers = {'accept': 'application/json'}

headers = {
            'email': 'test872@gmail.com',
            'password': 'Bobik1107!'
}

res_key = requests.get(f'https://{BASEURL}api/key', headers=headers)

print('get')
print(res_key.status_code)
print(res_key.text)
print(res_key.json())
print(type(res_key.json()))

print('------------------------------------------')

auth_key = res_key.json()

body = {
    'name': 'Ракета',
    'animal_type': 'Енот',
    'age': '22'
}

res_CreatPet = requests.post(f'https://{BASEURL}/api/create_pet_simple', headers={'auth_key': auth_key['key']}, data=body)

print('post')
print(res_CreatPet.status_code)
print(res_CreatPet.text)
print(res_CreatPet.json())
print(type(res_CreatPet.json()))

print('------------------------------------------')
#
res_ListOfMyPets = requests.get(f'https://{BASEURL}api/pets', headers={'auth_key': auth_key['key']}, params={'filter': 'my_pets'})

print('get')
print(res_ListOfMyPets.status_code)
print(res_ListOfMyPets.text)
print(res_ListOfMyPets.json())
print(type(res_ListOfMyPets.json()))

print('------------------------------------------')

pet = res_ListOfMyPets.json()
pet_id = pet['pets'][0]['id']
print(pet_id)


new_body = {
    'name': 'Чубакка',
    'animal_type': 'Собака',
    'age': '11'
}

res_UpdatePet = requests.put(f'https://{BASEURL}/api/pets/{pet_id}', headers={'auth_key': auth_key['key']}, data=new_body)

print('post')
print(res_UpdatePet.status_code)
print(res_UpdatePet.text)
print(res_UpdatePet.json())
print(type(res_UpdatePet.json()))

print('------------------------------------------')


pet_photo = open('image/Chewbacca.jpg', 'rb')
data = {'pet_photo': pet_photo}


res_SetPetPhoto = requests.post(f'https://{BASEURL}/api/pets/set_photo/{pet_id}', headers={'auth_key': auth_key['key']}, files=data)

print('postPhoto')
print(res_SetPetPhoto.status_code)
print(res_SetPetPhoto.text)
print(res_SetPetPhoto.json())
print(type(res_SetPetPhoto.json()))

print('------------------------------------------')

res_DeletePet = requests.delete(f'https://{BASEURL}api/pets/{pet_id}', headers={'auth_key': auth_key['key']})

print('delete')
print(res_DeletePet.status_code)

print('------------------------------------------')
