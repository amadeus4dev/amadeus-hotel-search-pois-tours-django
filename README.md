This project demonstrates how to integrate Amadeus APIs using the [Python SDK](https://github.com/amadeus4dev/amadeus-python) in a Django application.

In this scenario, the end user submits round-trip information via a form and the [Trip Purpose Prediction API](https://developers.amadeus.com/self-service/category/trip/api-doc/trip-purpose-prediction) is called. This API predicts if a the given journey is for leisure or business purposes.

## How to run the project locally

Clone the repository.

```sh
git clone https://github.com/amadeus4dev/amadeus-trip-purpose-django.git
cd amadeus-trip-purpose-django
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
python prediction/manage.py runserver
```

Finally, open a browser and go to `https://127.0.0.1:8000`

## License

This library is released under the [MIT License](LICENSE).

## Help

Our [developer support team](https://developers.amadeus.com/support) is here
to help you. You can find us on
[StackOverflow](https://stackoverflow.com/questions/tagged/amadeus) and
[email](mailto:developers@amadeus.com).
