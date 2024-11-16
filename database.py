import sqlite3

# 데이터베이스 초기화
def create_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # 환자 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            disease TEXT NOT NULL,
            medication TEXT NOT NULL,
            last_disease TEXT NOT NULL
        )
    ''')

    # 약물 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drugs (
            drug_id TEXT PRIMARY KEY,
            drug_name TEXT NOT NULL,
            drug_function TEXT NOT NULL,
            drug_capacity TEXT NOT NULL,
            drug_badfood TEXT NOT NULL,
            drug_goodfood TEXT NOT NULL,
            drug_exercise TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# 환자 정보 삽입
def insert_patient(patient_id, name, disease, medication, last_disease):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO patients (patient_id, name, disease, medication, last_disease)
        VALUES (?, ?, ?, ?, ?)
    ''', (patient_id, name, disease, medication, last_disease))
    
    conn.commit()
    conn.close()

# 환자 정보 조회
def get_patient_info(patient_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    patient = cursor.fetchone()
    conn.close()
    
    return patient

# 약물 정보 삽입
def insert_drug(drug_id, drug_name, drug_function, drug_capacity, drug_badfood, drug_goodfood, drug_exercise):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO drugs (drug_id, drug_name, drug_function, drug_capacity, drug_badfood, drug_goodfood, drug_exercise)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (drug_id, drug_name, drug_function, drug_capacity, drug_badfood, drug_goodfood, drug_exercise))
    
    conn.commit()
    conn.close()

# 약물 정보 조회
def get_drug_info(drug_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM drugs WHERE drug_id = ?', (drug_id,))
    drug = cursor.fetchone()
    conn.close()
    
    return drug

# 처음 실행 시 데이터베이스 생성
if __name__ == "__main__":
    create_db()
