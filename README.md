# CustomGPT: NASA Space Data Assistant

## Overview

The NASA Space Data Assistant is a CustomGPT-powered plugin designed to interact with various NASA APIs. It offers data and insights from space-related datasets, including International Space Station (ISS) tracking, near-earth objects (NEOs), space weather, and more. The project is a combination of Python-based backend services, API integration, and legal provisions for usage.

## Features

- **ISS Location Retrieval**: Provides the real-time location of the International Space Station.
- **Near-Earth Objects (NEO) Data**: Retrieves data related to near-earth objects, with options to filter by date.
- **Astronomy Picture of the Day (APOD)**: Access the NASA APOD service for images and descriptions.
- **Earth Observation Data**: Obtain Earth observation data based on provided coordinates or place names.
- **Space Weather Data**: Fetch data on solar flares, geomagnetic storms, and interplanetary shocks.
## Project Structure

- space.yaml: Defines API paths and their corresponding endpoints, providing documentation and schema for various NASA data services.
- space.py: Backend Python script implementing API interactions and response handling for the defined endpoints (file content details not included in this summary).
- legal.html: Contains the legal terms and conditions for usage of the NASA Space Data Assistant, including user conduct, license terms, and limitations of liability.

## API Endpoints
The available API endpoints are as follows:

- */api/iss_location*
    - Method: GET
    - Description: Retrieve the current location of the ISS.
- */api/neo*
  - Method: GET
  - Description: Retrieve data on near-earth objects. Accepts optional start_date and end_date query parameters.
- */api/apod*
  - Method: GET
  - Description: Retrieve the Astronomy Picture of the Day (APOD) between specified dates.
  
- */api/earth*
  - Method: GET
  - Description: Fetch Earth observation data using place name or coordinates.
    
- */api/space_weather*
  - Method: GET
  - Description: Retrieve data on solar flares and space weather.
- */api/geomagnetic_storms*
  - Method: GET
  - Description: Fetch geomagnetic storm data.
- */api/interplanetary*
  - Method: GET
  - Description: Obtain data on interplanetary shocks.
## API Key Modifications
- The original NASA API key has been replaced with a demo key to maintain security. This change ensures that sensitive credentials are not exposed while maintaining functionality for demonstration purposes.
- Additionally, a service authentication key has been added, which acts as a bearer token for OpenAI API calls, providing a secure means of authorization for API requests.
## Legal Information
Please refer to the Legal Information for details on terms of use, license agreements, intellectual property, user conduct, and privacy policies.


## Contact

For any questions or concerns, you can reach out to the developer team at bandarudevisri.ds@gmail.com.

