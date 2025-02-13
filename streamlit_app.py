import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Set judul halaman
st.set_page_config(page_title="Homepage Sederhana", page_icon="🏠", layout="wide")

# Judul utama
st.title("Loan Approval Prediction")

# Teks penjelasan
st.write("Ini adalah halaman depan aplikasi Streamlit sederhana.")

# Menampilkan gambar (opsional)
st.image("https://th.bing.com/th/id/OIP.QHvgD4mqNj7fNdLea9eckgAAAA?rs=1&pid=ImgDetMain")

# Input form untuk nama pengguna
name = st.text_input("Masukkan Nama Anda")
if name:
    st.write(f"Selamat datang, {name}!")

# Menambahkan tombol
if st.button("OK"):
    st.write("Tombol telah diklik!")

 # Input Pengguna
st.sidebar.header("Masukkan Data Anda")
age = st.sidebar.slider("Usia", 18, 100, 25)
income = st.sidebar.slider("Pendapatan Bulanan", 1000, 20000, 5000)
loan_amount = st.sidebar.slider("Jumlah Pinjaman", 1000, 50000, 10000)
credit_score = st.sidebar.slider("Skor Kredit", 300, 850, 650)
employment_status = st.sidebar.selectbox("Status Pekerjaan", ["Bekerja", "Tidak Bekerja"])
##########################################################################################

# Input untuk jumlah pinjaman
loan_amount = st.number_input("Jumlah Pinjaman (Rp)", min_value=100000, step=100000)

# Input untuk suku bunga
interest_rate = st.number_input("Suku Bunga Tahunan (%)", min_value=0.0, step=0.1)

# Input untuk lama pinjaman
loan_term = st.number_input("Jangka Waktu Pinjaman (Tahun)", min_value=1, step=1)

# Fungsi untuk menghitung cicilan bulanan
def calculate_monthly_payment(P, r, n):
    """
    P: Jumlah Pinjaman
    r: Suku bunga per bulan
    n: Jumlah total cicilan (bulan)
    """
    r = r / 100 / 12  # Mengubah suku bunga tahunan ke bulanan
    n = n * 12  # Mengubah jangka waktu dalam tahun ke bulan
    
    if r == 0:
        return P / n  # Jika bunga 0%, cicilan per bulan adalah jumlah pinjaman dibagi jangka waktu
    else:
        return P * r * (1 + r) ** n / ((1 + r) ** n - 1)

# Menghitung cicilan jika tombol dihitung ditekan
if st.button("Hitung Cicilan"):
    if loan_amount > 0 and interest_rate >= 0 and loan_term > 0:
        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)
        st.write(f"Cicilan Bulanan: Rp {monthly_payment:,.2f}")
    else:
        st.write("Mohon masukkan nilai yang valid untuk semua input.")
####################################################################################################################


    
# Footer
st.markdown("---")
st.write("Made with izlal")
