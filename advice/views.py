import openai
from django.shortcuts import render
import googlemaps
from django.conf import settings

gmaps = googlemaps.Client(key=settings.GOOGLEMAPS_API_KEY)
openai.api_key = settings.OPENAI_API_KEY


def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2500,
        n=1,
        stop=None,
        temperature=0.5,
        stream=False
    )
    return response["choices"][0].message.content


def home(request):
    if request.method == 'POST':
        lat = request.POST['latitude']
        lng = request.POST['longitude']

        if lat and lng:
            reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
            city = None
            country = None

            for result in reverse_geocode_result:
                if 'locality' in result['types']:
                    city = result['address_components'][0]['long_name']
                elif 'country' in result['types']:
                    country = result['address_components'][0]['long_name']

            if city and country:
                places_results = gmaps.places(query='tourist attractions in ' + city + ', ' + country,
                                              type='tourist_attraction')

                place_names = [place['name'] for place in places_results['results']]
                places_str = ", ".join(place_names)

                locations = []
                if places_str:
                    for place in places_results['results']:
                        location = {
                            'name': place['name'],
                            'lat': place['geometry']['location']['lat'],
                            'lng': place['geometry']['location']['lng']
                        }
                        locations.append(location)

                        content = f"Call me Travel Monster. Help me as a tourist guide for only the top 5 important places in {city} city: {places_str}. Describe them wildly and excitingly. Be funny. Explain in 50 words. Write in English. Use emojis at the end of sentences. Use paragraphs."

                else:
                        content = f"Call me Travel Monster. Tell me there are no any place to visit in {city} city. Ask if I can find another spot on Earth. Be funny. Explain very briefly. Write in English."
                print(city)
                print(places_str)

                text = generate_text(content)

                data = {
                    'content': text,
                    'lat': lat,
                    'lng': lng,
                    'locations': locations
                }

                return render(request, 'advice.html', data)

            else:

                content = f"Call me Travel Monster. Say there aren't many places to visit here. Ask if I can't find another spot on Earth. Be funny. Explain briefly. Write in English."
                text = generate_text(content)

                data = {
                    'content': text,
                    'lat': lat,
                    'lng': lng
                }

                return render(request, 'advice.html', data)

        else:
            data = {
                'content': "First, mark a place on the map that you're curious about!"
            }
            return render(request, "home.html", data)

    else:
        return render(request, "home.html")