import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Tính Thuế TNCN",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. CSS - GIAO DIỆN
# =========================================================

st.markdown("""
<style>

    /* ==============================
       NỀN ỨNG DỤNG
    ============================== */

    .stApp {
        background-color: #f4f7fb;
    }

    /* ==============================
       SIDEBAR
    ============================== */

    [data-testid="stSidebar"] {
        background-color: #0f2747;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    /* ==============================
       TIÊU ĐỀ
    ============================== */

    .main-title {
        font-size: 32px;
        font-weight: 800;
        color: #0f2747;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #64748b;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* ==============================
       CARD
    ============================== */

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.05);
        margin-bottom: 20px;
    }

    /* ==============================
       KẾT QUẢ LƯƠNG NET
    ============================== */

    .net-card {
        background-color: #0f766e;
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(15, 118, 110, 0.2);
        margin-bottom: 25px;
    }

    .net-label {
        font-size: 16px;
        font-weight: 600;
    }

    .net-money {
        font-size: 38px;
        font-weight: 800;
        margin-top: 8px;
    }

    .net-note {
        font-size: 14px;
        opacity: 0.9;
        margin-top: 5px;
    }

    /* ==============================
       SECTION
    ============================== */

    .section-title {
        color: #0f2747;
        font-size: 22px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* ==============================
       FOOTER
    ============================== */

    .footer {
        text-align: center;
        color: #64748b;
        padding: 25px;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. SIDEBAR
# =========================================================

with st.sidebar:

    st.title("💰 TNCN")

    st.write("Ứng dụng tính thuế thu nhập cá nhân")

    st.divider()

    st.markdown("### 📌 Danh mục")

    menu = st.radio(
        "Chọn nội dung",
        [
            "🏠 Tổng quan",
            "🧮 Tính thuế TNCN",
            "📊 Chi tiết thu nhập",
            "📚 Biểu thuế"
        ]
    )

    st.divider()

    st.caption(
        "Công cụ hỗ trợ tính toán\n"
        "Lương Gross - Thuế TNCN - Lương Net"
    )


# =========================================================
# 4. TIÊU ĐỀ CHÍNH
# =========================================================

st.markdown(
    '<div class="main-title">💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Quản lý và tính toán thu nhập cá nhân một cách trực quan</div>',
    unsafe_allow_html=True
)


# =========================================================
# 5. NHẬP THÔNG TIN
# =========================================================

st.markdown(
    '<div class="section-title">📝 Thông tin thu nhập</div>',
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
# 6. TÍNH BẢO HIỂM
# =========================================================

BHXH = gross_salary * 0.08

BHYT = gross_salary * 0.015

BHTN = gross_salary * 0.01

insurance = BHXH + BHYT + BHTN


# =========================================================
# 7. GIẢM TRỪ
# =========================================================

personal_deduction = 15500000

dependent_deduction = (
    dependents * 6200000
)


# =========================================================
# 8. THU NHẬP TÍNH THUẾ
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
# 9. HÀM TÍNH THUẾ
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
# 10. TÍNH THUẾ VÀ LƯƠNG NET
# =========================================================

tax = calculate_tax(
    taxable_income
)

net_salary = (
    gross_salary
    - insurance
    - tax
)


# =========================================================
# 11. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        '<div class="section-title">📊 Tổng quan tài chính</div>',
        unsafe_allow_html=True
    )

    # Lương Net

    st.markdown(
        f"""
        <div class="net-card">

            <div class="net-label">
                💵 LƯƠNG THỰC NHẬN
            </div>

            <div class="net-money">
                {net_salary:,.0f} đồng
            </div>

            <div class="net-note">
                Số tiền ước tính nhận được mỗi tháng
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # KPI

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "💵 Lương Gross",
            f"{gross_salary:,.0f} đ"
        )


    with col2:

        st.metric(
            "🏦 Bảo hiểm",
            f"{insurance:,.0f} đ"
        )


    with col3:

        st.metric(
            "📊 Thu nhập tính thuế",
            f"{taxable_income:,.0f} đ"
        )


    with col4:

        st.metric(
            "💸 Thuế TNCN",
            f"{tax:,.0f} đ"
        )


    st.divider()


    # Tỷ lệ

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("📈 Tỷ lệ lương thực nhận")

        if gross_salary > 0:

            net_ratio = (
                net_salary
                / gross_salary
            )

        else:

            net_ratio = 0


        st.progress(
            min(
                max(
                    net_ratio,
                    0.0
                ),
                1.0
            )
        )

        st.write(
            f"Lương Net chiếm "
            f"**{net_ratio * 100:.1f}%** "
            f"lương Gross."
        )


    with col2:

        st.subheader("👨‍👩‍👧‍👦 Người phụ thuộc")

        st.metric(
            "Số người phụ thuộc",
            f"{dependents:.0f} người"
        )

        st.write(
            f"Giảm trừ người phụ thuộc: "
            f"**{dependent_deduction:,.0f} đ**"
        )


