import streamlit as st

# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Ứng dụng tính Thuế TNCN",
    page_icon="💰",
    layout="wide"
)


# =========================================================
# 2. CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title-box {
    background: linear-gradient(135deg, #0d47a1, #1976d2);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.title-box h1 {
    margin: 0;
    font-size: 32px;
}

.title-box p {
    margin-top: 10px;
    font-size: 16px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result-box {
    background: linear-gradient(135deg, #00a86b, #00c853);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin: 20px 0;
}

.result-box h2 {
    margin: 0;
    font-size: 18px;
}

.result-box h1 {
    margin: 10px 0;
    font-size: 36px;
}

.section-title {
    color: #0d47a1;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. TIÊU ĐỀ
# =========================================================

st.markdown("""
<div class="title-box">

    <h1>💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN</h1>

    <p>
        Công cụ hỗ trợ tính toán Lương Gross - Thuế TNCN - Lương Net
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 4. NHẬP THÔNG TIN
# =========================================================

st.markdown(
    '<div class="section-title">📝
