import streamlit as st

# App configuration
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# Custom title with emoji
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Perform basic arithmetic operations with ease!</p>", unsafe_allow_html=True)

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter First Number 🔢", format="%.2f", value=0.0)

with col2:
    num2 = st.number_input("Enter Second Number 🔢", format="%.2f", value=0.0)

# Dropdown for operation selection
operation = st.selectbox(
    "Select Operation ➕➖✖️➗",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)", "Modulus (%)")
)

# Calculate button with color
if st.button("💡 Calculate Result"):
    st.markdown("---")  # Horizontal line
    result = None

    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            result = num1 / num2
        elif operation == "Modulus (%)":
            result = num1 % num2

        st.success(f"✅ The result of **{operation}** is: **{result}**")

    except ZeroDivisionError:
        st.error("❌ Error: Cannot divide or mod by zero.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🧠 Built with <b>Streamlit</b> | Made by YOU 💙</p>", unsafe_allow_html=True)
