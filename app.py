import streamlit as st

# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Ứng dụng tính Thuế TNCN",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# 2. CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

/* Tiêu đề chính */
.header-box {
    background: linear-gradient(135deg, #0f4c81, #1976b9);
    padding: 30px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}

.header-box h1 {
    margin: 0;
    font-size: 32px;
}

.header-box p {
    margin-top: 8px;
    font-size: 16px;
}

/* Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    border: 1px solid #e5e7eb;
}

/* Tiêu đề section */
.section-title {
    color: #0f4c81;
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Card kết quả */
.result-card {
    background-color: white;
    padding: 20px;
    border-radius: 16px;
    border-left: 5px solid #1976b9;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    min-height: 110px;
}

.result-title {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
}

.result-value {
    color: #0f172a;
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
}

/* Lương Net */
.net-box {
    background: linear-gradient(135deg, #059669, #10b981);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin: 25px 0;
    box-shadow: 0 10px 30px rgba(5,150,105,0.25);
}

.net-title {
    font-size: 18px;
    font-weight: 600;
}

.net-value {
    font-size: 38px;
    font-weight: 800;
    margin-top: 10px;
}

.net-description {
    font-size: 14px;
    margin-top: 5px;
}

/* Bảng */
.table-box {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 30px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. TIÊU ĐỀ
# =========================================================

st.markdown("""
<div class="header-box">
    <h1>💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN</h1>
    <p>
        Công cụ hỗ trợ tính toán thuế TNCN và lương thực nhận hàng tháng
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 4. NHẬP THÔNG TIN
# =========================================================

st.markdown(
    '<div class="section-title">📝 THÔNG TIN THU NHẬP</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 💵 Lương Gross")

    gross_salary = st.number_input(
        "Lương Gross (đồng/tháng)",
        min_value=0,
        value=30000000,
        step=1000000,
        format="%d"
    )

with col2:

    st.markdown("### 👨‍👩‍👧‍👦 Người phụ thuộc")

    dependents = st.number_input(
        "Số người phụ thuộc",
        min_value=0,
        value=0,
        step=1
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 5. TÍNH BẢO HIỂM
# =========================================================

BHXH = gross_salary * 0.08

BHYT = gross_salary * 0.015

BHTN = gross_salary * 0.01

insurance = BHXH + BHYT + BHTN


# =========================================================
# 6. GIẢM TRỪ
# =========================================================

personal_deduction = 15500000

dependent_deduction = dependents * 6200000


# =========================================================
# 7. THU NHẬP TÍNH THUẾ
# =========================================================

taxable_income = (
    gross_salary
    - insurance
    - personal_deduction
    - dependent_deduction
)

if taxable_income < 0:
    taxable_income = 0


# =========================================================
# 8. HÀM TÍNH THUẾ
# =========================================================

def calculate_tax(income):

    if income <= 10000000:

        tax = income * 0.05

    elif income <= 30000000:

        tax = (
            10000000 * 0.05
            + (income - 10000000) * 0.10
        )

    elif income <= 60000000:

        tax = (
            10000000 * 0.05
            + 20000000 * 0.10
            + (income - 30000000) * 0.20
        )

    elif income <= 100000000:

        tax = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + (income - 60000000) * 0.30
        )

    else:

        tax = (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + 40000000 * 0.30
            + (income - 100000000) * 0.35
        )

    return tax


# =========================================================
# 9. TÍNH THUẾ VÀ LƯƠNG NET
# =========================================================

tax = calculate_tax(taxable_income)

net_salary = gross_salary - insurance - tax


# =========================================================
# 10. KẾT QUẢ
# =========================================================

st.markdown(
    '<div class="section-title">📊 KẾT QUẢ TÍNH TOÁN</div>',
    unsafe_allow_html=True
)


# =========================================================
# 11. LƯƠNG NET
# =========================================================

st.markdown(
    f"""
    <div class="net-box">
        <div class="net-title">
            💵 LƯƠNG THỰC NHẬN
        </div>

        <div class="net-value">
            {net_salary:,.0f} đ
        </div>

        <div class="net-description">
            Số tiền ước tính nhận được mỗi tháng
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 12. 4 CARD KẾT QUẢ
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                💵 LƯƠNG GROSS
            </div>

            <div class="result-value">
                {gross_salary:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                🏦 TỔNG BẢO HIỂM
            </div>

            <div class="result-value">
                {insurance:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                📊 THU NHẬP TÍNH THUẾ
            </div>

            <div class="result-value">
                {taxable_income:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                💸 THUẾ TNCN
            </div>

            <div class="result-value">
                {tax:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 13. TỶ LỆ LƯƠNG NET
# =========================================================

st.markdown(
    '<div class="section-title">📈 TỶ LỆ LƯƠNG THỰC NHẬN</div>',
    unsafe_allow_html=True
)

if gross_salary > 0:

    net_ratio = net_salary / gross_salary

else:

    net_ratio = 0


st.progress(
    min(max(net_ratio, 0.0), 1.0)
)

st.info(
    f"Bạn thực nhận khoảng **{net_ratio * 100:.1f}%** "
    f"so với mức lương Gross."
)


# =========================================================
# 14. CHI TIẾT BẢO HIỂM
# =========================================================

st.markdown(
    '<div class="section-title">🏦 CHI TIẾT BẢO HIỂM</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                BHXH – 8%
            </div>

            <div class="result-value">
                {BHXH:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                BHYT – 1.5%
            </div>

            <div class="result-value">
                {BHYT:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                BHTN – 1%
            </div>

            <div class="result-value">
                {BHTN:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 15. CHI TIẾT GIẢM TRỪ
# =========================================================

st.markdown(
    '<div class="section-title">📉 CHI TIẾT GIẢM TRỪ</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                👤 GIẢM TRỪ BẢN THÂN
            </div>

            <div class="result-value">
                {personal_deduction:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                👨‍👩‍👧‍👦 SỐ NGƯỜI PHỤ THUỘC
            </div>

            <div class="result-value">
                {dependents:.0f} người
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">
                👨‍👩‍👧‍👦 GIẢM TRỪ NGƯỜI PHỤ THUỘC
            </div>

            <div class="result-value">
                {dependent_deduction:,.0f} đ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 16. THÔNG BÁO
# =========================================================

if taxable_income == 0:

    st.success(
        "✅ Thu nhập tính thuế bằng 0. "
        "Theo công thức hiện tại, bạn không phát sinh thuế TNCN."
    )

else:

    st.warning(
        f"⚠️ Thu nhập tính thuế: "
        f"{taxable_income:,.0f} đồng/tháng."
    )


# =========================================================
# 17. BẢNG CHI TIẾT
# =========================================================

st.markdown(
    '<div class="section-title">🧾 CHI TIẾT TÍNH LƯƠNG</div>',
    unsafe_allow_html=True
)

data = {

    "Khoản mục": [

        "💵 Lương Gross",

        "🏦 BHXH",

        "🏥 BHYT",

        "🛡️ BHTN",

        "🏦 Tổng bảo hiểm",

        "👤 Giảm trừ bản thân",

        "👨‍👩‍👧‍👦 Giảm trừ người phụ thuộc",

        "📊 Thu nhập tính thuế",

        "💸 Thuế TNCN",

        "💰 Lương Net"

    ],

    "Số tiền (đồng)": [

        f"{gross_salary:,.0f}",

        f"{BHXH:,.0f}",

        f"{BHYT:,.0f}",

        f"{BHTN:,.0f}",

        f"{insurance:,.0f}",

        f"{personal_deduction:,.0f}",

        f"{dependent_deduction:,.0f}",

        f"{taxable_income:,.0f}",

        f"{tax:,.0f}",

        f"{net_salary:,.0f}"

    ]

}

st.markdown(
    '<div class="table-box">',
    unsafe_allow_html=True
)

st.table(data)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 18. BIỂU THUẾ
# =========================================================

st.markdown(
    '<div class="section-title">📚 BIỂU THUẾ LŨY TIẾN TỪNG PHẦN</div>',
    unsafe_allow_html=True
)

with st.expander("🔍 Xem biểu thuế và công thức"):

    st.markdown("""
    ### Bậc 1
    Đến 10 triệu đồng → **5%**

    ### Bậc 2
    Trên 10 đến 30 triệu đồng → **10%**

    ### Bậc 3
    Trên 30 đến 60 triệu đồng → **20%**

    ### Bậc 4
    Trên 60 đến 100 triệu đồng → **30%**

    ### Bậc 5
    Trên 100 triệu đồng → **35%**

    ---

    ### Công thức tổng quát

    **Tổng bảo hiểm = BHXH + BHYT + BHTN**

    **Thu nhập tính thuế = Lương Gross - Tổng bảo hiểm - Giảm trừ bản thân - Giảm trừ người phụ thuộc**

    **Lương Net = Lương Gross - Tổng bảo hiểm - Thuế TNCN**
    """)


# =========================================================
# 19. FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        💰 Ứng dụng tính Thuế Thu nhập cá nhân
        <br>
        Công cụ hỗ trợ tính toán và tham khảo
    </div>
    """,
    unsafe_allow_html=True
)
