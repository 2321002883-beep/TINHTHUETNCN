import streamlit as st

# =========================================================
# 1. CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="Ứng dụng tính Thuế TNCN",
    page_icon="💰",
    layout="wide"
)


# =========================================================
# 2. CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

/* Tiêu đề */
.header-box {
    background: linear-gradient(135deg, #0f4c81, #1976b9);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.header-box h1 {
    margin: 0;
    font-size: 32px;
}

.header-box p {
    margin-top: 10px;
    font-size: 16px;
}

/* Tiêu đề section */
.section-title {
    color: #0f4c81;
    font-size: 24px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Khung lương Net */
.net-box {
    background: linear-gradient(135deg, #059669, #10b981);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin: 20px 0 30px 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}

.net-title {
    font-size: 20px;
    font-weight: bold;
}

.net-value {
    font-size: 40px;
    font-weight: bold;
    margin: 10px 0;
}

.net-description {
    font-size: 15px;
}

/* Metric */
[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    border-left: 4px solid #1976b9;
}

/* Input */
[data-testid="stNumberInput"] {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
    margin-top: 30px;
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
        Công cụ hỗ trợ tính toán Lương Gross - Thuế TNCN - Lương Net
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

col1, col2 = st.columns(2)

with col1:

    gross_salary = st.number_input(
        "💵 Lương Gross (đồng/tháng)",
        min_value=0,
        value=30000000,
        step=1000000
    )


with col2:

    dependents = st.number_input(
        "👨‍👩‍👧‍👦 Số người phụ thuộc",
        min_value=0,
        value=0,
        step=1
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

        return income * 0.05

    elif income <= 30000000:

        return (
            10000000 * 0.05
            + (income - 10000000) * 0.10
        )

    elif income <= 60000000:

        return (
            10000000 * 0.05
            + 20000000 * 0.10
            + (income - 30000000) * 0.20
        )

    elif income <= 100000000:

        return (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + (income - 60000000) * 0.30
        )

    else:

        return (
            10000000 * 0.05
            + 20000000 * 0.10
            + 30000000 * 0.20
            + 40000000 * 0.30
            + (income - 100000000) * 0.35
        )


# =========================================================
# 9. TÍNH THUẾ
# =========================================================

tax = calculate_tax(taxable_income)


# =========================================================
# 10. LƯƠNG NET
# =========================================================

net_salary = gross_salary - insurance - tax


# =========================================================
# 11. LƯƠNG THỰC NHẬN
# =========================================================

st.markdown(
    '<div class="section-title">💰 KẾT QUẢ LƯƠNG THỰC NHẬN</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="net-box">

        <div class="net-title">
            💵 LƯƠNG THỰC NHẬN
        </div>

        <div class="net-value">
            {net_salary:,.0f} đồng
        </div>

        <div class="net-description">
            Số tiền ước tính nhận được mỗi tháng
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 12. KẾT QUẢ TỔNG QUAN
# =========================================================

st.markdown(
    '<div class="section-title">📊 KẾT QUẢ TỔNG QUAN</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="💵 Lương Gross",
        value=f"{gross_salary:,.0f} đ"
    )

with col2:

    st.metric(
        label="🏦 Tổng bảo hiểm",
        value=f"{insurance:,.0f} đ"
    )

with col3:

    st.metric(
        label="📊 Thu nhập tính thuế",
        value=f"{taxable_income:,.0f} đ"
    )

with col4:

    st.metric(
        label="💸 Thuế TNCN",
        value=f"{tax:,.0f} đ"
    )


# =========================================================
# 13. TỶ LỆ LƯƠNG THỰC NHẬN
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

    st.metric(
        label="🏦 BHXH (8%)",
        value=f"{BHXH:,.0f} đ"
    )

with col2:

    st.metric(
        label="🏥 BHYT (1.5%)",
        value=f"{BHYT:,.0f} đ"
    )

with col3:

    st.metric(
        label="🛡️ BHTN (1%)",
        value=f"{BHTN:,.0f} đ"
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

    st.metric(
        label="👤 Giảm trừ bản thân",
        value=f"{personal_deduction:,.0f} đ"
    )

with col2:

    st.metric(
        label="👨‍👩‍👧‍👦 Số người phụ thuộc",
        value=f"{dependents:.0f} người"
    )

with col3:

    st.metric(
        label="👨‍👩‍👧‍👦 Giảm trừ người phụ thuộc",
        value=f"{dependent_deduction:,.0f} đ"
    )


# =========================================================
# 16. THÔNG BÁO
# =========================================================

if taxable_income == 0:

    st.success(
        "✅ Thu nhập tính thuế bằng 0. "
        "Bạn không phát sinh thuế TNCN theo công thức hiện tại."
    )

else:

    st.warning(
        f"⚠️ Thu nhập tính thuế của bạn là "
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

st.table(data)


# =========================================================
# 18. BIỂU THUẾ
# =========================================================

st.markdown(
    '<div class="section-title">📚 BIỂU THUẾ LŨY TIẾN TỪNG PHẦN</div>',
    unsafe_allow_html=True
)

with st.expander("🔍 Xem biểu thuế"):

    st.write(
        "Bậc 1: Đến 10 triệu đồng → 5%"
    )

    st.write(
        "Bậc 2: Trên 10 - 30 triệu đồng → 10%"
    )

    st.write(
        "Bậc 3: Trên 30 - 60 triệu đồng → 20%"
    )

    st.write(
        "Bậc 4: Trên 60 - 100 triệu đồng → 30%"
    )

    st.write(
        "Bậc 5: Trên 100 triệu đồng → 35%"
    )


# =========================================================
# 19. FOOTER
# =========================================================

st.markdown("---")

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
