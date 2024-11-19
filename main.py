import json
import os.path

from flask import Flask, request, jsonify
from logger import logger
app = Flask(__name__)

JSON_DATA_FILE_NAME = 'energy_data.json'

def read_from_json_file() -> dict:
    logger.info('Reading existing data...')

    if os.path.exists(JSON_DATA_FILE_NAME):
        with open(JSON_DATA_FILE_NAME, 'r') as f:
            existing_data = json.load(f)
            logger.info('Successfully read existing data.')
            return existing_data

    logger.info('No data to read, returning empty dict...')
    return {}


def write_to_json_file(new_data: dict) -> None:
    existing_data = read_from_json_file()

    logger.info('Writing new data...')

    with open(JSON_DATA_FILE_NAME, 'w') as f:
        if existing_data:
            existing_data['energy_generated'].append(new_data)
        else:
            existing_data['energy_generated'] = [new_data]

        json.dump(existing_data, f, indent=4)
        logger.info('Successfully written new data.')


@app.route('/post_energy_info', methods=['POST'])
def receive_energy_info():
    try:
        request_data = request.get_json()

        logger.info(f'Received data from post request.')
        logger.debug(f'Data received from post request: {request_data}')

        write_to_json_file(request_data)

        return jsonify({'status': 'success', 'data': request_data}), 200

    except Exception as e:
        logger.exception(f'Error trying to process post request: {e}')
        return jsonify({'status': 'error', 'message': e}), 500


if __name__ == '__main__':
    app.run()
