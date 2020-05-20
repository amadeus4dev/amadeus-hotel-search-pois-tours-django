In this prototype we demonstrate the safety information and POIs for a chosen hotel on the map, using:
- [Hotel Search API](https://developers.amadeus.com/self-service/category/hotel/api-doc/hotel-search): shows hotels on the map
- Geosure API: shows safety information for the area each hotel is located
- [Points of Interests API](https://developers.amadeus.com/self-service/category/destination-content/api-doc/points-of-interest): shows POIs near the hotel
- [HERE Maps API](https://developer.here.com/): displays a map with markers and text bubbles

## How to run the project via Docker (recommended)

Build the image from the Dockerfile. The following command will 

```sh
make
```

The container receives your API key/secret from the environment variables.
Before running the container, make sure your have your credentials correctly
set:

```sh
export AMADEUS_CLIENT_ID=YOUR_AMADEUS_API_KEY
export AMADEUS_CLIENT_SECRET=YOUR_AMADEUS_API_SECRET
export GEOSURE_ENDPOINT=YOUR_GEOSURE_ENDPOINT
export GEOSURE_ACCESS_TOKEN=YOUR_GEOSURE_ACCESS_TOKEN
export HERE_API_KEY=YOUR_HERE_API_KEY
```

Finally, start the container from the image:

```
make run
```

At this point you can open a browser and go to `https://0.0.0.0:8000`.

Note that it is also possible to run in detached mode so your terminal is still
usable:

```
make start
```

Stop the container with:

```
make stop
```

## How to run the project locally

Clone the repository.

```sh
git clone https://github.com/amadeus4dev/amadeus-hotel-area-safety-pois-django.git
cd amadeus-hotel-area-safety-pois-django
```

Next create a virtual environment and install the dependencies.

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For authentication add your API key/secret to your `.bashrc` or `.zshrc` files.

```sh
export AMADEUS_CLIENT_ID=YOUR_API_KEY
export AMADEUS_CLIENT_SECRET=YOUR_API_SECRET
export GEOSURE_ENDPOINT=YOUR_GEOSURE_ENDPOINT
export GEOSURE_ACCESS_TOKEN=YOUR_GEOSURE_ACCESS_TOKEN
export HERE_API_KEY=YOUR_HERE_API_KEY
```

You can easily switch between `test` and `production` environments by setting:

```
export AMADEUS_HOSTNAME="test" # an empty value will also set the environment to test
```

or

```
export AMADEUS_HOSTNAME="production"
```

> Each environment has different API keys. Do not forget to update them!

Finally, run the Django server.

```sh
python amadeus_demo//manage.py runserver
```

Finally, open a browser and go to `https://127.0.0.1:8000`

## License

This library is released under the [MIT License](LICENSE).

## Help

Our [developer support team](https://developers.amadeus.com/support) is here
to help you. You can find us on
[StackOverflow](https://stackoverflow.com/questions/tagged/amadeus) and
[email](mailto:developers@amadeus.com).
