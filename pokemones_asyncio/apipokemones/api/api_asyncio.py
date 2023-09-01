async def get_imagen_pokemon(session, url):
    async with session.get(url) as resp:
        response_json = await resp.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data
