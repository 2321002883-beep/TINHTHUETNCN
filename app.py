import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính Thuế TNCN",
    page_icon="💰",
    layout="wide"
)

st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN")

st.markdown("---")

st.header("Nhập thông tin")

col1, col2 = st.columns(2)

with col1:
    gross_salary = st.number_input(
        "Lương Gross (đồng/tháng)",
        min_value=0,
        value=30000000,
        step=1000000
    )

with col2:
    dependents = st.number_input(
        "Số người phụ thuộc",
        min_value=0,
        value=0,
        step=1
    )

st.markdown("---")

###########################################################
# Bảo hiểm
###########################################################

BHXH = gross_salary * 0.08
BHYT = gross_salary * 0.015
BHTN = gross_salary * 0.01

insurance = BHXH + BHYT + BHTN

###########################################################
# Giảm trừ
###########################################################

personal_deduction = 15_500_000
dependent_deduction = dependents * 6_200_000

###########################################################
# Thu nhập tính thuế
###########################################################

taxable_income = gross_salary - insurance - personal_deduction - dependent_deduction

if taxable_income < 0:
    taxable_income = 0

###########################################################
# Hàm tính thuế lũy tiến
###########################################################

def calculate_tax(income):

    tax = 0

    if income <= 10_000_000:
        tax = income * 0.05

    elif income <= 30_000_000:
        tax = (
            10_000_000 * 0.05 +
            (income - 10_000_000) * 0.10
        )

    elif income <= 60_000_000:
        tax = (
            10_000_000 * 0.05 +
            20_000_000 * 0.10 +
            (income - 30_000_000) * 0.20
        )

    elif income <= 100_000_000:
        tax = (
            10_000_000 * 0.05 +
            20_000_000 * 0.10 +
            30_000_000 * 0.20 +
            (income - 60_000_000) * 0.30
        )

    else:
        tax = (
            10_000_000 * 0.05 +
            20_000_000 * 0.10 +
            30_000_000 * 0.20 +
            40_000_000 * 0.30 +
            (income - 100_000_000) * 0.35
        )

    return tax

tax = calculate_tax(taxable_income)

###########################################################
# Lương thực nhận
###########################################################

net_salary = gross_salary - insurance - tax

###########################################################
# Hiển thị kết quả
###########################################################

st.header("📊 KẾT QUẢ")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "BHXH (8%)",
        f"{BHXH:,.0f} đ"
    )

    st.metric(
        "BHYT (1.5%)",
        f"{BHYT:,.0f} đ"
    )

    st.metric(
        "BHTN (1%)",
        f"{BHTN:,.0f} đ"
    )

    st.metric(
        "Tổng bảo hiểm",
        f"{insurance:,.0f} đ"
    )

with col2:

    st.metric(
        "Giảm trừ bản thân",
        f"{personal_deduction:,.0f} đ"
    )

    st.metric(
        "Giảm trừ người phụ thuộc",
        f"{dependent_deduction:,.0f} đ"
    )

    st.metric(
        "Thu nhập tính thuế",
        f"{taxable_income:,.0f} đ"
    )

    st.metric(
        "Thuế TNCN",
        f"{tax:,.0f} đ"
    )

st.markdown("---")

st.success(f"💵 LƯƠNG THỰC NHẬN: {net_salary:,.0f} đồng/tháng")

st.markdown("---")

st.subheader("Chi tiết")

st.table({
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
})

st.markdown("---")

st.info("""
Biểu thuế lũy tiến từng phần

Bậc 1: Đến 10 triệu: 5%

Bậc 2: Trên 10 - 30 triệu: 10%

Bậc 3: Trên 30 - 60 triệu: 20%

Bậc 4: Trên 60 - 100 triệu: 30%

Bậc 5: Trên 100 triệu: 35%
""")
