from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Endpoint لعرض الفتاوى على شكل JSON
@app.route('/fatwas')
def get_fatwas():
    try:
        with open('fatwas_output.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)  # إرجاع البيانات على شكل JSON
    except FileNotFoundError as e:
        return jsonify({"error": "File not found."}), 500
    except json.JSONDecodeError as e:
        return jsonify({"error": "Error decoding JSON."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# الصفحة الرئيسية لعرض بيانات الفتاوى
@app.route('/')
def index():
    try:
        with open('fatwas_output.json', 'r') as file:
            data = json.load(file)
        return render_template('index.html', data=data)  # عرض البيانات في صفحة HTML
    except FileNotFoundError as e:
        return "File not found.", 500
    except json.JSONDecodeError as e:
        return "Error decoding JSON.", 500
    except Exception as e:
        return "An unexpected error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True)
