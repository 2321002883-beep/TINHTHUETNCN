import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Hệ thống phân tích thuế TNCN",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f4f7fb;
    }

    [data-testid="stSidebar"] {
        background-color: #0f2747;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    }

    [data-testid="stNumberInput"] {
        background-color: white;
        border-radius: 12px;
    }

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
        "Hệ thống phân tích "
        "thu nhập và thuế TNCN"
    )

    st.divider()

    st.subheader("📌 MENU")

    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "📝 Thông tin thu nhập",
            "🏦 Phân tích bảo hiểm",
            "📉 Phân tích giảm trừ",
            "🧮 Phân tích thuế",
            "📊 Báo cáo chi tiết",
            "📚 Biểu thuế"
        ]
    )

    st.divider()

    st.info(
        "Hệ thống hỗ trợ:\n\n"
        "• Tổng hợp thu nhập Gross\n\n"
        "• Phân tích bảo hiểm\n\n"
        "• Tính giảm trừ\n\n"
        "• Tính thu nhập tính thuế\n\n"
        "• Tính thuế TNCN\n\n"
        "• Tính lương Net"
    )


# =========================================================
# 4. TIÊU ĐỀ
# =========================================================

st.title(
    "💰 HỆ THỐNG PHÂN TÍCH THUẾ THU NHẬP CÁ NHÂN"
)

st.caption(
    "Phân tích chi tiết từ thu nhập thành phần "
    "đến Lương Gross - Thuế TNCN - Lương Net"
)

st.divider()


# =========================================================
# 5. NHẬP THÔNG TIN THU NHẬP
# =========================================================

st.header("📝 Thông tin thu nhập")

