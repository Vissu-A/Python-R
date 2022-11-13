import jwt

encoded_token = jwt.encode({'username':'vissu'}, 'SECRET', algorithm='HS256')

print(encoded_token)

decoded_token = jwt.decode(encoded_token, 'SECRET', algorithms=['HS256'])

print(decoded_token)