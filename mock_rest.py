# encoding: utf-8
import json
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
txt_file = './data.txt'

with open(txt_file, 'w') as f:
    f.write(json.dumps([{'name': 'alice', 'email': 'alice@outlook.com', 'zipcode': '1111-1111'}], indent=2))


@app.route('/', methods=['GET'])
def query_records():
    time.sleep(1)
    with open(txt_file, 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)


# PUT is update All data
@app.route('/', methods=['PUT'])
def create_record():
    new_records = json.loads(request.data)
    with open(txt_file, 'r') as f:
        data = f.read()

    records = json.loads(data)
    is_exist = False
    for r in records:
        if r['name'] == new_records['name']:
            r['email'] = new_records['email']
            is_exist = True
    if is_exist:
        with open(txt_file, 'w') as f:
            f.write(json.dumps(records, indent=2))
        return jsonify(records)
    else:
        return jsonify({'error': 'put data not found'})


# PUT is update one atomic data
@app.route('/', methods=['PATCH'])
def patch_record():
    new_records = json.loads(request.data)
    with open(txt_file, 'r') as f:
        data = f.read()

    records = json.loads(data)
    is_exist = False
    for r in records:
        if r['name'] == new_records['name']:
            if 'email' in new_records.keys():
                r['email'] = new_records['email']
            if 'zipcode' in new_records.keys():
                r['zipcode'] = new_records['zipcode']
            is_exist = True

    if is_exist:
        with open(txt_file, 'w') as f:
            f.write(json.dumps(records, indent=2))
        return jsonify(records)
    else:
        return jsonify({'error': 'put data not found'})


@app.route('/', methods=['POST'])
def update_record():
    new_records = json.loads(request.data)
    with open(txt_file, 'r') as f:
        data = f.read()
        records = json.loads(data)
    is_exist = False
    for r in records:
        if r['name'] == new_records['name'] and r['email'] == new_records['email']:
            is_exist = True

    if is_exist is False:
        records.append(new_records)

    with open(txt_file, 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(records)


@app.route('/<name>', methods=['DELETE'])
def del_record(name):
    with open(txt_file, 'r') as f:
        data = f.read()

    records = json.loads(data)
    deleted_records = []
    for r in records:
        if r['name'] != str(name):
            deleted_records.append(r)

    if deleted_records != records:
        with open(txt_file, 'w') as f:
            f.write(json.dumps(deleted_records, indent=2))
        return jsonify(deleted_records)
    else:
        return jsonify({'error': 'delete data not found'})


app.run(debug=True)
