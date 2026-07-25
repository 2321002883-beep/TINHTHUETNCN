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
# 2. TIÊU ĐỀ
# =========================================================

st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN")

st.caption(
    "Công cụ hỗ trợ tính toán Lương Gross - Thuế TNCN - Lương Net"
)

st.divider()


# =========================================================
# 3. NHẬP THÔNG TIN
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
# 4. TÍNH BẢO HIỂM
# =========================================================

BHXH = gross_salary * 0.08

BHYT = gross_salary * 0.015

BHTN = gross_salary * 0.01

insurance = BHXH + BHYT + BHTN


# =========================================================
# 5. TÍNH GIẢM TRỪ
# =========================================================

personal_deduction = 15500000

dependent_deduction = (
    dependents * 6200000
)


# =========================================================
# 6. TÍNH THU NHẬP TÍNH THUẾ
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
# 7. HÀM TÍNH THUẾ TNCN
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
# 8. TÍNH THUẾ
# =========================================================

tax = calculate_tax(
    taxable_income
)


# =========================================================
# 9. TÍNH LƯƠNG NET
# =========================================================

net_salary = (
    gross_salary
    - insurance
    - tax
)


# =========================================================
# 10. KẾT QUẢ LƯƠNG THỰC NHẬN
# =========================================================

st.divider()

st.header("💰 Kết quả lương thực nhận")

st.success(
    f"💵 LƯƠNG THỰC NHẬN: "
    f"{net_salary:,.0f} đồng/tháng"
)


# =========================================================
# 11. KẾT QUẢ TỔNG QUAN
# =========================================================

st.subheader("📊 Kết quả tổng quan")

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
# 12. TỶ LỆ LƯƠNG THỰC NHẬN
# =========================================================

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
    f"Bạn thực nhận khoảng "
    f"**{net_ratio * 100:.1f}%** "
    f"so với mức lương Gross."
)


# =========================================================
# 13. CHI TIẾT BẢO HIỂM
# =========================================================

st.divider()

st.header("🏦 Chi tiết bảo hiểm")

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
# 14. CHI TIẾT GIẢM TRỪ
# =========================================================

st.header("📉 Chi tiết giảm trừ")

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
# 15. THÔNG BÁO THUẾ
# =========================================================

st.header("🔔 Thông báo")

if taxable_income == 0:

    st.success(
        "✅ Thu nhập tính thuế bằng 0. "
        "Bạn không phát sinh thuế TNCN "
        "theo công thức hiện tại."
    )

else:

    st.warning(
        f"⚠️ Thu nhập tính thuế của bạn là "
        f"{taxable_income:,.0f} đồng/tháng."
    )


# =========================================================
# 16. BẢNG CHI TIẾT
# =========================================================

st.divider()

st.header("🧾 Chi tiết tính lương")

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
# 17. BIỂU THUẾ
# =========================================================

st.divider()

st.header("📚 Biểu thuế lũy tiến từng phần")

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
# 18. CÔNG THỨC TÍNH
# =========================================================

st.header("🧮 Công thức tính")

with st.expander("Xem công thức"):

    st.write(
        "Tổng bảo hiểm = BHXH + BHYT + BHTN"
    )

    st.write(
        "Thu nhập tính thuế = "
        "Lương Gross - Tổng bảo hiểm "
        "- Giảm trừ bản thân "
        "- Giảm trừ người phụ thuộc"
    )

    st.write(
        "Lương Net = "
        "Lương Gross - Tổng bảo hiểm - Thuế TNCN"
    )


# =========================================================
# 19. FOOTER
# =========================================================

st.divider()

st.caption(
    "💰 Ứng dụng tính Thuế Thu nhập cá nhân | "
    "Công cụ hỗ trợ tính toán và tham khảo"
)
