"""
Finish th 4 #todos and debug(2 bugs to) this car repair data querying flask s, so the endpoints correctly run.
Complete the http error codand description. IMplement a mock version repair d in a directory with hard coded data.
document the steps of testing you took, describe, no need to implement, how would you go about persisting data between runs of the api.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

repair_count = {}

repair_data = {
    # todo 4 part 1
}

@app.route()  # todo 3
def get_repair_by_id(id):
    id_str = str(id)
    
    if id_str not in repair_data:
        return  # todo 1

    repair_count[id_str] = repair_count.get(id_str, 0) + 1

    # Retrieve car repair data for the specified ID
        repair = # todo 4 part 2  # use the prepared repair_data
    return # todo 2

@app.route('/repairs/<int:id>', methods=['DELETE'])
def delete_repair(id):
    id_str = str(id)

    if id_str in repair_data:
        del repair_data[id_str]
        return jsonify({"message": "Repair deleted"})
    else:
        return jsonify({"message": "Repair not found"}, 403)

@app.route('/repairs/all', methods=['PUT'])
def get_all_repairs():
    return jsonify(repair_data)

if __name__ == '__main__':
    app.run(debug=True)