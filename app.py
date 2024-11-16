from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# 비밀번호 설정 (예시)
CORRECT_PASSWORD = "0302"

# 홈 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 비밀번호 입력 페이지 (환자 정보)
@app.route('/password_patient')
def password_patient_page():
    return render_template('password_form.html', page_type="patient")  # 환자 정보 비밀번호 입력 폼 렌더링

# 비밀번호 입력 페이지 (약물 정보)
@app.route('/password_drug')
def password_drug_page():
    return render_template('password_form.html', page_type="drug")  # 약물 정보 비밀번호 입력 폼 렌더링

@app.route('/check_password_patient', methods=['POST'])
def check_password_patient():
    entered_password = request.form['password']
    if entered_password == CORRECT_PASSWORD:
        return redirect(url_for('add_patient'))  # 비밀번호 맞으면 환자 정보 입력 폼으로 리다이렉트
    else:
        return "비밀번호가 틀렸습니다.", 403  # 비밀번호 틀리면 403 오류

@app.route('/check_password_drug', methods=['POST'])
def check_password_drug():
    entered_password = request.form['password']
    if entered_password == CORRECT_PASSWORD:
        return redirect(url_for('add_drug'))  # 비밀번호 맞으면 약물 정보 입력 폼으로 리다이렉트
    else:
        return "비밀번호가 틀렸습니다.", 403  # 비밀번호 틀리면 403 오류

# 환자 정보 입력 페이지
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        name = request.form['name']
        disease = request.form['disease']
        medication = request.form['medication']
        last_disease = request.form['last_disease']

        # 환자 정보 데이터베이스에 저장
        database.insert_patient(patient_id, name, disease, medication, last_disease)
        return redirect(url_for('index'))
    
    return render_template('add_patient.html')

# 환자 정보 조회
@app.route('/patient_info', methods=['GET'])
def patient_info():
    patient_id = request.args.get('patient_id')
    if not patient_id:
        return "환자 ID를 입력하세요.", 400

    patient = database.get_patient_info(patient_id)
    if patient:
        return render_template('patient_info.html', patient=patient)
    else:
        return f"환자 {patient_id}를 찾을 수 없습니다.", 404

# 약물 정보 입력 페이지
@app.route('/add_drug', methods=['GET', 'POST'])
def add_drug():
    if request.method == 'POST':
        drug_id = request.form['drug_id']
        drug_name = request.form['drug_name']
        drug_function = request.form['drug_function']
        drug_capacity = request.form['drug_capacity']
        drug_badfood = request.form['drug_badfood']
        drug_goodfood = request.form['drug_goodfood']
        drug_exercise = request.form['drug_exercise']

        # 약물 정보 데이터베이스에 저장
        database.insert_drug(drug_id, drug_name, drug_function, drug_capacity, drug_badfood, drug_goodfood, drug_exercise)
        return redirect(url_for('index'))
    
    return render_template('add_drug.html')

# 약물 정보 조회
@app.route('/drug_info', methods=['GET'])
def drug_info():
    drug_id = request.args.get('drug_id')
    if not drug_id:
        return "약물 ID를 입력하세요.", 400

    drug = database.get_drug_info(drug_id)
    if drug:
        return render_template('drug_info.html', drug=drug)
    else:
        return f"약물 {drug_id}를 찾을 수 없습니다.", 404

if __name__ == '__main__':
    app.run(debug=True)