# =========================================================
# 12. TÍNH THUẾ TNCN
# =========================================================

elif menu == "🧮 Tính thuế TNCN":

    st.markdown(
        '<div class="section-title">🧮 Tính toán thuế TNCN</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("📥 Các khoản đầu vào")

        st.write(
            f"💵 Lương Gross: "
            f"**{gross_salary:,.0f} đ**"
        )

        st.write(
            f"👨‍👩‍👧‍👦 Người phụ thuộc: "
            f"**{dependents:.0f} người**"
        )


    with col2:

        st.subheader("📤 Kết quả")

        st.write(
            f"🏦 Tổng bảo hiểm: "
            f"**{insurance:,.0f} đ**"
        )

        st.write(
            f"📊 Thu nhập tính thuế: "
            f"**{taxable_income:,.0f} đ**"
        )

        st.write(
            f"💸 Thuế TNCN: "
            f"**{tax:,.0f} đ**"
        )


    st.divider()

    st.success(
        f"💰 Lương Net dự kiến: "
        f"{net_salary:,.0f} đồng/tháng"
    )


# =========================================================
# 13. CHI TIẾT THU NHẬP
# =========================================================

elif menu == "📊 Chi tiết thu nhập":

    st.markdown(
        '<div class="section-title">📊 Phân tích chi tiết thu nhập</div>',
        unsafe_allow_html=True
    )


    # Bảo hiểm

    st.subheader("🏦 Các khoản bảo hiểm")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "BHXH (8%)",
            f"{BHXH:,.0f} đ"
        )


    with col2:

        st.metric(
            "BHYT (1.5%)",
            f"{BHYT:,.0f} đ"
        )


    with col3:

        st.metric(
            "BHTN (1%)",
            f"{BHTN:,.0f} đ"
        )


    st.divider()


    # Giảm trừ

    st.subheader("📉 Các khoản giảm trừ")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Giảm trừ bản thân",
            f"{personal_deduction:,.0f} đ"
        )


    with col2:

        st.metric(
            "Số người phụ thuộc",
            f"{dependents:.0f} người"
        )


    with col3:

        st.metric(
            "Giảm trừ người phụ thuộc",
            f"{dependent_deduction:,.0f} đ"
        )


    st.divider()


    # Bảng

    st.subheader("🧾 Bảng chi tiết")

    data = pd.DataFrame({

        "Khoản mục": [

            "Lương Gross",

            "BHXH",

            "BHYT",

            "BHTN",

            "Tổng bảo hiểm",

            "Giảm trừ bản thân",

            "Giảm trừ người phụ thuộc",

            "Thu nhập tính thuế",

            "Thuế TNCN",

            "Lương Net"

        ],

        "Số tiền (đồng)": [

            gross_salary,

            BHXH,

            BHYT,

            BHTN,

            insurance,

            personal_deduction,

            dependent_deduction,

            taxable_income,

            tax,

            net_salary

        ]

    })


    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# 14. BIỂU THUẾ
# =========================================================

elif menu == "📚 Biểu thuế":

    st.markdown(
        '<div class="section-title">📚 Biểu thuế lũy tiến từng phần</div>',
        unsafe_allow_html=True
    )


    tax_data = pd.DataFrame({

        "Bậc": [

            "Bậc 1",

            "Bậc 2",

            "Bậc 3",

            "Bậc 4",

            "Bậc 5"

        ],

        "Phần thu nhập tính thuế": [

            "Đến 10 triệu",

            "Trên 10 - 30 triệu",

            "Trên 30 - 60 triệu",

            "Trên 60 - 100 triệu",

            "Trên 100 triệu"

        ],

        "Thuế suất": [

            "5%",

            "10%",

            "20%",

            "30%",

            "35%"

        ]

    })


    st.dataframe(
        tax_data,
        use_container_width=True,
        hide_index=True
    )


    st.info(
        "Thuế TNCN được tính theo phương pháp lũy tiến từng phần."
    )


# =========================================================
# 15. FOOTER
# =========================================================

st.divider()

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