st.write(
    "Nhập các khoản thu nhập hàng tháng. "
    "Hệ thống sẽ tự động tổng hợp thành tổng thu nhập Gross."
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("💵 Thu nhập chính")

    luong_co_ban = st.number_input(
        "Lương cơ bản (đồng/tháng)",
        min_value=0,
        value=20000000,
        step=500000
    )

    lam_them = st.number_input(
        "Tiền làm thêm giờ (đồng/tháng)",
        min_value=0,
        value=0,
        step=500000
    )

    thuong = st.number_input(
        "Tiền thưởng (đồng/tháng)",
        min_value=0,
        value=0,
        step=500000
    )


with col2:

    st.subheader("💰 Thu nhập bổ sung")

    phu_cap = st.number_input(
        "Phụ cấp (đồng/tháng)",
        min_value=0,
        value=0,
        step=500000
    )

    thu_nhap_khac = st.number_input(
        "Thu nhập khác (đồng/tháng)",
        min_value=0,
        value=0,
        step=500000
    )

    dependents = st.number_input(
        "Số người phụ thuộc",
        min_value=0,
        value=0,
        step=1
    )


# =========================================================
# 6. TỔNG HỢP THU NHẬP GROSS
# =========================================================

gross_salary = (
    luong_co_ban
    + lam_them
    + thuong
    + phu_cap
    + thu_nhap_khac
)


# =========================================================
# 7. BẢO HIỂM
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
# 8. GIẢM TRỪ
# =========================================================

personal_deduction = 15500000

dependent_deduction = (
    dependents
    * 6200000
)


# =========================================================
# 9. THU NHẬP TÍNH THUẾ
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
# 10. HÀM TÍNH THUẾ
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
# 11. TÍNH THUẾ
# =========================================================

tax = calculate_tax(
    taxable_income
)


# =========================================================
# 12. TÍNH LƯƠNG NET
# =========================================================

net_salary = (
    gross_salary
    - insurance
    - tax
)


# =========================================================
# 13. TỶ LỆ
# =========================================================

if gross_salary > 0:

    net_ratio = (
        net_salary
        / gross_salary
    )

else:

    net_ratio = 0


# =========================================================
# 14. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.header(
        "🏠 Tổng quan tài chính"
    )


    # -----------------------------------------------------
    # KẾT QUẢ CHÍNH
    # -----------------------------------------------------

    st.subheader(
        "💰 Kết quả tổng hợp"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "💵 Tổng thu nhập Gross",
            f"{gross_salary:,.0f} đ"
        )


    with col2:

        st.metric(
            "🏦 Tổng bảo hiểm",
            f"{insurance:,.0f} đ"
        )


    with col3:

        st.metric(
            "💸 Thuế TNCN",
            f"{tax:,.0f} đ"
        )


    with col4:

        st.metric(
            "💰 Lương Net",
            f"{net_salary:,.0f} đ"
        )


    st.divider()


    # -----------------------------------------------------
    # LƯƠNG NET
    # -----------------------------------------------------

    st.subheader(
        "💵 Lương thực nhận"
    )


    st.success(
        f"💰 Sau khi trừ bảo hiểm và thuế, "
        f"lương thực nhận dự kiến là "
        f"**{net_salary:,.0f} đồng/tháng**."
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


    st.caption(
        f"Lương Net chiếm "
        f"{net_ratio * 100:.1f}% "
        f"tổng thu nhập Gross."
    )


    st.divider()


    # -----------------------------------------------------
    # CƠ CẤU THU NHẬP
    # -----------------------------------------------------

    st.subheader(
        "📊 Cơ cấu thu nhập"
    )


    income_data = pd.DataFrame({

        "Khoản thu nhập": [

            "Lương cơ bản",

            "Làm thêm giờ",

            "Thưởng",

            "Phụ cấp",

            "Thu nhập khác"

        ],

        "Số tiền": [

            luong_co_ban,

            lam_them,

            thuong,

            phu_cap,

            thu_nhap_khac

        ]

    })


    st.bar_chart(
        income_data.set_index(
            "Khoản thu nhập"
        )
    )


# =========================================================
# 15. THÔNG TIN THU NHẬP
# =========================================================

elif menu == "📝 Thông tin thu nhập":

    st.header(
        "📝 Phân tích các khoản thu nhập"
    )


    st.info(
        "Tổng thu nhập Gross được tổng hợp "
        "từ các khoản thu nhập bạn đã nhập."
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Lương cơ bản",
            f"{luong_co_ban:,.0f} đ"
        )

        st.metric(
            "Tiền làm thêm",
            f"{lam_them:,.0f} đ"
        )

        st.metric(
            "Tiền thưởng",
            f"{thuong:,.0f} đ"
        )


    with col2:

        st.metric(
            "Phụ cấp",
            f"{phu_cap:,.0f} đ"
        )

        st.metric(
            "Thu nhập khác",
            f"{thu_nhap_khac:,.0f} đ"
        )

        st.metric(
            "Tổng Gross",
            f"{gross_salary:,.0f} đ"
        )


    st.divider()


    st.subheader(
        "📊 Tỷ trọng từng khoản thu nhập"
    )


    if gross_salary > 0:

        income_ratio = pd.DataFrame({

            "Khoản thu nhập": [

                "Lương cơ bản",

                "Làm thêm",

                "Thưởng",

                "Phụ cấp",

                "Thu nhập khác"

            ],

            "Tỷ trọng (%)": [

                luong_co_ban
                / gross_salary
                * 100,

                lam_them
                / gross_salary
                * 100,

                thuong
                / gross_salary
                * 100,

                phu_cap
                / gross_salary
                * 100,

                thu_nhap_khac
                / gross_salary
                * 100

            ]

        })


        st.dataframe(
            income_ratio,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# 16. PHÂN TÍCH BẢO HIỂM
# =========================================================

elif menu == "🏦 Phân tích bảo hiểm":

    st.header(
        "🏦 Phân tích các khoản bảo hiểm"
    )


    st.subheader(
        "📊 Chi tiết bảo hiểm"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "BHXH - 8%",
            f"{BHXH:,.0f} đ"
        )


    with col2:

        st.metric(
            "BHYT - 1.5%",
            f"{BHYT:,.0f} đ"
        )


    with col3:

        st.metric(
            "BHTN - 1%",
            f"{BHTN:,.0f} đ"
        )


    with col4:

        st.metric(
            "Tổng bảo hiểm",
            f"{insurance:,.0f} đ"
        )


    st.divider()


    st.subheader(
        "📈 Tỷ lệ bảo hiểm trên Gross"
    )


    if gross_salary > 0:

        insurance_ratio = (
            insurance
            / gross_salary
        )

    else:

        insurance_ratio = 0


    st.progress(
        min(
            max(
                insurance_ratio,
                0.0
            ),
            1.0
        )
    )


    st.write(
        f"Tổng bảo hiểm chiếm "
        f"**{insurance_ratio * 100:.1f}%** "
        f"tổng thu nhập Gross."
    )


# =========================================================
# 17. PHÂN TÍCH GIẢM TRỪ
# =========================================================

elif menu == "📉 Phân tích giảm trừ":

    st.header(
        "📉 Phân tích các khoản giảm trừ"
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


    st.subheader(
        "🧮 Tính thu nhập tính thuế"
    )


    deduction_data = pd.DataFrame({

        "Khoản mục": [

            "Tổng thu nhập Gross",

            "Trừ: Tổng bảo hiểm",

            "Trừ: Giảm trừ bản thân",

            "Trừ: Giảm trừ người phụ thuộc",

            "Thu nhập tính thuế"

        ],

        "Số tiền (đồng)": [

            gross_salary,

            insurance,

            personal_deduction,

            dependent_deduction,

            taxable_income

        ]

    })


    st.dataframe(
        deduction_data,
        use_container_width=True,
        hide_index=True
    )


    st.success(
        f"📊 Thu nhập tính thuế: "
        f"**{taxable_income:,.0f} đồng/tháng**"
    )


# =========================================================
# 18. PHÂN TÍCH THUẾ
# =========================================================

elif menu == "🧮 Phân tích thuế":

    st.header(
        "🧮 Phân tích thuế TNCN"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Thu nhập tính thuế",
            f"{taxable_income:,.0f} đ"
        )


    with col2:

        st.metric(
            "Thuế TNCN phải nộp",
            f"{tax:,.0f} đ"
        )


    st.divider()


    if taxable_income == 0:

        st.success(
            "✅ Bạn không phát sinh thuế TNCN "
            "theo công thức hiện tại."
        )

    else:

        st.warning(
            f"⚠️ Thu nhập tính thuế của bạn là "
            f"{taxable_income:,.0f} đồng/tháng."
        )


    st.subheader(
        "📈 Tỷ lệ thuế trên tổng Gross"
    )


    if gross_salary > 0:

        tax_ratio = (
            tax
            / gross_salary
        )

    else:

        tax_ratio = 0


    st.progress(
        min(
            max(
                tax_ratio,
                0.0
            ),
            1.0
        )
    )


    st.write(
        f"Thuế TNCN chiếm khoảng "
        f"**{tax_ratio * 100:.2f}%** "
        f"tổng thu nhập Gross."
    )


# =========================================================
# 19. BÁO CÁO CHI TIẾT
# =========================================================

elif menu == "📊 Báo cáo chi tiết":

    st.header(
        "📊 Báo cáo phân tích thu nhập"
    )


    report = pd.DataFrame({

        "Khoản mục": [

            "Lương cơ bản",

            "Tiền làm thêm",

            "Tiền thưởng",

            "Phụ cấp",

            "Thu nhập khác",

            "TỔNG THU NHẬP GROSS",

            "BHXH",

            "BHYT",

            "BHTN",

            "TỔNG BẢO HIỂM",

            "Giảm trừ bản thân",

            "Giảm trừ người phụ thuộc",

            "THU NHẬP TÍNH THUẾ",

            "THUẾ TNCN",

            "LƯƠNG NET"

        ],


        "Số tiền (đồng)": [

            luong_co_ban,

            lam_them,

            thuong,

            phu_cap,

            thu_nhap_khac,

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
        report,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    st.subheader(
        "📌 Tóm tắt kết quả"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Tổng Gross",
            f"{gross_salary:,.0f} đ"
        )


    with col2:

        st.metric(
            "Tổng khấu trừ",
            f"{insurance + tax:,.0f} đ"
        )


    with col3:

        st.metric(
            "Lương Net",
            f"{net_salary:,.0f} đ"
        )


# =========================================================
# 20. BIỂU THUẾ
# =========================================================

elif menu == "📚 Biểu thuế":

    st.header(
        "📚 Biểu thuế lũy tiến từng phần"
    )


    tax_table = pd.DataFrame({

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
        tax_table,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    st.subheader(
        "🧮 Công thức tổng quát"
    )


    st.info(
        "Tổng Gross = "
        "Lương cơ bản + Làm thêm + Thưởng "
        "+ Phụ cấp + Thu nhập khác"
    )


    st.info(
        "Tổng bảo hiểm = "
        "BHXH + BHYT + BHTN"
    )


    st.info(
        "Thu nhập tính thuế = "
        "Gross - Tổng bảo hiểm "
        "- Giảm trừ bản thân "
        "- Giảm trừ người phụ thuộc"
    )


    st.info(
        "Lương Net = "
        "Gross - Tổng bảo hiểm - Thuế TNCN"
    )


# =========================================================
# 21. FOOTER
# =========================================================

st.divider()

st.caption(
    "💰 Hệ thống phân tích Thuế Thu nhập cá nhân "
    "| Công cụ hỗ trợ tính toán và tham khảo"
)
