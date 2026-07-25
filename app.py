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

    /* ===== NỀN CHÍNH ===== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f5f7fb 0%,
            #eef3f8 50%,
            #f8fafc 100%
        );
    }


    /* ===== TIÊU ĐỀ ===== */

    .main-title {
        background: linear-gradient(
            135deg,
            #0f4c81,
            #1677b7
        );

        padding: 30px 35px;
        border-radius: 20px;

        color: white;

        box-shadow:
            0 10px 30px rgba(15, 76, 129, 0.20);

        margin-bottom: 25px;
    }

    .main-title h1 {
        font-size: 32px;
        margin: 0;
        font-weight: 700;
    }

    .main-title p {
        margin-top: 8px;
        font-size: 16px;
        opacity: 0.9;
    }


    /* ===== SECTION ===== */

    .section-title {
        color: #0f4c81;
        font-size: 24px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 15px;
    }


    /* ===== CARD NHẬP LIỆU ===== */

    .input-card {
        background: white;
        padding: 25px;

        border-radius: 18px;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.06);

        margin-bottom: 20px;
    }


    /* ===== KPI CARD ===== */

    .metric-card {
        background: white;

        padding: 22px;

        border-radius: 18px;

        border-left: 5px solid #1677b7;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.06);

        min-height: 125px;

        margin-bottom: 15px;
    }

    .metric-title {
        color: #64748b;

        font-size: 14px;

        font-weight: 600;

        margin-bottom: 8px;
    }

    .metric-value {
        color: #0f172a;

        font-size: 23px;

        font-weight: 700;
    }


    /* ===== CARD LƯƠNG NET ===== */

    .net-card {
        background: linear-gradient(
            135deg,
            #059669,
            #10b981
        );

        padding: 30px;

        border-radius: 20px;

        color: white;

        text-align: center;

        box-shadow:
            0 12px 30px rgba(5, 150, 105, 0.25);

        margin-top: 20px;
        margin-bottom: 25px;
    }

    .net-title {
        font-size: 17px;

        font-weight: 600;

        opacity: 0.9;
    }

    .net-value {
        font-size: 36px;

        font-weight: 800;

        margin-top: 8px;
    }

    .net-subtitle {
        font-size: 14px;

        opacity: 0.85;

        margin-top: 5px;
    }


    /* ===== INFO CARD ===== */

    .info-card {
        background: white;

        padding: 25px;

        border-radius: 18px;

        border: 1px solid #e5e7eb;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.05);

        margin-top: 20px;
    }


    /* ===== TAX CARD ===== */

    .tax-card {
        background: #fff7ed;

        border-left: 5px solid #f97316;

        padding: 20px;

        border-radius: 15px;

        margin-top: 20px;
    }


    /* ===== TABLE ===== */

    [data-testid="stTable"] {
        background: white;

        border-radius: 15px;

        overflow: hidden;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.05);
    }


    /* ===== INPUT ===== */

    div[data-baseweb="input"] {
        border-radius: 10px;
    }


    /* ===== BUTTON ===== */

    .stButton > button {
        width: 100%;

        border-radius: 10px;

        height: 45px;

        background: #0f4c81;

        color: white;

        border: none;

        font-weight: 600;
    }


    /* ===== FOOTER ===== */

    .footer {
        text-align: center;

        color: #64748b;

        font-size: 13px;

        padding: 25px 0;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. TIÊU ĐỀ
# =========================================================

st.markdown("""
<div class="main-title">

    <h1>💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN</h1>

    <p>
        Công cụ hỗ trợ ước tính thuế TNCN và lương thực nhận hàng tháng
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
    '<div class="input-card">',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 💵 Mức lương")

    gross_salary = st.number_input(
        "Lương Gross (đồng/tháng)",
        min_value=0,
        value=30_000_000,
        step=1_000_000,
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

personal_deduction = 15_500_000

dependent_deduction = dependents * 6_200_000


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
# 8. HÀM TÍNH THUẾ LŨY TIẾN
# =========================================================

def calculate_tax(income):

    tax = 0

    if income <= 10_000_000:

        tax = income * 0.05

    elif income <= 30_000_000:

        tax = (
            10_000_000 * 0.05
            + (income - 10_000_000) * 0.10
        )

    elif income <= 60_000_000:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + (income - 30_000_000) * 0.20
        )

    elif income <= 100_000_000:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + (income - 60_000_000) * 0.30
        )

    else:

        tax = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + 40_000_000 * 0.30
            + (income - 100_000_000) * 0.35
        )

    return tax


# =========================================================
# 9. TÍNH THUẾ
# =========================================================

tax = calculate_tax(taxable_income)


# =========================================================
# 10. TÍNH LƯƠNG NET
# =========================================================

net_salary = gross_salary - insurance - tax


# =========================================================
# 11. KẾT QUẢ TỔNG QUAN
# =========================================================

st.markdown(
    '<div class="section-title">📊 KẾT QUẢ TÍNH TOÁN</div>',
    unsafe_allow_html=True
)


# =========================================================
# 12. LƯƠNG NET
# =========================================================

st.markdown(f"""
<div class="net-card">

    <div class="net-title">
        💵 LƯƠNG THỰC NHẬN
    </div>

    <div class="net-value">
        {net_salary:,.0f} đ
    </div>

    <div class="net-subtitle">
        Số tiền ước tính nhận được mỗi tháng
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 13. CÁC CHỈ SỐ CHÍNH
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            💵 LƯƠNG GROSS
        </div>

        <div class="metric-value">
            {gross_salary:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            🏦 TỔNG BẢO HIỂM
        </div>

        <div class="metric-value">
            {insurance:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            🧾 THU NHẬP TÍNH THUẾ
        </div>

        <div class="metric-value">
            {taxable_income:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            💸 THUẾ TNCN
        </div>

        <div class="metric-value">
            {tax:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 14. TỶ LỆ LƯƠNG THỰC NHẬN
# =========================================================

if gross_salary > 0:

    net_ratio = net_salary / gross_salary

else:

    net_ratio = 0


st.markdown(
    '<div class="info-card">',
    unsafe_allow_html=True
)

st.markdown("### 📈 Tỷ lệ lương thực nhận")

st.progress(
    min(max(net_ratio, 0.0), 1.0)
)

st.write(
    f"Bạn thực nhận khoảng **{net_ratio * 100:.1f}%** "
    f"so với mức lương Gross."
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 15. CHI TIẾT BẢO HIỂM
# =========================================================

st.markdown(
    '<div class="section-title">🏦 CHI TIẾT CÁC KHOẢN BẢO HIỂM</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            BHXH – 8%
        </div>

        <div class="metric-value">
            {BHXH:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            BHYT – 1.5%
        </div>

        <div class="metric-value">
            {BHYT:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            BHTN – 1%
        </div>

        <div class="metric-value">
            {BHTN:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 16. CHI TIẾT GIẢM TRỪ
# =========================================================

st.markdown(
    '<div class="section-title">📉 CÁC KHOẢN GIẢM TRỪ</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            👤 Giảm trừ bản thân
        </div>

        <div class="metric-value">
            {personal_deduction:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            👨‍👩‍👧‍👦 Số người phụ thuộc
        </div>

        <div class="metric-value">
            {dependents:.0f} người
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            👨‍👩‍👧‍👦 Giảm trừ người phụ thuộc
        </div>

        <div class="metric-value">
            {dependent_deduction:,.0f} đ
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 17. CẢNH BÁO
# =========================================================

if taxable_income == 0:

    st.success(
        "✅ Thu nhập tính thuế bằng 0. "
        "Theo công thức đang sử dụng, bạn không phát sinh thuế TNCN."
    )

else:

    st.warning(
        f"⚠️ Thu nhập tính thuế của bạn là "
        f"{taxable_income:,.0f} đồng/tháng."
    )


# =========================================================
# 18. BẢNG CHI TIẾT
# =========================================================

st.markdown(
    '<div class="section-title">🧾 BẢNG CHI TIẾT TÍNH LƯƠNG</div>',
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
# 19. CÁCH TÍNH THUẾ
# =========================================================

st.markdown(
    '<div class="section-title">📚 BIỂU THUẾ LŨY TIẾN TỪNG PHẦN</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="tax-card">

<h3>🧮 Các bậc thuế đang áp dụng trong công thức</h3>

<p><b>Bậc 1:</b> Đến 10 triệu đồng → Thuế suất 5%</p>

<p><b>Bậc 2:</b> Trên 10 – 30 triệu đồng → Thuế suất 10%</p>

<p><b>Bậc 3:</b> Trên 30 – 60 triệu đồng → Thuế suất 20%</p>

<p><b>Bậc 4:</b> Trên 60 – 100 triệu đồng → Thuế suất 30%</p>

<p><b>Bậc 5:</b> Trên 100 triệu đồng → Thuế suất 35%</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 20. CÔNG THỨC TỔNG QUÁT
# =========================================================

with st.expander("🔍 Xem công thức tính chi tiết"):

    st.markdown("""
### 1️⃣ Tổng bảo hiểm

**Tổng bảo hiểm = BHXH + BHYT + BHTN**

Trong đó:

- BHXH = Lương Gross × 8%
- BHYT = Lương Gross × 1,5%
- BHTN = Lương Gross × 1%

---

### 2️⃣ Thu nhập tính thuế

**Thu nhập tính thuế = Lương Gross – Tổng bảo hiểm – Giảm trừ bản thân – Giảm trừ người phụ thuộc**

Nếu kết quả nhỏ hơn 0 thì thu nhập tính thuế được tính bằng 0.

---

### 3️⃣ Thuế TNCN

Thuế TNCN được tính theo **biểu thuế lũy tiến từng phần**.

---

### 4️⃣ Lương thực nhận

**Lương Net = Lương Gross – Tổng bảo hiểm – Thuế TNCN**
""")


# =========================================================
# 21. FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    💰 Ứng dụng tính Thuế Thu nhập cá nhân
    
    <br>

    Công cụ hỗ trợ tính toán và tham khảo

</div>
""", unsafe_allow_html=True)
