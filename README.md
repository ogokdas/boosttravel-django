Boost Travel - Django Tourist Guide:

![Selection for Istanbul](https://github.com/ogokdas/boosttravel-django/blob/main/png/select_istanbul.PNG)
![Advices for Istanbul](https://github.com/ogokdas/boosttravel-django/blob/main/png/advice_istanbul.PNG)
![Selection for Jersey](https://github.com/ogokdas/boosttravel-django/blob/main/png/select_jersey.PNG)
![Advices for Jersey](https://github.com/ogokdas/boosttravel-django/blob/main/png/advice_jersey.PNG)
![Selection for no where](https://github.com/ogokdas/boosttravel-django/blob/main/png/select_nowhere.PNG)
![Advices for no where](https://github.com/ogokdas/boosttravel-django/blob/main/png/advice_neverland.PNG)

Description:

I have developed the Boosttravel - Django Tourist Guide application to provide online tourist guide services to users. The application empowers users to explore tourist attractions in a city by connecting them to a selected location on a world map. Users can mark points of interest on the map, click the "Get Recommendations" button, and access highlighted tourist spots in the associated city. Moreover, the application generates a concise summary of the tourist guide, presenting information about activities and attractions in the marked locations. To build this application, I utilized HTML, CSS, and JavaScript for the frontend, while the backend leverages the Django framework and Python programming language. The map functionality relies on the Google Maps API, tourist spot retrieval is facilitated by the Google Places API, and the OpenAI ChatGPT API is employed to generate the tourist guide text. By sending the coordinates obtained from Google Maps as a prompt to the ChatGPT API, the guide text is dynamically created. I have created this platform with the intention of sharing it with others on GitHub.

Installation:

To install and run the application locally, follow these steps:
1.	Clone the repository:
git clone https://github.com/ogokdas/boosttravel-django.git
2.	Navigate to the project directory:
cd project_directory
3.	Install the required packages by running the following command:
pip install -r requirements.txt
4.	Obtain the necessary API keys:
1.	Google Maps API: Visit the Google Cloud Console (https://console.cloud.google.com/) to create a project and generate an API key. Enable the Maps JavaScript API, Places API, and Geocoding API for your project.
2.	OpenAI ChatGPT API: Obtain an API key from OpenAI (https://platform.openai.com/account/api-keys/) to use the ChatGPT API.
5.	Update API keys in the application:
Open the settings.py file located at boosttravel/settings.py. In this file, replace the placeholders GOOGLEMAPS_API_KEY and OPENAI_API_KEY with your own API keys. Additionally, in the HTML files within the Templates folder (advice/templates), make sure to replace the placeholder GOOGLEMAPS_API_KEY with your own API key.
6.	Run the development server:
python manage.py runserver
7.	Access the application in your web browser: http://localhost:8000/

Contribution:

If you wish to contribute to the development of this application, you can help by enabling the dynamic display of the tourist guide text on the web. Here's how you can contribute:
1.	Explore the Django templates and views to identify the appropriate locations for integrating the dynamic display of the tourist guide text.
2.	Implement the necessary changes to fetch and display the tourist guide text dynamically using JavaScript or Django's templating engine with StreamingHTTPResponse.
3.	Thoroughly test the changes to ensure proper functionality.
4.	Submit a pull request with your modifications, providing a clear description of the changes made.
Contact
For any inquiries or feedback, please contact me at
OGOKDAS1@gmail.com 
and 
+90 542 218 55 44




