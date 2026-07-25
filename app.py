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
# 2. CSS GIAO DIỆN
# =========================================================
# Lưu ý:
# - Không sử dụng HTML
# - Không sử dụng <div>
# - Không sử dụng <h1>
# - Không sử dụng unsafe_allow_html
# =========================================================

st.markdown(
    """
    <style>

    /* Nền chính */

    .stApp {
        background-color: #f4f7fb;
    }


    /* Sidebar */

    [data-testid="stSidebar"] {
        background-color: #0f2747;
    }


    /* Chữ trong Sidebar */

    [data-testid="stSidebar"] * {
        color: white;
    }


    /* Các ô Metric */

    [data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    }


    /* Input */

    [data-testid="stNumberInput"] {
        background-color: white;
        padding: 10px;
        border-radius: 12px;
    }


    /* Nút */

    .stButton button {
        border-radius: 10px;
        font-weight: 600;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 3. SIDEBAR
# =========================================================

with st.sidebar:

    st.title("💰 TNCN")

    st.write(
        "Ứng dụng tính thuế "
        "thu nhập cá nhân"
    )

    st.divider()

    st.subheader("📌 MENU")

    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🧮 Tính thuế TNCN",
            "📊 Chi tiết thu nhập",
            "📚 Biểu thuế"
        ]
    )

    st.divider()

    st.info(
        "Công cụ hỗ trợ tính toán:\n\n"
        "• Lương Gross\n\n"
        "• Bảo hiểm\n\n"
        "• Thu nhập tính thuế\n\n"
        "• Thuế TNCN\n\n"
        "• Lương Net"
    )


# =========================================================
# 4. TIÊU ĐỀ CHÍNH
# =========================================================

st.title(
    "💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN"
)

st.caption(
    "Công cụ hỗ trợ tính toán "
    "Lương Gross - Thuế TNCN - Lương Net"
)

st.divider()


# =========================================================
# 5. NHẬP THÔNG TIN
# =========================================================

st.header("📝 Thông tin thu nhập")

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

insurance = (
    BHXH
    + BHYT
    + BHTN
)


# =========================================================
# 7. TÍNH GIẢM TRỪ
# =========================================================

personal_deduction = 15500000

dependent_deduction = (
    dependents
    * 6200000
)


# =========================================================
# 8. TÍNH THU NHẬP TÍNH THUẾ
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
# 9. HÀM TÍNH THUẾ TNCN
# =========================================================

def calculate_tax(income):

    if income <= 10000000:

        tax = (
            income
            * 0.05
        )


    elif income <= 30000000:

        tax = (
            10000000
            * 0.05
            + (
                income
                - 10000000
            )
            * 0.10
        )


    elif income <= 60000000:

        tax = (
            10000000
            * 0.05

            + 20000000
            * 0.10

            + (
                income
                - 30000000
            )
            * 0.20
        )


    elif income <= 100000000:

        tax = (
            10000000
            * 0.05

            + 20000000
            * 0.10

            + 30000000
            * 0.20

            + (
                income
                - 60000000
            )
            * 0.30
        )


    else:

        tax = (
            10000000
            * 0.05

            + 20000000
            * 0.10

            + 30000000
            * 0.20

            + 40000000
            * 0.30

            + (
                income
                - 100000000
            )
            * 0.35
        )


    return tax


# =========================================================
# 10. TÍNH THUẾ
# =========================================================

tax = calculate_tax(
    taxable_income
)


# =========================================================
# 11. TÍNH LƯƠNG NET
# =========================================================

net_salary = (
    gross_salary
    - insurance
    - tax
)


# =========================================================
# 12. TÍNH TỶ LỆ LƯƠNG NET
# =========================================================

if gross_salary > 0:

    net_ratio = (
        net_salary
        / gross_salary
    )

else:

    net_ratio = 0


# =========================================================
# 13. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.header(
        "📊 Tổng quan tài chính"
    )


    # -----------------------------------------------------
    # LƯƠNG THỰC NHẬN
    # -----------------------------------------------------

    st.subheader(
        "💵 Lương thực nhận"
    )


    st.success(
        f"💰 LƯƠNG NET: "
        f"{net_salary:,.0f} đồng/tháng"
    )


    st.caption(
        "Số tiền ước tính nhận được "
        "sau khi trừ bảo hiểm và thuế TNCN."
    )


    # -----------------------------------------------------
    # KPI
    # -----------------------------------------------------

    st.subheader(
        "📌 Các chỉ tiêu chính"
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


    st.divider()


    # -----------------------------------------------------
    # TỶ LỆ LƯƠNG NET
    # -----------------------------------------------------

    st.subheader(
        "📈 Tỷ lệ lương thực nhận"
    )


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
        f"Lương thực nhận chiếm "
        f"**{net_ratio * 100:.1f}%** "
        f"so với lương Gross."
    )


    # -----------------------------------------------------
    # THÔNG TIN NGƯỜI PHỤ THUỘC
    # -----------------------------------------------------

    st.subheader(
        "👨‍👩‍👧‍👦 Thông tin người phụ thuộc"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            label="Số người phụ thuộc",
            value=f"{dependents:.0f} người"
        )


    with col2:

        st.metric(
            label="Giảm trừ người phụ thuộc",
            value=f"{dependent_deduction:,.0f} đ"
        )


    # -----------------------------------------------------
    # TÌNH TRẠNG THUẾ
    # -----------------------------------------------------

    st.subheader(
        "🔔 Tình trạng thuế"
    )


    if taxable_income == 0:

        st.success(
            "✅ Bạn không phát sinh "
            "thuế TNCN theo công thức hiện tại."
        )

    else:

        st.warning(
            f"⚠️ Thu nhập tính thuế: "
            f"{taxable_income:,.0f} đồng/tháng."
        )


# =========================================================
# 14. TRANG TÍNH THUẾ
# =========================================================

elif menu == "🧮 Tính thuế TNCN":

    st.header(
        "🧮 Tính toán thuế TNCN"
    )


    st.subheader(
        "📥 Thông tin đầu vào"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "💵 Lương Gross",
            f"{gross_salary:,.0f} đ"
        )


    with col2:

        st.metric(
            "👨‍👩‍👧‍👦 Người phụ thuộc",
            f"{dependents:.0f} người"
        )


    st.divider()


    st.subheader(
        "📉 Các khoản khấu trừ"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🏦 BHXH",
            f"{BHXH:,.0f} đ"
        )


    with col2:

        st.metric(
            "🏥 BHYT",
            f"{BHYT:,.0f} đ"
        )


    with col3:

        st.metric(
            "🛡️ BHTN",
            f"{BHTN:,.0f} đ"
        )


    st.divider()


    st.subheader(
        "📊 Kết quả tính thuế"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Tổng bảo hiểm",
            f"{insurance:,.0f} đ"
        )


    with col2:

        st.metric(
            "Thu nhập tính thuế",
            f"{taxable_income:,.0f} đ"
        )


    with col3:

        st.metric(
            "Thuế TNCN",
            f"{tax:,.0f} đ"
        )


    st.divider()


    st.success(
        f"💰 Lương thực nhận "
        f"(Lương Net): "
        f"{net_salary:,.0f} đồng/tháng"
    )


# =========================================================
# 15. TRANG CHI TIẾT THU NHẬP
# =========================================================

elif menu == "📊 Chi tiết thu nhập":

    st.header(
        "📊 Chi tiết thu nhập"
    )


    # -----------------------------------------------------
    # BẢO HIỂM
    # -----------------------------------------------------

    st.subheader(
        "🏦 Chi tiết bảo hiểm"
    )


    col1, col2, col3, col4 = st.columns(4)


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


    with col4:

        st.metric(
            "Tổng bảo hiểm",
            f"{insurance:,.0f} đ"
        )


    st.divider()


    # -----------------------------------------------------
    # GIẢM TRỪ
    # -----------------------------------------------------

    st.subheader(
        "📉 Chi tiết giảm trừ"
    )


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


    # -----------------------------------------------------
    # BẢNG CHI TIẾT
    # -----------------------------------------------------

    st.subheader(
        "🧾 Bảng chi tiết tính lương"
    )


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
# 16. TRANG BIỂU THUẾ
# =========================================================

elif menu == "📚 Biểu thuế":

    st.header(
        "📚 Biểu thuế lũy tiến từng phần"
    )


    st.info(
        "Thuế TNCN được tính theo "
        "phương pháp lũy tiến từng phần."
    )


    tax_data = pd.DataFrame({

        "Bậc": [

            "Bậc 1",

            "Bậc 2",

            "Bậc 3",

            "Bậc 4",

            "Bậc 5"

        ],


        "Thu nhập tính thuế": [

            "Đến 10 triệu đồng",

            "Trên 10 - 30 triệu đồng",

            "Trên 30 - 60 triệu đồng",

            "Trên 60 - 100 triệu đồng",

            "Trên 100 triệu đồng"

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


    st.divider()


    st.subheader(
        "🧮 Công thức tính"
    )


    st.info(
        "Tổng bảo hiểm = BHXH + BHYT + BHTN"
    )


    st.info(
        "Thu nhập tính thuế = "
        "Lương Gross - Tổng bảo hiểm "
        "- Giảm trừ bản thân "
        "- Giảm trừ người phụ thuộc"
    )


    st.info(
        "Lương Net = "
        "Lương Gross - Tổng bảo hiểm "
        "- Thuế TNCN"
    )


# =========================================================
# 17. FOOTER
# =========================================================

st.divider()

st.caption(
    "💰 Ứng dụng tính Thuế Thu nhập cá nhân "
    "| Công cụ hỗ trợ tính toán và tham khảo"
)
