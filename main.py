import json
import os.path

from flask import Flask, request, jsonify
from flask_cors import CORS

from logger import logger

app = Flask(__name__)
CORS(app)

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


@app.route('/get_average_energy_generated', methods=['GET'])
def get_average_energy_generated():
    logger.info('Received GET request for average energy generated data.')

    json_data = read_from_json_file()
    energy_data = json_data.get('energy_generated', [])

    if not energy_data:
        logger.warning('No energy generated data available.')
        return jsonify({'message': 'No data available to calculate averages.'}), 404

    total_entries = len(energy_data)
    total_forca = 0.0
    total_pressao = 0.0
    total_tensao = 0.0
    total_energia = 0.0

    for index, entry in enumerate(energy_data):
        try:
            total_forca += float(entry.get('forca', 0))
            total_pressao += float(entry.get('pressao', 0))
            total_tensao += float(entry.get('tensao', 0))
            total_energia += float(entry.get('energia', 0))

        except (TypeError, ValueError) as e:
            logger.error(f'Data format error at index {index}: {e}')
            return jsonify({'message': f'Invalid data format in entry {index}.'}), 400

    if total_entries == 0:
        logger.warning('Total entries count is zero after processing data.')
        return jsonify({'message': 'No valid data to calculate averages.'}), 404

    averages = {
        'forca_average': total_forca / total_entries,
        'pressao_average': total_pressao / total_entries,
        'tensao_average': total_tensao / total_entries,
        'energia_average': total_energia / total_entries
    }

    logger.info('Successfully calculated averages. Returning averages.')
    return jsonify(averages), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
